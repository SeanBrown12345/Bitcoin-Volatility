import json
from datetime import datetime, timezone
import numpy as np
import pandas as pd
import yfinance as yf
import joblib

FEATURES = ["vol_5d", "vol_20d", "vol_30d", "return_5d", "vol_change", "close"]

btc = yf.download("BTC-USD", start="2014-01-01", auto_adjust=True)
btc = btc[["Close", "Volume"]].dropna()

btc["log_return"] = np.log(btc["Close"] / btc["Close"].shift(1))
btc["target_vol_5d"] = btc["log_return"].rolling(5).std().shift(-5)

btc["vol_5d"] = btc["log_return"].rolling(5).std()
btc["vol_20d"] = btc["log_return"].rolling(20).std()
btc["vol_30d"] = btc["log_return"].rolling(30).std()
btc["return_5d"] = btc["log_return"].rolling(5).sum()
btc["vol_change"] = btc["Volume"].pct_change()
btc["close"] = btc["Close"].shift(1)

btc = btc.dropna()

model = joblib.load("models/btc_vol_xgb.joblib")

last_week_actual = btc["target_vol_5d"].iloc[-7:]
last_x = btc[FEATURES].iloc[[-1]]
next_vol_pred = float(model.predict(last_x)[0])

future_dates = pd.bdate_range(btc.index[-1] + pd.Timedelta(days=1), periods=5)
future_forecast = pd.Series([next_vol_pred] * 5, index=future_dates)

payload = {
    "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "as_of_date": btc.index[-1].strftime("%Y-%m-%d"),
    "last_week": [{"date": d.strftime("%Y-%m-%d"), "vol": float(v)} for d, v in last_week_actual.items()],
    "forecast": [{"date": d.strftime("%Y-%m-%d"), "vol": float(v)} for d, v in future_forecast.items()],
    "next_vol_pred": next_vol_pred,
}

with open("public/bitcoin_vol_forecast.json", "w") as f:
    json.dump(payload, f, indent=2)