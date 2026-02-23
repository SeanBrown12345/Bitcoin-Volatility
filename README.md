# Bitcoin Volatility Forecasting

Dashhboard Webpage: https://seanbrown.io/bitcoin

Machine Learning–Based Forecasting of 5-Day Forward Realized Volatility for Bitcoin.

This project builds and deploys a supervised machine learning model to forecast short-horizon Bitcoin volatility. The system evaluates classical econometric benchmarks and demonstrates statistically significant improvement using XGBoost.

Forecasts are generated daily via an automated pipeline and published to a live dashboard.

---

## Project Overview

This repository contains:

- Data ingestion using historical Bitcoin market data  
- Feature engineering for volatility forecasting  
- Model training and validation  
- Benchmark comparison (Naive, GARCH, HAR)  
- Statistical testing (Diebold–Mariano)  
- Automated daily forecast generation  
- Deployment pipeline exporting JSON for web visualization  

**Target variable:**  
5-day forward realized volatility computed from log returns.

---

## Models Evaluated

| Model      | RMSE   |
|------------|--------|
| Baseline   | 0.0167 |
| GARCH(1,1) | 0.0146 |
| HAR        | 0.0135 |
| XGBoost    | 0.0127 |

XGBoost achieved statistically significant improvement over baseline models (Diebold–Mariano test, p < 0.05).

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/seanbrown12345/Bitcoin-Volatility.git
cd Bitcoin-Volatility
```

### 2. Create and Activate Environment

Using the provided environment.yml:
```bash
conda env create -f environment.yml
conda activate bitcoin
```

## Full Analysis & Model Development

The complete research workflow — including exploratory data analysis, feature engineering, model training, hyperparameter tuning, benchmark comparison, and statistical testing — is documented in the Jupyter notebook:

`Bitcoin Volatility.ipynb`

The notebook contains:

- Data preprocessing and log return computation  
- Volatility feature construction  
- Time-series cross-validation  
- XGBoost hyperparameter tuning  
- GARCH and HAR benchmark implementation  
- Diebold–Mariano statistical testing  
- Model performance comparison and interpretation  

The production script (`scripts/generate_forecast.py`) loads the trained model from this analysis and performs daily inference.

## Automated Daily Forecasting
A GitHub Actions workflow runs daily to:
1. Fetch fresh data
2. Generate updated forecasts
3. Commit the updated JSON
4. ublish via GitHub Pages

The forecast is visualized on a deployed React dashboard which can be found here: https://www.seanbrown.io/bitcoin

## Disclaimer
This project is for research and educational purposes only.
Forecasts are not investment advice.





```bash
git clone https://github.com/seanbrown12345/Bitcoin-Volatility.git
cd Bitcoin-Volatility
