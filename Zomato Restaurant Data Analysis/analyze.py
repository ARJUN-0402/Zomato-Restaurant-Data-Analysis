import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load Dataset
data = pd.read_csv("zomato.csv", encoding='latin-1')
print(data.head())

# Step 2: Data Cleaning
data.drop_duplicates(inplace=True)
data.fillna(method='ffill', inplace=True)

# Handle data types
data['Average Cost for two'] = pd.to_numeric(data['Average Cost for two'], errors='coerce')
data['Aggregate rating'] = pd.to_numeric(data['Aggregate rating'], errors='coerce')

# Deal with missing or inconsistent cuisine names
data['Cuisines'] = data['Cuisines'].str.split(',').str[0]

print("Data cleaned successfully")

# Step 3: Exploratory Data Analysis (EDA)

# Top Cities by Number of Restaurants
top_cities = data['City'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette='viridis')
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.savefig('top_cities.png', bbox_inches='tight')
plt.show()

# Popular Cuisines
top_cuisines = data['Cuisines'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette='viridis')
plt.title("Top 10 Cuisines")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine")
plt.savefig('top_cuisines.png', bbox_inches='tight')
plt.show()

# Average Rating vs. Cost
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Average Cost for two', y='Aggregate rating', data=data)
plt.title("Cost vs Rating")
plt.savefig('cost_vs_rating.png', bbox_inches='tight')
plt.show()

# Step 4: Insights

# City with most expensive restaurants
city_cost = data.groupby('City')['Average Cost for two'].mean().sort_values(ascending=False).head(10)
print("\nTop 10 Cities with Most Expensive Restaurants:")
print(city_cost)

# Best-rated cuisine
cuisine_rating = data.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
print("\nTop 10 Best-rated Cuisines:")
print(cuisine_rating)

# Correlation between cost and rating
correlation = data[['Average Cost for two', 'Aggregate rating']].corr()
print("\nCorrelation between Cost and Rating:")
print(correlation)

# Summary Report
print("\nSummary:")
print("Most restaurants are in:", top_cities.idxmax())
print("Most popular cuisine:", top_cuisines.idxmax())
print("Highest rated cuisine:", cuisine_rating.idxmax())