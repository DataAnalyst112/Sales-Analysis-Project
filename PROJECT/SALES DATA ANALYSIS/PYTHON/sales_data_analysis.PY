import pandas as pd
import matplotlib.pyplot as plt

# load dataset
data=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\PROJECT\SALES DATA ANALYSIS\EXCEL\sales.csv")

# create revenue column
data["Revenue"]=data["Price"]*data["Quantity"]

#create total revenue
data["Total Revenue"]=data["Revenue"].sum()

#create revenue by product
product_sales=data.groupby("Product")["Revenue"].sum()
print(product_sales)

#create revenue by region
region_sales=data.groupby("Region")["Revenue"].sum()
print(region_sales)

#plot graph of revenue by product
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.show()

#plot graph of revenue by region
region_sales.plot(kind="pie",autopct="%1.1f%%")
plt.title("Revenue by Region")
plt.show()