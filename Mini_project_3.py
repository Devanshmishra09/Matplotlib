# Question 3: City-Wise Customer Satisfaction

# Chart Type: Horizontal Bar Chart

# A service company collects customer satisfaction ratings from different cities. Analyze which cities perform best and worst.

# Dataset


# Tasks

# 1. Find the city with the highest satisfaction score.
# 2. Find the city with the highest number of complaints.
# 3. Calculate the average satisfaction score across all cities.
# 4. Create a horizontal bar chart of satisfaction scores by city.
# 5. Use different colors for the bars.
# 6. Set the X-axis limit from 0 to 100.
# 7. Add a title, axis labels, and grid.
# 8. Display the cities in descending order of satisfaction score.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "City": ["Lucknow", "Delhi", "Mumbai", "Pune", "Jaipur",
             "Kanpur", "Bhopal", "Patna", "Noida", "Agra"],
    "Satisfaction_Score": [82, 74, 91, 88, 67, 79, 85, 62, 94, 71],
    "Complaints": [45, 78, 32, 39, 67, 51, 41, 82, 28, 63],
    "Customers": [450, 720, 850, 610, 390, 520, 480, 350, 680, 420]
}

df = pd.DataFrame(data)
df.sort_values("Satisfaction_Score",ascending=False,inplace=True)
print(df)
df.sort_values("Complaints",ascending=False,inplace=True)
print(df)
a=df.groupby("City")["Satisfaction_Score"].mean()
print(a)
var=["pink","red","green","orange","black"]
plt.barh(df["City"],df["Satisfaction_Score"],color=var)
plt.xticks(range(0,110,10))
plt.title("City-Wise Customer Satisfaction",color="navy",fontsize=22)
plt.xlabel("Satisfaction_Score",color="purple",fontsize=20)
plt.ylabel("City",color="purple",fontsize=20)
plt.savefig("project3.png")
plt.show()