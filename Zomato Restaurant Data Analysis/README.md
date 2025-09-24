# Zomato Restaurant Data Analysis

## 1. Project Overview

This project analyzes restaurant data from Zomato to gain insights into the restaurant industry. The analysis focuses on:

*   Popular cuisines in different cities
*   Top-rated restaurants
*   Price trends
*   City-wise restaurant density

The project demonstrates skills in Python, Pandas, Matplotlib/Seaborn for data cleaning, data visualization, and exploratory data analysis (EDA).

## 2. Dataset

The dataset used in this project is `zomato.csv`. It contains information about restaurants, including:

*   Restaurant Name
*   City
*   Cuisines
*   Average Cost for Two
*   Aggregate Rating
*   Votes

## 3. Python Libraries Required

The following Python libraries are used in this project:

*   `pandas`
*   `numpy`
*   `matplotlib`
*   `seaborn`

You can install these libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn
```

## 4. Steps to Build the Project

### Step 1: Load Dataset

The dataset is loaded into a pandas DataFrame from the `zomato.csv` file.

### Step 2: Data Cleaning

The following data cleaning steps are performed:

*   **Remove duplicates:** Duplicate rows are removed from the dataset.
*   **Handle missing values:** Missing values are filled using the forward fill method (`ffill`).
*   **Convert text columns to lowercase:** Text columns are converted to lowercase for consistency (this step was not explicitly implemented in the script but is a good practice).

### Step 3: Exploratory Data Analysis (EDA)

The following EDA is performed to understand the data:

*   **Top Cities by Number of Restaurants:** A bar plot is created to visualize the top 10 cities with the highest number of restaurants.
*   **Popular Cuisines:** A bar plot is created to visualize the top 10 most popular cuisines.
*   **Average Rating vs. Cost:** A scatter plot is created to visualize the relationship between the average cost for two people and the aggregate rating.

### Step 4: Insights

The following insights are extracted from the analysis:

*   **City with most expensive restaurants:** The top 10 cities with the highest average cost for two people are identified.
*   **Best-rated cuisine:** The top 10 cuisines with the highest average aggregate rating are identified.
*   **Correlation between cost and rating:** The correlation between the average cost for two people and the aggregate rating is calculated.

## 5. How to Run the Analysis

To run the analysis, execute the `analyze.py` script:

```bash
python analyze.py
```

The script will print the data head, a success message for data cleaning, and the insights to the console. The plots will be displayed in separate windows.

## 6. Optional Enhancements

The following enhancements can be made to the project:

*   Use Plotly for interactive visualizations.
*   Build a dashboard using Streamlit or Dash.
*   Predict restaurant ratings using machine learning models.
