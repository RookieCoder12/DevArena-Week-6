from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd 
import plotly.express as pex

#--- Completed Sales 
df = pd.read_csv(r"/Users/developer/Documents/Current Project/Python/DevArena /DevArena-Week-6/data/amazon_final.csv")

#--- Monthly Sales
df_monthly_sales = df.groupby("Month").agg(
    monthly_revenue = ("Amount", "sum"), 
    no_orders = ("Order ID", "nunique")
).reset_index().sort_values("Month")
# Create a line plot object
fig_monthly_sales_line = pex.line(df_monthly_sales, x="Month", y="monthly_revenue", title="Monthly Revenue", markers=True)
fig_monthly_orders_line = pex.line(df_monthly_sales, x="Month", y="no_orders", title="Monthly Orders", markers=True)

#--- Category Sales
df_category_sales = df.groupby(["Month", "Category"]).agg(
    monthly_revenue = ("Amount", "sum"), 
    no_orders = ("Order ID", "nunique")
)
categories = df["Category"].unique().tolist()

#--- State Sales
df_state_sales = df.groupby(["ship-state", "Category"]).agg(
    revenue = ("Amount", "sum")
)

#--- Not Completed Sales
not_df = pd.read_csv(r"/Users/developer/Documents/Current Project/Python/DevArena /DevArena-Week-6/data/notamazon_final.csv")

not_df_aggregated = not_df.groupby("Status").agg(
    no_orders = ("Order ID", "nunique")
).reset_index()
#--- Creating a bar graph objects
fig_monthly_orders_not_completed = pex.bar(data_frame=not_df_aggregated
                  , x="Status"
                  , y="no_orders")

app = Dash()

app.layout = html.Div([
    #--- Title & Data
    html.Div([
        html.H1("Amazon Sales Dashboard")
    ], style={"textAlign": "center"}) ,

    #--- Monthly Sales
    html.Div([
        html.Div([
            dcc.Graph(figure=fig_monthly_sales_line)
        ], style={"width": "50%"
                  , "display": "inline-block"
                  } ) ,

        html.Div([
            dcc.Graph(figure=fig_monthly_orders_line)
        ], style={"width": "50%", "display": "inline-block"})
    ], style={"display": "flex" 
              , "alignItems": "center" 
              , "width": "90%" 
              , "margin": "0 auto"
              } ) ,

    #--- Category Sales
    html.Div([
        html.Div([
            dcc.RadioItems(options=[ {'label' : c.title(), 'value' : c} for c in categories] ,
                           value = categories[0] ,
                           inline = False ,
                           id = 'category_radio_button')
        ], style={"width": "5%", "display": "inline-block"}),

        html.Div([
            dcc.Graph(id='category_line_chart_monthlyRev')
        ], style={"width": "47%", "display": "inline-block"}) ,

        html.Div([
            dcc.Graph(id='category_line_chart_monthlyOrders')
        ], style={"width": "47%", "display": "inline-block"})
    ], style={"display": "flex" 
              , "alignItems": "center" 
              , "width": "90%" 
              , "margin": "0 auto"
              } ) ,

    #--- State Sales
    html.Div([
        dcc.Graph(id='state_sales_bar_chart')
    ], style={"alignItems": "center" 
              , "width": "90%" 
              , "margin": "0 auto"
              } ) ,

    #--- Cancelled Orders
    html.Div([
        dcc.Graph(figure=fig_monthly_orders_not_completed)
    ], style={"alignItems": "center" 
              , "width": "90%" 
              , "margin": "0 auto"
              } )
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

# 'state_sales_bar_chart'
@callback(
    Output('state_sales_bar_chart', 'figure') ,
    Input('category_radio_button', 'value')
)
def category_chart_noOrders(selected_category):
    df_filtered_state = df_state_sales.xs(selected_category, level="Category").reset_index().head(15).sort_values(by="revenue", ascending=False)
    # Create a line plot object
    fig = pex.bar(data_frame= df_filtered_state, 
                   x="ship-state" ,
                   y="revenue" ,
                   title= f"Top State Sales")

    return fig

if __name__ == '__main__':
    app.run(debug=True)