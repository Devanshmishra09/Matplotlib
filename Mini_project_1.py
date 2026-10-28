# Question 1: Monthly Sales Performance Analysis

# Chart Type: Line Plot

# A retail company wants to analyze its monthly sales performance across three product categories.

# Dataset



# Tasks

# 1. Calculate total sales for each product category.
# 2. Identify the month with the highest total sales.
# 3. Create a line plot showing monthly sales for all three categories.
# 4. Use different colors, markers, and line styles for each category.
# 5. Add a suitable title, X-axis label, Y-axis label, grid, and legend.
# 6. Display all 12 months on the X-axis.
# 7. Save the chart as "monthly_sales.png".


import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Electronics": [45000, 52000, 48000, 61000, 58000, 72000,
                    68000, 75000, 82000, 90000, 105000, 120000],
    "Clothing": [30000, 28000, 35000, 40000, 42000, 38000,
                 45000, 48000, 50000, 62000, 75000, 85000],
    "Furniture": [25000, 27000, 22000, 30000, 32000, 35000,
                  33000, 40000, 38000, 42000, 50000, 65000]
}

df = pd.DataFrame(data)
a=(df[["Electronics","Clothing","Furniture"]].sum())
print(a)
df["Total Sales"]=(df[["Electronics","Clothing","Furniture"]].sum(axis=1))
print(df)
c=df["Total Sales"].sort_values(ascending=False)
print(c)
plt.plot(df["Month"],df["Electronics"],label="Electronics",marker="o")
plt.plot(df["Month"],df["Clothing"],label="Clothing",marker="*")
plt.plot(df["Month"],df["Furniture"],label="Furniture",marker="x")
plt.title("Monthly Sales Performance Analysis",color="red",fontsize=20)
plt.xlabel("Months",color="purple",fontsize=13)
plt.ylabel("Sales",color="purple",fontsize=13)
plt.legend()
plt.grid()
plt.savefig("Project_3.png")
plt.show()