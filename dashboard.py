from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd 
import plotly.express as pex

df = pd.read_csv(r"/Users/developer/Documents/Current Project/Python/DevArena /DevArena-Week-6/data/amazon_final.csv")

# Monthly Sales
df_monthly_sales = df.groupby("Month").agg(
    monthly_revenue = ("Amount", "sum"), 
    no_orders = ("Order ID", "nunique")
).reset_index().sort_values("Month")
# Create a line plot object
fig_monthly_sales_line = pex.line(df_monthly_sales, x="Month", y="monthly_revenue", title="Monthly Revenue", markers=True)
fig_monthly_orders_line = pex.line(df_monthly_sales, x="Month", y="no_orders", title="Monthly Orders", markers=True)

# Category Sales
df_category_sales = df.groupby(["Month", "Category"]).agg(
    monthly_revenue = ("Amount", "sum"), 
    no_orders = ("Order ID", "nunique")
)
categories = df["Category"].unique().tolist()
# print(categories)

app = Dash()

app.layout = html.Div([
    #--- Title & Data
    html.Div([
        html.H1("This is where it starts")
    ], style={"textAlign": "center"}) ,
    
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    ),

    #--- Monthly Sales
    html.Div([
        html.Div([
            dag.AgGrid(
                rowData=df_monthly_sales.to_dict('records'),
                columnDefs=[{"field": i} for i in df_monthly_sales.columns]
            )
        ], style={"width": "33%", "display": "inline-block"}),

        html.Div([
            dcc.Graph(figure=fig_monthly_sales_line)
        ], style={"width": "35%", "display": "inline-block"}) ,

        html.Div([
            dcc.Graph(figure=fig_monthly_orders_line)
        ], style={"width": "33%", "display": "inline-block"})
    ], style={"display": "flex"}) ,

    #--- Category Sales
    html.Div([
        html.Div([
            dcc.RadioItems(options=[ {'label' : c.title(), 'value' : c} for c in categories] ,
                           value = categories[0] ,
                           inline = False ,
                           id = 'category_radio_button')
        ], style={"width": "33%", "display": "inline-block"}),

        html.Div([
            dcc.Graph(id='category_line_chart_monthlyRev')
        ], style={"width": "35%", "display": "inline-block"}) ,

        html.Div([
            dcc.Graph(id='category_line_chart_monthlyOrders')
        ], style={"width": "33%", "display": "inline-block"})
    ], style={"display": "flex"})

    
])

# 'category_line_chart_monthlyRev'
@callback(
    Output('category_line_chart_monthlyRev', 'figure') ,
    Input('category_radio_button', 'value')
)
# Chart function
def update_category_chart(selected_category):
    # Filter Data
    df_filtered_category = df_category_sales.xs(selected_category, level="Category").reset_index()
    # Create a line plot object
    fig = pex.line(data_frame= df_filtered_category, 
                   x="Month" ,
                   y="monthly_revenue" ,
                   markers= True ,
                   title= f"{selected_category.title()} - Monthly Sales Trend")

    return fig

# 'category_line_chart_monthlyOrders'
@callback(
    Output('category_line_chart_monthlyOrders', 'figure') ,
    Input('category_radio_button', 'value')
)
# chart function
def category_chart_noOrders(selected_category):
    df_filtered_category = df_category_sales.xs(selected_category, level="Category").reset_index()
    # Create a line plot object
    fig = pex.line(data_frame= df_filtered_category, 
                   x="Month" ,
                   y="no_orders" ,
                   markers= True ,
                   title= f"{selected_category.title()} - Monthly Orders Trend")

    return fig
    
if __name__ == '__main__':
    app.run(debug=True)