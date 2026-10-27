# Tasks 
#  1 Study_Hours aur  marks ka line plot banao 
#  2 Line colour red ,marker circle aur linestyle dashed rakho 
#  3 Chat ka title  X- axis aur Y axis label add karo 
#  4 Grid enable karo aur legend Display karo 
#  5 Sabhi students ke marks ka bar chart banao . Har chart ka name  X-axis per show hona chaheye .
#  6 Bar chart main  Y-axis  ki limit  0 se 100 tak set karo aur ticks  20-20 ke gap pe set karo 
#  7 Attendance  ka histogram banao aur "bins=5" use karo 
#  8 Pass aur fail students ka pie chart banao . jinke marks 40 ya use zayada  hain  woh  Pass  hain 
#  9 Pie chart main Percentage  "autopct="%1.1f%%"" se show karo 
#  10 har chart main sutaible title aur labels add karo  aur "plt.show()" se display  karo 

# Condition : Har chart ke liye se alag se figure banao. Pandas ka use sirf Dataset  Banane  ke liye karo . Plotting Matplotlib se hi karni hai 

# Data set 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
data={
    "Student": ["Aman","priya","Rahul","Neha","Rohit","Sneha","Vikash","Pooja","Arjun","Simran"],
    "Marks": [35,45,55,70,85,50,92,60,96,80],
    "Study_Hours":[1,2,3,4,5,2,6,3,7,5],
    "Attendance":[65,70,75,85,95,72,98,80,99,90]
}
df=pd.DataFrame(data)
a=df["Study_Hours"].sort_values(ascending=True)
print(a)
df["Status"]="Fail"
df.loc[df["Marks"]>40,"Status"]="Pass"
print(df)
c=df["Status"].value_counts()
print(c)

plt.subplot(2,3,1)
plt.plot(a,df["Marks"],color="red",marker="o",linestyle="--")
plt.xlabel("Students Study_hours",font="u",fontsize=10,color="navy")
plt.ylabel("Students Marks",color="navy",fontsize=10,font="underline")
plt.title("Student study_hour and marks chart",color="navy",weight='bold',fontsize=15)
plt.plot(a,df["Attendance"],color="blue",marker="*",linestyle="--")
plt.grid()
plt.legend()
plt.subplot(2,3,2)
plt.pie(df["Marks"],labels=df["Student"],autopct="%1.f%%")
plt.title("Students and Marks Percentage",color="red",weight="bold",style="italic",fontsize=15)
plt.subplot(2,3,3)
plt.bar(df["Student"],df["Marks"])
plt.ylim(0,100)
plt.yticks(range(0,120,20))
plt.yticks(rotation=45)
plt.xticks(rotation=45)
plt.xlabel("Students Marks",font="u",fontsize=10,color="fuchsia")
plt.ylabel("Students Name",color="olive",fontsize=10,font="underline")
plt.title("Students and Marks",color="Purple",weight="bold",style="italic",fontsize=15)
plt.subplot(2,3,4)
plt.hist(df["Attendance"],bins=5)
plt.xlabel("Students Attendance ",font="u",fontsize=10,color="indigo")
plt.ylabel("Numers of Students",color="Green",fontsize=10)
plt.title("Students Attendance Report ",color="Purple",weight="bold",style="italic",fontsize=15)
plt.subplot(2,3,5)
plt.pie(c,labels=c.index,autopct="%1.1f%%")
plt.title("Students Pass and Fail Report ",color="Purple",weight="bold",style="italic",fontsize=15)
plt.savefig("Students Dashboard.png")
plt.show()
