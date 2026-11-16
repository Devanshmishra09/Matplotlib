import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df=pd.read_excel("retail_sales_matplotlib_minor_project.xlsx")


# # # # Data inspection -Display shape, columns, data types, first 10 rows, summary statistics, missing values, 
# # # # and duplicate Order_ID count. Clean missing or duplicate records if found.
# print("========================================================")
# print("----------------------Data inspection--------------------- ")
# print("========================================================")
# print(df.shape)
# print(df.columns.tolist())
# print(df.info())
# print(df.head(10))
# print(df.describe())
# print(df.isna().sum())
# print(df.duplicated("Order_ID").sum())
# print("========================================================")

# # # #Q2 — Feature engineering - 
# # # # Prepare useful analysis columns
# # # #   Convert Order_Date to datetime if needed. Create Profit_Margin_Pct = Profit_INR / Net_Sales_INR * 100, 
# # # #   handling zero denominators safely. Create Month_Number to preserve calendar order.
# Short_months = {
#     "Jan": 1,
#     "Feb": 2,
#     "Mar": 3,
#     "Apr": 4,
#     "May": 5,
#     "Jun": 6,
#     "Jul": 7,
#     "Aug": 8,
#     "Sep": 9,
#     "Oct": 10,
#     "Nov": 11,
#     "Dec": 12,
# }
# print("=================================================")
# print("----------------Feature engineering ---------------")
# print("====================Q2=============================")



# Profit_Margin_percentage=df["Profit_INR"]/df["Net_Sales_INR"]*100.
# print("Profit_Margin_percentage  =  ",Profit_Margin_percentage)

# df["Month_Number"] = pd.to_datetime(df["Month"], format="%b").dt.month
# print(df["Month_Number"])
# print("===================Q2==============================")


# # # Q3 — KPI summary
# # # Calculate business KPIs
# # #  Calculate total Net Sales, total Profit, total Orders, total Units, average Order Value, 
# # # average Customer Rating, and Return Rate. Show a neat Pandas summary.
# print("=================================================")
# print("----------------KPI summary----------------------")
# print("====================Q3=============================")

# Total_Net_sales =df["Net_Sales_INR"].sum()
# print("Total_Net_sales  =  ",Total_Net_sales)

# Total_profit = df["Profit_INR"].sum()
# print("Total_profit  =  ",Total_profit)

# Total_orders=df["Order_ID"].nunique()
# print("Total_orders  =  ",Total_orders)

# total_Units=df["Units"].sum()
# print("total_Units  =  ",total_Units)

# average_order=df["Units"].mean()
# print("average_order  =  ",average_order)

# Average_customer_rating=df["Customer_Rating"].mean()
# print(" Average_customer_rating  =  ",Average_customer_rating)

# Total_return=df["Returned"].count()
# print("Total_return  =  ",Total_return)

# Return_Rate=(Total_return)/(Total_orders)*100
# print("Return_Rate  =  ",Return_Rate)

# print("====================Q3=============================")

# # Q4 — Monthly trend
# # Analyze monthly sales and profit
# # Group by month and calculate Net_Sales_INR and Profit_INR totals. Plot sales and profit
# # as two lines in one chart or separate subplots. Add title, labels, markers, colors, grid, and legend.
# print("===============Q4===================")
# month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# Total = ["2L", "7L", "12L", "17L", "22L", "27L", "32L", "37L", "42L", "47L","50L"]


# Sales_inr=df.groupby("Month_Number")["Net_Sales_INR"].sum()



# Profit_inr=df.groupby("Month_Number")["Profit_INR"].sum()
# print(Profit_inr)

# print("===============Q4===================")

# # #Q5 — Product analysis
# # #Find best-selling products
# # #Group by Product and calculate total net sales, profit, units sold, and average rating. Sort by net sales descending. 
# # # Plot top 8 products in a bar chart. Use plt.text() to show values above bars.

# print("===============Q5===================")

# b= df.groupby("Product").agg({
#     "Net_Sales_INR": "sum",
#     "Profit_INR": "sum",
#     "Units": "sum",
#     "Customer_Rating": "mean"
# })
# print(b)

# top_8=b.sort_values("Product",ascending=False)
# print(top_8)


# print("===============Q5===================")

# # Q6 — City performance
# # Compare city performance
# # Group by City and calculate net sales, profit, order count, and average rating. 
# # Sort cities by net sales. Create a horizontal bar chart and set suitable axis limits and ticks.

# print("===============Q6===================")
# Calculated_net_sales=df.groupby("City")["Net_Sales_INR"].sum()
# print(Calculated_net_sales)
# calculated_Profit=df.groupby("City")["Profit_INR"].sum()
# print(calculated_Profit)
# Calculated_Order_count=df.groupby("City")["Order_ID"].count()
# print(Calculated_Order_count)
# calculated_Rating=df.groupby("City")["Customer_Rating"].mean()
# print(calculated_Rating)
# sorted_city=Calculated_net_sales.sort_values(ascending=True)
# print(sorted_city)
# print("===============Q6===================")


# # Q7 — Category contribution
# # Analyze category revenue share
# # Calculate each Category's share of total Net Sales. Create a pie chart with labels
# #  autopct='%1.1f%%', distinct colors, and startangle=90. 
# # Change individual category label colors using the texts returned by plt.pie().

# Category_type=df.groupby("Category")["Net_Sales_INR"].sum()
# print(Category_type)
# print("===============Q7===================")



# # Q8 — Sales channel analysis
# # Compare sales channels
# # Compare total net sales and order counts across Sales_Channel. Identify the best channel using Pandas.
# # Plot a bar chart with title, labels, colors, grid, and legend.
# print("===============Q8===================")

# Total_net_sales=df.groupby("Sales_Channel")["Net_Sales_INR"].sum()
# print("=========================================================================================",Total_net_sales)
# Total_order_count=df.groupby("Sales_Channel")["Order_ID"].count()
# print(Total_order_count)
# Q9 — Customer ratings
# Understand customer satisfaction
# Calculate rating counts and average rating by Product and by City. 
# Create a histogram of Customer_Rating using bins=5. Explain the overall rating distribution.
print("===============Q8===================")

Calculate_rating_counts=df["Customer_Rating"].count()
print(Calculate_rating_counts)
calculate_average_rating=df.groupby(["Product","City"])["Customer_Rating"].mean()
print(calculate_average_rating.head(100))

print("===============Q9===================")



# # Q10 — Discount and profit
# # Investigate discounts
# # Group by Discount_Rate and calculate total net sales, total profit, and average profit margin. 
# # Identify the discount level with the highest total profit. Present findings using a bar chart.
# print("===============Q10===================")

# Discount_Rate_Calculation=df.groupby("Discount_Rate").agg({
#     "Profit_INR":"sum",
#     "Net_Sales_INR":"sum",
#    # "Profit_INR":"mean"
# })

# print(Discount_Rate_Calculation)
# print("===============Q10===================")

# # Q11 — Returns analysis
# # Study returned orders
# # Compare returned vs non-returned orders. Calculate order counts and net sales by Returned status.
# # Calculate return rate by Product and identify products with the highest return rates.
# print("===============Q11===================")
# compare_not_returned=df["Returned"]=="No"
# print(compare_not_returned.sum())

# compare_returned=df["Returned"]=="Yes"
# c=compare_not_returned.sum()
# print(c)

# Calculate_order=df.groupby("Returned")["Order_ID"].count()
# Calculate_Net_sales=df.groupby("Returned")["Net_Sales_INR"].sum()
# print(Calculate_order)
# print(Calculate_Net_sales)

# Return_product=df.groupby(["Returned","Product"])["Returned"].count()

# print(Return_product)
# Return_rate=c/Total_orders*100
# print(Return_rate,"%")

# print(Return_product.max())
# print("===============Q11===================")

# # Q12 — Shipping analysis
# # Analyze shipping performance
# # Calculate average Shipping_Days by City and Sales_Channel. Identify the slowest 
# # city and channel. Create a bar chart of average shipping days by city.

  
# print("==============Q12=====================")
# Average_shiping_days=df.groupby("City")["Shipping_Days"].mean()
# print(Average_shiping_days,"Shiping_days ")

# slowest_city_channels=df.groupby(["City","Sales_Channel"])["Shipping_Days"].mean()
# print(slowest_city_channels)
# slowest=slowest_city_channels.idxmin()
# print(slowest)

# print(" ===============Q12 =================")

# # Q13 — Relationship analysis
# # Study units, sales, and ratings
# # Create a scatter plot with Units on X-axis and Net_Sales_INR on Y-axis. Discuss the relationship.
# # Calculate a Pandas correlation matrix for Units, Unit_Price_INR, Net_Sales_INR, Profit_INR, Customer_Rating, and Shipping_Days.

# correlation_columns = [
#     "Units", 
#     "Unit_Price_INR", 
#     "Net_Sales_INR", 
#     "Profit_INR", 
#     "Customer_Rating", 
#     "Shipping_Days"
# ]

# scat=df.groupby("Units")["Net_Sales_INR"].sum()
# print(scat)
# corr_matrix = df[correlation_columns].corr()
# print(corr_matrix)


# # Q14 — Multi-chart dashboard
# # Build a subplot dashboard
# # Create one figure with 4 subplots (2 rows × 2 columns): (1) monthly net sales line plot, (2) top 8 products bar chart,
# # (3) customer rating histogram, (4) category revenue-share pie chart. Give each subplot a title and suitable labels.
# # Use figsize, plt.tight_layout(), and save as retail_dashboard.png with dpi=300.


# # Q15 — Final conclusion
# # Write business recommendations
# # Write 5 evidence-based findings, including best product, best city, best sales channel, 
# # return-rate concern, and one recommendation to improve sales or customer satisfaction.

