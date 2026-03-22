# DevArena-Week-6

## Overview
This project develops an interactive sales **analytics dashboard using Python** and the **Dash framework** to **analyze Amazon sales data**. The primary objective is to explore **revenue trends**, **order patterns**, and **regional performance**, while also examining **incomplete or cancelled orders** to provide a comprehensive view of business operations.
During the preprocessing stage, the datasets were cleaned and prepared for analysis. Monthly trends for sales, number of orders, and quantity sold were examined to understand overall business performance. In addition, product category sales trends and regional performance were analyzed to identify fluctuations in revenue.
The dashboard incorporates multiple interactive visualizations built with **Plotly**. These include monthly revenue and order trend line charts, category-wise performance analysis using dynamic filters, and state-level revenue comparisons through bar charts. A **radio button selector** allows users to **interactively explore different product categories, updating the visualizations in real time**.
The project also analyzes non-completed orders by examining order statuses and visualizing their distribution, helping identify operational inefficiencies or fulfillment issues.
Overall, this project demonstrates the integration of data preprocessing, aggregation, and interactive visualization techniques to build a dynamic dashboard that supports business insights and decision-making.


## Files
- data/
    - `Amazon Sales Report.csv` - <b>CSV file</b> that contains the data we analysed for insights and recommendation in this project.

- visualizations/
    - `amount_box.gif` - <b>Interactive Boxplot chart</b> showing the <b>distribution of values of Amount for different months.</b>.
    - `amount_values_box.png` - <b>Boxplot chart</b> showing the <b>distribution of values of Amount for different months.</b>.
    - `amount_values_violin.png` - <b>Violin chart</b> showing the <b>distribution of values of Amount for different months.</b>.
    - `amount_violin.gif` - <b>Interactive Violin chart</b> showing the <b>distribution of values of Amount for different months.</b>.
    - `cancelled_orders_bar.png` - <b>Bar chart</b> displaying the <b>cancelled prders in different courier status.</b>.
    - `categories_sales_trend.png` - <b>Line chart</b> displaying the <b>sales trend for different product category</b>.

- `dashboard_demo.gif` - <b>GIF File</b> showing the <b>working of the interactive dashboard</b> containing different interactive visualizations picturising the insights generated from the data

- `dashboard.ipynb` - Main <b>Python Notebook</b> showing the <b>exploratory data analysis</b> done on the data and different visualizations picturising the insights generated from the data.

- `dashboard.py` - <b>Python script</b> contains code for the dashboard.

- `README.md` - This file.

- `requirements.txt` - Consist of <b>Python libraries</b> required for this project.


## Getting Started

### Prerequisites
Ensure you have Python 3.x installed on your system.

### Cloning Repository
Cloning the repository:
```zsh
git clone https://github.com/RookieCoder12/DevArena-Week-6.git
```

### Installation
Install the required dependencies:
```zsh
pip install -r requirements.txt
```

### Running the Project

#### Running the Python Notebook
1. Run jupyter notebook:
```zsh
jupyter notebook
```
2. Open ```dashboaard.ipynb```

#### Running the Python Script
1. Run Python file:
```zsh
python dashboard.py
```

## Structure
In this project, an interactive **data analytics dashboard** was developed using **Python** and the **Dash framework** to perform Exploratory Data Analysis (EDA) on Amazon sales data and generate **actionable business insights**.

During the preprocessing phase, the datasets were **cleaned and aggregated** to support efficient analysis. The sales data was structured to evaluate **monthly revenue trends** and **number of orders**, enabling a clear understanding of **overall business performance** over time.

The dashboard includes analysis of **monthly sales trends**, where line charts were used to visualize fluctuations in revenue and order volume across different months. This helped identify patterns in demand and overall platform performance.

Further analysis was conducted on product categories, where users can dynamically select a category using an interactive radio button. Based on the selection, the dashboard updates to display category-wise monthly revenue and order trends, allowing deeper insight into product-level performance and demand variations.

A **regional (state-level) analysis** was also implemented to **examine revenue distribution** across different locations. The dashboard highlights the **top-performing states by revenue**, helping identify key geographical markets contributing to sales.

In addition to completed sales, the dashboard analyzes non-completed (cancelled or failed) orders by visualizing order counts across different statuses. This provides visibility into operational inefficiencies and potential fulfillment issues.

Overall, this dashboard integrates **data preprocessing, aggregation**, and **interactive visualization** to **enable real-time exploration of sales data**. The insights derived from this analysis can support better decision-making in areas such as product strategy, regional targeting, and operational efficiency.