import os
import logging

import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

from dotenv import load_dotenv


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)


# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

load_dotenv(
    os.path.join(BASE_DIR, ".env")
)

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DATABASE = os.getenv("PG_DATABASE")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "analyse.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logging.info("========== ANALYSIS START ==========")


try:

    print("\n======================================")
    print("       DATA ENGINEERING ANALYSIS")
    print("======================================")


    # ========================================================
    # 1. POSTGRESQL CONNECTION
    # ========================================================

    print("\n1. Connecting to PostgreSQL...")

    conn = psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        database=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD
    )

    logging.info("PostgreSQL connection successful")

    print("PostgreSQL connection successful.")


    # ========================================================
    # 2. EXTRACT DATA
    # ========================================================

    print("\n2. Extracting data...")

    query = """
        SELECT *
        FROM sales_analysis;
    """

    df = pd.read_sql(
        query,
        conn
    )

    conn.close()

    print("\n========== DATA ==========")
    print(df)


    # ========================================================
    # 3. DATA INFORMATION
    # ========================================================

    print("\n========== DATA INFORMATION ==========")

    df.info()


    # ========================================================
    # 4. DESCRIPTIVE STATISTICS
    # ========================================================

    print("\n========== STATISTICS ==========")

    print(
        df.describe()
    )


    # ========================================================
    # 5. PANDAS CLEANING / TRANSFORMATION
    # ========================================================

    print("\n========== PART 6 : PANDAS ==========")


    # High-value orders

    high_sales = df[
        df["total_amount"] > 500
    ]

    print("\n--- Orders > 500 ---")
    print(high_sales)


    # Morocco + high value

    morocco_high_sales = df[
        (df["total_amount"] > 500)
        &
        (df["country"] == "Morocco")
    ]

    print("\n--- Orders > 500 in Morocco ---")
    print(morocco_high_sales)


    # LOC

    print("\n--- LOC ---")

    print(
        df.loc[
            :,
            [
                "customer",
                "total_amount"
            ]
        ]
    )


    # ILOC

    print("\n--- ILOC ---")

    print(
        df.iloc[:3]
    )


    # Sorting

    print("\n--- Sorted orders ---")

    sorted_sales = df.sort_values(
        "total_amount",
        ascending=False
    )

    print(sorted_sales)


    # New column

    df["high_value"] = (
        df["total_amount"] > 500
    )


    # Dates

    df["order_date"] = pd.to_datetime(
        df["order_date"]
    )

    df["year"] = (
        df["order_date"].dt.year
    )

    df["month"] = (
        df["order_date"].dt.month
    )

    df["day"] = (
        df["order_date"].dt.day
    )


    print("\n--- Missing values ---")

    print(
        df.isna().sum()
    )


    print("\n--- Duplicates ---")

    print(
        df.duplicated().sum()
    )


    print("\n--- Data types ---")

    print(
        df.dtypes
    )


    # ========================================================
    # 6. BUSINESS ANALYSIS
    # ========================================================

    print("\n========== PART 7 : DATA ANALYSIS ==========")


    # KPI

    total_sales = (
        df["total_amount"].sum()
    )

    total_orders = (
        df["order_id"].nunique()
    )

    total_units = (
        df["quantity"].sum()
    )

    average_order = (
        df["total_amount"].mean()
    )


    print("\n--- KPI ---")

    print(
        f"Total revenue : {total_sales:.2f}"
    )

    print(
        f"Total orders : {total_orders}"
    )

    print(
        f"Units sold : {total_units}"
    )

    print(
        f"Average order : {average_order:.2f}"
    )


    # ========================================================
    # PRODUCT ANALYSIS
    # ========================================================

    sales_by_product = (
        df.groupby("product_name")
        .agg(
            orders=("order_id", "count"),
            units_sold=("quantity", "sum"),
            revenue=("total_amount", "sum")
        )
        .sort_values(
            "revenue",
            ascending=False
        )
    )

    print("\n--- Sales by product ---")
    print(sales_by_product)


    best_product = (
        sales_by_product["revenue"]
        .idxmax()
    )

    best_selling_product = (
        sales_by_product["units_sold"]
        .idxmax()
    )


    # ========================================================
    # CUSTOMER ANALYSIS
    # ========================================================

    sales_by_customer = (
        df.groupby("customer")
        .agg(
            orders=("order_id", "count"),
            units_sold=("quantity", "sum"),
            total_spent=("total_amount", "sum")
        )
        .sort_values(
            "total_spent",
            ascending=False
        )
    )

    print("\n--- Sales by customer ---")
    print(sales_by_customer)


    best_customer = (
        sales_by_customer["total_spent"]
        .idxmax()
    )


    # ========================================================
    # COUNTRY ANALYSIS
    # ========================================================

    sales_by_country = (
        df.groupby("country")
        .agg(
            orders=("order_id", "count"),
            units_sold=("quantity", "sum"),
            revenue=("total_amount", "sum")
        )
        .sort_values(
            "revenue",
            ascending=False
        )
    )

    print("\n--- Sales by country ---")
    print(sales_by_country)


    # ========================================================
    # CATEGORY ANALYSIS
    # ========================================================

    sales_by_category = (
        df.groupby("category")
        .agg(
            orders=("order_id", "count"),
            units_sold=("quantity", "sum"),
            revenue=("total_amount", "sum")
        )
        .sort_values(
            "revenue",
            ascending=False
        )
    )

    print("\n--- Sales by category ---")
    print(sales_by_category)


    # ========================================================
    # 7. EXPORT CSV
    # ========================================================

    print("\n========== EXPORT CSV ==========")


    sales_by_country.to_csv(
        os.path.join(
            OUTPUT_DIR,
            "sales_by_country.csv"
        )
    )


    sales_by_product.to_csv(
        os.path.join(
            OUTPUT_DIR,
            "sales_by_product.csv"
        )
    )


    sales_by_customer.to_csv(
        os.path.join(
            OUTPUT_DIR,
            "sales_by_customer.csv"
        )
    )


    sales_by_category.to_csv(
        os.path.join(
            OUTPUT_DIR,
            "sales_by_category.csv"
        )
    )


    print(
        "CSV files exported successfully."
    )


    # ========================================================
    # 8. VISUALIZATION
    # ========================================================

    print("\n========== PART 8 : VISUALIZATION ==========")


    # Country

    plt.figure()

    sales_by_country["revenue"].plot(
        kind="bar"
    )

    plt.title(
        "Revenue by Country"
    )

    plt.xlabel("Country")
    plt.ylabel("Revenue")

    plt.tight_layout()

    plt.show()


    # Product

    plt.figure()

    sales_by_product["revenue"].plot(
        kind="bar"
    )

    plt.title(
        "Revenue by Product"
    )

    plt.xlabel("Product")
    plt.ylabel("Revenue")

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.show()


    # Category

    plt.figure()

    sales_by_category["revenue"].plot(
        kind="bar"
    )

    plt.title(
        "Revenue by Category"
    )

    plt.xlabel("Category")
    plt.ylabel("Revenue")

    plt.tight_layout()

    plt.show()


    # Top customers

    top_customers = (
        sales_by_customer.head(5)
    )

    plt.figure()

    top_customers["total_spent"].plot(
        kind="bar"
    )

    plt.title(
        "Top 5 Customers"
    )

    plt.xlabel("Customer")
    plt.ylabel("Total Spent")

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.show()


    # ========================================================
    # 9. FINAL SUMMARY
    # ========================================================

    print("\n======================================")
    print("       FINAL PIPELINE SUMMARY")
    print("======================================")


    print(
        f"Revenue             : {total_sales:.2f}"
    )

    print(
        f"Orders              : {total_orders}"
    )

    print(
        f"Units sold          : {total_units}"
    )

    print(
        f"Average order       : {average_order:.2f}"
    )

    print(
        f"Best product        : {best_product}"
    )

    print(
        f"Most sold product   : {best_selling_product}"
    )

    print(
        f"Best customer       : {best_customer}"
    )

    print(
        f"Best country        : {sales_by_country.index[0]}"
    )

    print(
        f"Best category       : {sales_by_category.index[0]}"
    )


    logging.info(
        "Analysis completed successfully"
    )

    logging.info(
        "========== ANALYSIS END =========="
    )


    print("\n========== ANALYSIS COMPLETED ==========")


except Exception as e:

    logging.error(
        f"ERROR : {e}",
        exc_info=True
    )

    print("\n======================================")
    print("ERROR")
    print("======================================")

    print(e)

    raise