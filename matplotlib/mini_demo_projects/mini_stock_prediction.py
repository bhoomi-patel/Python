import numpy as np, pandas as pd, matplotlib.pyplot as plt

# 1 ── fake stock data ───────────────────────────────────────────────────────
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=60, freq='B')
price = 100 * (1 + np.random.normal(.001, .01, len(dates))).cumprod()
vol   = np.random.randint(1e5, 5e6, len(dates))
ma10  = pd.Series(price).rolling(10).mean()

# 2 ── figure + sub-plots (one above the other) ─────────────────────────────
plt.style.use('seaborn-v0_8-dark')          # one-line style upgrade
fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
fig.suptitle('Simple Stock Dashboard (Simulated)', fontsize=18, weight='bold')

# 3 ── price panel ──────────────────────────────────────────────────────────
ax_price = ax[0]
ax_price.plot(dates, price,  color='#2a9df4', lw=2,  label='Close')
ax_price.plot(dates, ma10,   color='#ff9900', lw=1.5, ls='--', label='10-Day SMA')
ax_price.fill_between(dates, price,  color='#2a9df4', alpha=.1)  # subtle area
ax_price.set_title('Price Trend',  fontsize=12)
ax_price.set_ylabel('Price  ($)')
ax_price.legend()
ax_price.grid(alpha=.3)

# 4 ── volume panel ─────────────────────────────────────────────────────────
ax_vol = ax[1]
ax_vol.bar(dates, vol, color='#777777', alpha=.6)
ax_vol.set_title('Daily Volume', fontsize=12)
ax_vol.set_xlabel('Date')
ax_vol.set_ylabel('Shares')
ax_vol.grid(alpha=.3)

# 5 ── final polish ─────────────────────────────────────────────────────────
fig.autofmt_xdate()                        # tilt date labels nicely
plt.tight_layout(rect=[0, 0.03, 1, 0.96])  # leave space for suptitle
plt.show()
