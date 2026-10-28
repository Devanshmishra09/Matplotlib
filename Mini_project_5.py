#

# Question 5: Employee Salary Distribution

# Chart Type: Histogram

# A company wants to understand the distribution of salaries among its employees.

# Dataset

# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "Employee_ID": list(range(101, 116)),
#     "Salary": [18000, 22000, 25000, 28000, 30000,
#                32000, 35000, 38000, 42000, 45000,
#                48000, 52000, 60000, 75000, 95000],
#     "Experience": [0, 1, 1, 2, 2, 3, 3, 4, 4, 5,
#                    5, 6, 7, 9, 12]
# }

# df = pd.DataFrame(data)

# Tasks

# 1. Calculate the mean, median, minimum, and maximum salary using Pandas.
# 2. Count employees earning more than ₹40,000.
# 3. Create a histogram of employee salaries using "plt.hist()".
# 4. Set "bins=5".
# 5. Customize the histogram color and edge color.
# 6. Add a title, X-axis label, Y-axis label, and grid.
# 7. Explain which salary range appears most frequently in the histogram.

#

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Employee_ID": list(range(101, 116)),
    "Salary": [18000, 22000, 25000, 28000, 30000,
               32000, 35000, 38000, 42000, 45000,
               48000, 52000, 60000, 75000, 95000],
    "Experience": [0, 1, 1, 2, 2, 3, 3, 4, 4, 5,
                   5, 6, 7, 9, 12]
}

df = pd.DataFrame(data)
a=df["Salary"].mean()
print(a)
b=df["Salary"].max()
print(b)
c=df["Salary"].min()
print(c)
d=df["Salary"].median()
print(d)
e=df.loc[df["Salary"]>40000]
print(e)
plt.hist(df["Salary"],bins=5,color="yellow",edgecolor="red")
plt.title("Employee Salary Distribution",color="red",fontsize="20")
plt.xlabel("Salary",color="red",fontsize=18)
plt.ylabel("NO.of salary frequarncy",color="red",fontsize=18)
plt.savefig("project7.png")
plt.show()