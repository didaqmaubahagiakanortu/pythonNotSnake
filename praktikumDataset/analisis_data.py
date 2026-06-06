# Persiapan Library dan Data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data_praktikum_analisis_data.csv')
print(df.head())

# Inspeksi dan Pembersihan Data

df.info()
df.isnull().sum()
df = df[df['Price_Per_Unit'] > 0]
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Analisis dan Visualisasi

df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.show()

correlation = df[['Total_Sales', 'Ad_Budget']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Peta Korelasi Antar Variabel')
plt.show()

# Identifikasi Produk "Underperformer"

plt.scatter(df['Price_Per_Unit'], df['Quantity'], marker='o', color='b')
plt.show()

# Analisis Kontribusi Kategori

ad_budget_per_category = df.groupby('Product_Category')['Ad_Budget'].sum().sort_values(ascending=False)
plt.barh(ad_budget_per_category.index, ad_budget_per_category.values, color='b')
plt.title('Analisis Efisiensi Kategori Produk')
plt.show()

# Uji Hipotesis Sederhana

median = df['Ad_Budget'].median()
high_ad = df[df['Ad_Budget'] > median]
low_ad = df[df['Ad_Budget'] < median]

plt.bar(['Iklan Tinggi', 'Iklan Rendah'], [high_ad['Total_Sales'].mean(), low_ad['Total_Sales'].mean()])
plt.title('Perbandingan Rata-Rata Penjualan Berdasarkan Iklan')
plt.show()

# Pendalaman Teknik: RFM Analysis

import datetime as dt

snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

rfm['RFM_Group'] = rfm.R_Score.astype(str) + rfm.F_Score.astype(str) + rfm.M_Score.astype(str)
print(rfm)

# Pendalaman Teknik: Regresi Linear Sederhana

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df[df['Ad_Budget'].notna()]
y = df[df['Total_Sales'].notna()]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Koefisien Iklan: {model.coef_[0]}")
print(f"Akurasi Model (R2 Score): {model.score(X_test, y_test)}")