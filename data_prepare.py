import pandas as pd
import numpy as np
import yfinance as yf
from scipy import stats


#households = pd.read_csv('household_disposable_income.csv')
#print(households.head(100))

#print(households['TIME'])


period = "1y"

# Obtain information about the security
security_name = "MSFT"
security = yf.Ticker(security_name)
security_data = security.history(period=period).pct_change(1)
security_data = security_data.groupby(by=[security_data.index.year, security_data.index.month]).mean()

# Obtain information about the exchange
market_name = "^IXIC"
market_data = yf.Ticker(market_name)
market_data = security.history(period=period).pct_change(1)
market_data = market_data.groupby(by=[market_data.index.year, market_data.index.month]).mean()



# Covariance
def cov(x, y):
    xbar, ybar = x.mean(), y.mean()
    return np.sum((x - xbar)*(y - ybar))/(len(x) - 1)

print(cov(np.array(security_data['Close']), np.array(market_data['Close'])))


print(cov(np.array(market_data['Close']), np.array(security_data['Close'])))

print(np.var(np.array(market_data['Close'])))


covariance = cov(np.array(market_data['Close']), np.array(security_data['Close']))
variance_market = np.var(np.array(market_data['Close']))

beta = covariance/variance_market
print(beta)

