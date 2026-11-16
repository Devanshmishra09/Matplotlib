import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df=pd.read_excel("retail_sales_matplotlib_minor_project.xlsx")


# # # Data inspection -Display shape, columns, data types, first 10 rows, summary statistics, missing values, 
# # # and duplicate Order_ID count. Clean missing or duplicate records if found.
print("========================================================")
print("----------------------Data inspection--------------------- ")
print("========================================================")
print(df.shape)
print(df.columns.tolist())
print(df.info())
print(df.head(10))
print(df.describe())
print(df.isna().sum())
print(df.duplicated("Order_ID").sum())
print("========================================================")

# # #Q2 — Feature engineering - 
# # # Prepare useful analysis columns
# # #   Convert Order_Date to datetime if needed. Create Profit_Margin_Pct = Profit_INR / Net_Sales_INR * 100, 
# # #   handling zero denominators safely. Create Month_Number to preserve calendar order.
Short_months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}
print("=================================================")
print("----------------Feature engineering ---------------")
print("=================================================")



Profit_Margin_percentage=df["Profit_INR"]/df["Net_Sales_INR"]*100.
print("Profit_Margin_percentage  =  ",Profit_Margin_percentage)

df["Month_Number"] = pd.to_datetime(df["Month"], format="%b").dt.month
print(df["Month_Number"])
print("=================================================")


# # Q3 — KPI summary
# # Calculate business KPIs
# #  Calculate total Net Sales, total Profit, total Orders, total Units, average Order Value, 
# # average Customer Rating, and Return Rate. Show a neat Pandas summary.
print("=================================================")
print("----------------KPI summary----------------------")
print("=================================================")

Total_Net_sales =df["Net_Sales_INR"].sum()
print("Total_Net_sales  =  ",Total_Net_sales)

Total_profit = df["Profit_INR"].sum()
print("Total_profit  =  ",Total_profit)

Total_orders=df["Order_ID"].nunique()
print("Total_orders  =  ",Total_orders)

total_Units=df["Units"].sum()
print("total_Units  =  ",total_Units)

average_order=df["Units"].mean()
print("average_order  =  ",average_order)

Average_customer_rating=df["Customer_Rating"].mean()
print(" Average_customer_rating  =  ",Average_customer_rating)

Total_return=df["Returned"].count()
print("Total_return  =  ",Total_return)

Return_Rate=(Total_return)/(Total_orders)*100
print("Return_Rate  =  ",Return_Rate)

print("=================================================")

# Q4 — Monthly trend
# Analyze monthly sales and profit
# Group by month and calculate Net_Sales_INR and Profit_INR totals. Plot sales and profit
# as two lines in one chart or separate subplots. Add title, labels, markers, colors, grid, and legend.

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Total = ["2L", "7L", "12L", "17L", "22L", "27L", "32L", "37L", "42L", "47L","50L"]


Sales_inr=df.groupby("Month_Number")["Net_Sales_INR"].sum()



Profit_inr=df.groupby("Month_Number")["Profit_INR"].sum()
plt.figure(figsize=(15,8))
print(Profit_inr)
plt.subplot(2,2,1)
plt.plot(Sales_inr.index,Sales_inr.values,marker="*",color="Blue",label="Sales")
plt.xticks(range(1,13),labels=month_names,weight=12,color="#2D3748",fontsize=10)

plt.text(1,4400000," ₹ 4356892",fontsize=9)
plt.text(2,4200000," ₹ 4128793",fontsize=9)
plt.text(3,3200000," ₹ 3114912",fontsize=9)
plt.text(4,4700000," ₹ 4648282",fontsize=9)
plt.text(5,2200000," ₹ 2138591",fontsize=9)
plt.text(6,4700000," ₹ 4639741",fontsize=9)
plt.text(7,3700000," ₹ 3823858",fontsize=9)
plt.text(8,4600000," ₹ 4505341",fontsize=9)
plt.text(9,2600000," ₹ 2541882",fontsize=9)
plt.text(10,4800000," ₹ 4734604",fontsize=9)
plt.text(11,3700000," ₹ 3621247",fontsize=9)
plt.text(12,5000000," ₹ 4978264",fontsize=9)

plt.plot(Sales_inr.index,Profit_inr.values,marker="o",color="Green",label="Profit")

plt.text(1 ,800000 ,"₹ 1160602",fontsize=9)
plt.text(2 ,1200000,"₹ 1128130",fontsize=9)
plt.text(3,700000,"₹ 858289",fontsize=9)
plt.text(4,1300000,"₹ 1236440",fontsize=9)
plt.text(5,400000,"₹ 595579",fontsize=9)
plt.text(6,1400000,"₹ 1351547",fontsize=9)
plt.text(7,800000,"₹ 1003400",fontsize=9)
plt.text(8,1200000,"₹ 1169098",fontsize=9)
plt.text(9,500000,"₹ 685203",fontsize=9)
plt.text(10,1400000,"₹ 1331549",fontsize=9)
plt.text(11,800000,"₹ 911942",fontsize=9)
plt.text(12,1400000,"₹ 1325369",fontsize=9)


plt.yticks(range(100000,5100000,300000),color="#1A365D")
plt.xlabel("Month",color="#1A365D",weight="bold")
plt.ylabel("Rupees in Lakhs  ",color="#1A365D",weight="bold")
plt.title("Monthly Sales & Profit Performance", color="#0F2B52", fontweight="bold", pad=15)
plt.grid(True, linestyle="--", alpha=0.5, color="#CBD5E0")
plt.legend(facecolor="#FFFFFF", edgecolor="#CBD5E0", loc="upper left")
plt.ticklabel_format(style="plain",axis="y")


# #Q5 — Product analysis
# #Find best-selling products
# #Group by Product and calculate total net sales, profit, units sold, and average rating. Sort by net sales descending. 
# # Plot top 8 products in a bar chart. Use plt.text() to show values above bars.

b= df.groupby("Product").agg({
    "Net_Sales_INR": "sum",
    "Profit_INR": "sum",
    "Units": "sum",
    "Customer_Rating": "mean"
})
print(b)

top_8=b.sort_values("Product",ascending=False)
print(top_8)
plt.subplot(2,2,2)
b=plt.bar(top_8.index, top_8["Net_Sales_INR"], color="royalblue", edgecolor="black")
plt.bar_label(b,fmt="%.0f")
plt.title("Top 8 Best-Selling Products by Net Sales", fontsize=14, fontweight="bold")
plt.xticks(rotation=35,fontsize=10)
plt.xlabel("Product Names",fontsize=11,weight="bold")
plt.ylabel("Net Sales (INR in Lakhs )",fontsize=11,weight="bold")

plt.yticks(range(1000000,17000000,1500000))

plt.grid(True, linestyle="--", alpha=0.5)



plt.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.ticklabel_format(style="plain",axis="y")


# Q6 — City performance
# Compare city performance
# Group by City and calculate net sales, profit, order count, and average rating. 
# Sort cities by net sales. Create a horizontal bar chart and set suitable axis limits and ticks.


Calculated_net_sales=df.groupby("City")["Net_Sales_INR"].sum()
calculated_Profit=df.groupby("City")["Profit_INR"].sum()
Calculated_Order_count=df.groupby("City")["Order_ID"].count()
calculated_Rating=df.groupby("City")["Customer_Rating"].mean()
sorted_city=Calculated_net_sales.sort_values(ascending=True)
plt.subplot(2,2,3)
a=plt.barh(sorted_city.index,sorted_city.values,color="#8A810D")
plt.bar_label(a,fmt="%.0f")
plt.title(" Comparing city performance",color="#140664",fontsize=14,weight="bold")
plt.ylabel("City",color="#020001",fontsize=14)
plt.xlabel("Net_Sales_inr",color="#0C0109",fontsize=11,weight="bold")
plt.xticks(range(1000000,8000000,1000000))
plt.ticklabel_format(style="plain",axis="x")
plt

# Q7 — Category contribution
# Analyze category revenue share
# Calculate each Category's share of total Net Sales. Create a pie chart with labels
#  autopct='%1.1f%%', distinct colors, and startangle=90. 
# Change individual category label colors using the texts returned by plt.pie().

Category_type=df.groupby("Category")["Net_Sales_INR"].sum()
plt.subplot(2,2,4)
plt.pie(Category_type.values,labels=Category_type.index,autopct="%1.1f%%", wedgeprops={'edgecolor': 'white', 'linewidth': 2})
plt.title("Analyze category revenue share",color="#07000FFF",fontsize=14,weight="bold")
plt.grid()

plt.suptitle("Retail Sales Dashboard",fontsize=20,color="royalblue",fontweight="bold")
plt.tight_layout()
# plt.savefig("Retail_Sales.png")
plt.show()