import pandas as pd
import sqlite3


# ----------------------
# EXTRACT
# ----------------------
def extract():
    print("Extracting data...")
    df = pd.read_csv("data/sales_data.csv")

    print("Columns in CSV")
    print(df.columns)

    return df


# ----------------------
# TRANSFORM
# ----------------------
def transform(df):
    print("Transforming data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    # Create new column (example)
    df["total_Sales"] = df["quantity"] * df["price"]
    
    # Convert order_date to proper date format
    df["order_date"] = pd.to_datetime(df["order_date"])

    #Add Business Transformation(Monthly analysis)
    df["month"] = df["order_date"].dt.month

    return df


# ----------------------
# LOAD
# ----------------------
def load(df):
    print("Loading data into SQLite database...")

    conn = sqlite3.connect("sales_database.db")

    df.to_sql("sales", conn, if_exists="replace", index=False)

    conn.close()

    print("Data successfully loaded!")

# SQL Analytics 

def run_analytics():
    conn = sqlite3.connect("sales_database.db")
    cursor = conn.cursor()

    print("\n--- Total Revenue ---")
    cursor.execute("SELECT SUM(total_sales) FROM sales;")
    print(cursor.fetchone())

    print("\n--- Revenue by Region ---")
    cursor.execute("""
        SELECT region, SUM(total_sales)
        FROM sales
        GROUP BY region;
    """)
    for row in cursor.fetchall():
        print(row)

    print("\n--- Top 5 Products by Revenue ---")
    cursor.execute("""
        SELECT Product, SUM(total_sales) as revenue
        FROM sales
        GROUP BY Product
        ORDER BY revenue DESC
        LIMIT 5;
    """)
    for row in cursor.fetchall():
        print(row)

    conn.close()

# ----------------------
# MAIN PIPELINE
# ----------------------
def run_pipeline():
    df = extract()
    df = transform(df)
    load(df)
    run_analytics() 
    

if __name__ == "__main__":
    run_pipeline()