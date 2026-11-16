import matplotlib.pyplot as plt

# Data
languages = ["Python", "JavaScript", "SQL", "TypeScript", "Java"]
popularity = [68, 62, 51, 39, 30]
colors = ["#3b82f6", "#f59e0b", "#10b981", "#6366f1", "#ef4444"]

# Create plot
fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.bar(languages, popularity, color=colors, width=0.55)

# Add data labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{height}%",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 4),
        textcoords="offset points",
        ha="center",
        fontweight="bold",
    )

# Customize
ax.set_title("Developer Language Usage", fontsize=14, fontweight="bold")
ax.set_ylabel("Percentage (%)")
ax.set_ylim(0, 80)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("Practice_2.png")
plt.show()
