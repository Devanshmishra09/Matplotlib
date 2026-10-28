# Question 2: Department-Wise Employee Performance

# Chart Type: Bar Chart

# An IT company wants to compare the average employee performance score across its departments.

# Dataset

# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "Employee": ["Aman", "Priya", "Rahul", "Neha", "Rohit",
#                  "Sneha", "Vikas", "Pooja", "Arjun", "Simran",
#                  "Karan", "Meena"],
#     "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales",
#                    "IT", "Finance", "Finance", "Sales", "HR", "Finance"],
#     "Performance": [88, 76, 92, 81, 69, 95, 74, 86, 91, 72, 84, 79],
#     "Projects_Completed": [5, 3, 7, 4, 2, 6, 3, 5, 8, 4, 5, 4]
# }

# df = pd.DataFrame(data)

# Tasks

# 1. Calculate the average performance score of each department using Pandas.
# 2. Find the department with the highest average performance.
# 3. Calculate the total projects completed by each department.
# 4. Create a bar chart comparing average department performance.
# 5. Use different bar colors and add suitable titles and axis labels.
# 6. Set the Y-axis limit from 0 to 100 and show ticks at intervals of 10.
# 7. Add a grid to improve readability.


import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Employee": ["Aman", "Priya", "Rahul", "Neha", "Rohit",
                 "Sneha", "Vikas", "Pooja", "Arjun", "Simran",
                 "Karan", "Meena"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales",
                   "IT", "Finance", "Finance", "Sales", "HR", "Finance"],
    "Performance": [88, 76, 92, 81, 69, 95, 74, 86, 91, 72, 84, 79],
    "Projects_Completed": [5, 3, 7, 4, 2, 6, 3, 5, 8, 4, 5, 4]
}
df = pd.DataFrame(data)
print(df)
a=df.groupby("Department")["Performance"].mean()
print(a)
b=a.sort_values(ascending=False)
print(b)
c=df.groupby("Department")["Projects_Completed"].sum()
print(c)
col=["red","blue","green","navy"]
plt.bar(df["Department"],df["Performance"])
plt.title("Department-Wise Employee Performance",color="red",fontsize=25)
plt.xlabel("Department",color="purple",fontsize=13)
plt.ylabel("Department",color="purple",fontsize=13)
plt.yticks(range(0,110,10))
plt.grid()
plt.savefig("project_2.png")
plt.show()