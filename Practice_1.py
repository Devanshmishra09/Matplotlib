import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
rng = np.random.default_rng(42)
x = rng.normal(50, 10, 200)
y = x * 1.5 + rng.normal(0, 12, 200)

# Create 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

# Left plot: Scatter
ax1.scatter(x, y, alpha=0.7, color="#8b5cf6", edgecolors="white")
ax1.set_title("Correlation Scatter Plot")
ax1.set_xlabel("Variable X")
ax1.set_ylabel("Variable Y")
ax1.grid(True, alpha=0.3)

# Right plot: Histogram
ax2.hist(x, bins=18, color="#14b8a6", edgecolor="black", alpha=0.8)
ax2.set_title("Distribution of Variable X")
ax2.set_xlabel("Value")
ax2.set_ylabel("Frequency")

fig.suptitle("Data Exploration Dashboard", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig("Practice_1.png")
plt.show()
