import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Data for the betas
stocks = ['Microsoft (MSFT)', 'Procter & Gamble (PG)', 'Disney (DIS)', 'UnitedHealth (UNH)', 'Verizon (VZ)']
betas = [0.89, 1.40, 0.40, 0.39, 0.60]  # Reordered betas
colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#d62728']  # Matching previous chart colors

# Portfolio Beta Calculation
allocation = 0.2  # 20% for each stock
portfolio_beta = np.dot(betas, [allocation] * len(betas))

# Create figure
plt.figure(figsize=(14, 8))

# Bar chart for individual stock betas with specific colors
plt.bar(stocks, betas, color=colors, width=0.6, label='Individual Stock Betas')

# Add Portfolio Beta as a yellow dashed line
plt.axhline(y=portfolio_beta, color='yellow', linestyle='--', linewidth=2, label=f'Portfolio Beta: {portfolio_beta:.2f}')

# Add Market Beta as a bright red line
plt.axhline(y=1, color='red', linewidth=2, label='Market Beta: 1')

# Add text labels for each bar
for i, beta in enumerate(betas):
    plt.text(i, beta + 0.05, f"{beta:.2f}", ha='center', fontsize=12)

# Adding title and labels
plt.title("Stock Betas with Portfolio and Market Beta", fontsize=16)
plt.xlabel("Company Ticker", fontsize=14)
plt.ylabel("Beta", fontsize=14)
plt.ylim(0, max(betas) + 0.5)  # Adjust y-axis for better visualization

# Adding grid and legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Show plot
plt.show()
