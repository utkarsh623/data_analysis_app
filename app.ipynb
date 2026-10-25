import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(page_title="Data Analysis Dashboard", layout="wide")

@st.cache_data
def load_data(uploaded_file):
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            df = pd.read_json(uploaded_file)
        else:
            st.error("Unsupported file format.")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def preprocess_data(df):
    df = df.drop_duplicates()
    
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    df[cat_cols] = df[cat_cols].fillna("Unknown")
    
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        
    return df

def get_column_mapping(df, expected_terms):
    cols = df.columns.str.lower()
    for term in expected_terms:
        for col in df.columns:
            if term in col.lower():
                return col
    return None

st.title("📊 Interactive Data Analysis & KPI Dashboard")
st.markdown("""
Upload your dataset to validate, preprocess, and visualize your data. 
*(You can test this application using your `experiment10_raw_dataset.csv` file).*
""")

uploaded_file = st.file_uploader("Upload CSV, Excel, or JSON", type=['csv', 'xlsx', 'xls', 'json'])

if uploaded_file is not None:
    df_raw = load_data(uploaded_file)
    
    if df_raw is not None:
        st.header("1. Data Validation & Overview")
        with st.expander("View Raw Data Validation Info", expanded=False):
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Rows", df_raw.shape[0])
            col2.metric("Total Columns", df_raw.shape[1])
            col3.metric("Duplicate Records", df_raw.duplicated().sum())
            
            st.write("**Column Names and Data Types:**")
            st.dataframe(df_raw.dtypes.astype(str).reset_index().rename(columns={'index': 'Column', 0: 'Data Type'}))
            
            st.write("**Missing Values per Column:**")
            st.dataframe(df_raw.isnull().sum().reset_index().rename(columns={'index': 'Column', 0: 'Missing Values'}))

        df_clean = preprocess_data(df_raw)
        
        st.header("2. Interactive Filters")
        
        cat_columns = df_clean.select_dtypes(include=['object']).columns.tolist()
        
        col_f1, col_f2, col_f3 = st.columns(3)
        if len(cat_columns) >= 3:
            filter_1_col = cat_columns[0]
            filter_2_col = cat_columns[1]
            filter_3_col = cat_columns[2]
            
            f1_val = col_f1.multiselect(f"Filter by {filter_1_col}", options=df_clean[filter_1_col].unique(), default=df_clean[filter_1_col].unique())
            f2_val = col_f2.multiselect(f"Filter by {filter_2_col}", options=df_clean[filter_2_col].unique(), default=df_clean[filter_2_col].unique())
            f3_val = col_f3.multiselect(f"Filter by {filter_3_col}", options=df_clean[filter_3_col].unique(), default=df_clean[filter_3_col].unique())
            
            df_filtered = df_clean[
                (df_clean[filter_1_col].isin(f1_val)) & 
                (df_clean[filter_2_col].isin(f2_val)) & 
                (df_clean[filter_3_col].isin(f3_val))
            ]
        else:
            st.info("Not enough categorical columns to apply 3 distinct filters. Displaying unfiltered data.")
            df_filtered = df_clean.copy()

        st.header("3. Key Performance Indicators (KPIs)")
        
        sales_col = get_column_mapping(df_filtered, ['sales', 'revenue', 'amount'])
        profit_col = get_column_mapping(df_filtered, ['profit', 'margin'])
        order_col = get_column_mapping(df_filtered, ['order id', 'transaction id', 'id'])
        qty_col = get_column_mapping(df_filtered, ['quantity', 'qty', 'units'])

        if sales_col and profit_col and order_col and qty_col:
            total_sales = df_filtered[sales_col].sum()
            total_profit = df_filtered[profit_col].sum()
            total_orders = df_filtered[order_col].nunique()
            total_quantity = df_filtered[qty_col].sum()
            profit_margin = (total_profit / total_sales * 100) if total_sales != 0 else 0
            
            kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
            kpi1.metric("Total Sales", f"${total_sales:,.2f}")
            kpi2.metric("Total Profit", f"${total_profit:,.2f}")
            kpi3.metric("Total Orders", f"{total_orders:,}")
            kpi4.metric("Total Quantity", f"{total_quantity:,}")
            kpi5.metric("Profit Margin (%)", f"{profit_margin:.2f}%")
            
            st.header("4. Interactive Visualizations")
            
            chart_col1, chart_col2 = st.columns(2)
            
            with chart_col1:
                st.subheader("Sales vs Profit")
                fig1 = px.scatter(df_filtered, x=sales_col, y=profit_col, color=filter_1_col if len(cat_columns)>0 else None, 
                                  title="Profitability per Sale")
                st.plotly_chart(fig1, use_container_width=True)
            
            with chart_col2:
                if len(cat_columns) > 0:
                    st.subheader(f"Quantity by {cat_columns[0]}")
                    qty_by_cat = df_filtered.groupby(cat_columns[0])[qty_col].sum().reset_index()
                    fig2 = px.bar(qty_by_cat, x=cat_columns[0], y=qty_col, color=cat_columns[0],
                                  title=f"Total Quantity Sold by {cat_columns[0]}")
                    st.plotly_chart(fig2, use_container_width=True)
                
            date_cols = df_filtered.select_dtypes(include=['datetime64']).columns
            if len(date_cols) > 0:
                st.subheader(f"Sales Trend over Time")
                trend_data = df_filtered.groupby(df_filtered[date_cols[0]].dt.to_period("M"))[sales_col].sum().reset_index()
                trend_data[date_cols[0]] = trend_data[date_cols[0]].astype(str)
                fig3 = px.line(trend_data, x=date_cols[0], y=sales_col, title="Monthly Sales Trend")
                st.plotly_chart(fig3, use_container_width=True)
            else:
                st.info("No datetime column found to plot a time-series chart.")
                
            st.subheader("Statistical Summaries")
            st.dataframe(df_filtered[[sales_col, profit_col, qty_col]].describe())

        else:
            st.error("Could not automatically identify 'Sales', 'Profit', 'Order ID', or 'Quantity' columns in the dataset to calculate required KPIs. Please ensure your columns are named appropriately.")
else:
    st.info("Please upload a file to proceed.")
