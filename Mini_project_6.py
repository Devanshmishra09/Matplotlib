
# Question 6: Online Shopping Revenue Share each category

# Chart Type: Pie Chart

# An e-commerce company wants to analyze the revenue contribution of different product categories.

# Dataset

# Tasks

# 1. Calculate total revenue across all product categories.
# 2. Identify the category with the highest revenue.
# 3. Calculate the percentage contribution o to total revenue using Pandas.
# 4. Create a pie chart showing revenue distribution.
# 5. Display category names and percentages using "labels" and "autopct="%1.1f%%"".
# 6. Use a different color for each category.
# 7. Change the label color of individual categories using the "texts" returned by "plt.pie()".
# 8. Set "startangle=90" and add a suitable title.
# 9. Explain which category contributes the most and least revenue.



import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Category": ["Electronics", "Fashion", "Home Decor",
                 "Books", "Beauty", "Sports"],
    "Revenue": [250000, 180000, 120000, 50000, 90000, 60000],
    "Orders": [420, 680, 300, 250, 510, 220]
}

df = pd.DataFrame(data)
print(df)
a=df["Revenue"].sum()
print(df.loc[df["Revenue"].idxmax()])
df["total_Revenue"]=(df["Revenue"]/a)*100
print(df)
plt.pie(df["Revenue"],labels=df["Category"],autopct="%1.1f%%", startangle=90 )
plt.title("Online Shopping Revenue Share each category",color="navy",fontsize=20)
plt.savefig("project_6.png")
plt.show()