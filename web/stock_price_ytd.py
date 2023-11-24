# filename: stock_price_ytd.py
import matplotlib.pyplot as plt

# Placeholder data for stock price change YTD
meta_stock_prices = [100, 110, 115, 120, 125, 130, 135, 140, 145, 150]  # Placeholder values for META stock prices
tesla_stock_prices = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290]  # Placeholder values for TESLA stock prices
days = range(1, 11)  # Placeholder values for days

# Plotting the stock price change YTD
plt.plot(days, meta_stock_prices, label='META')
plt.plot(days, tesla_stock_prices, label='TESLA')
plt.xlabel('Days YTD')
plt.ylabel('Stock Price')
plt.title('Stock Price Change YTD')
plt.legend()
plt.savefig('stock_price_ytd.png')
plt.show()