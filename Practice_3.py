import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [12, 19, 15, 25, 32, 38]
expenses = [10, 12, 14, 16, 18, 20]

# Create plot
plt.figure(figsize=(8, 4.5))
plt.plot(months, revenue, marker="o", linewidth=2, color="#2563eb", label="Revenue ($K)")
plt.plot(months, expenses, marker="s", linestyle="--", color="#dc2626", label="Expenses ($K)")

# Customize
plt.title("First Half Financial Performance", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Amount ($ Thousands)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.savefig("Practice_3.png")
plt.show()
