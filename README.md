# E-Commerce Data Engineering Pipeline

An end-to-end data engineering pipeline designed to demonstrate data integration, transformation, analysis and automation using modern data engineering technologies.

This project is designed as a practical portfolio project for Data Engineer, Data Analyst, BI and Analytics Engineering opportunities.

---

## 🎯 Project Objective

The objective is to build a complete e-commerce data pipeline capable of:

- Integrating operational data
- Synchronizing data using Airbyte
- Running infrastructure with Docker
- Storing data in PostgreSQL
- Transforming and analyzing data using SQL
- Extracting analytical datasets with Python
- Performing data analysis with Pandas
- Generating business KPIs
- Exporting analytical datasets to CSV
- Automating the complete workflow
- Producing pipeline execution logs

The project demonstrates an end-to-end workflow from raw operational data to business-ready analytical datasets.

---

# 🏗️ Architecture

```text
                  E-COMMERCE SOURCE DATA
                           │
                           ▼
                    ┌─────────────┐
                    │   Airbyte   │
                    │     ETL     │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ PostgreSQL  │
                    │ Destination │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │     SQL     │
                    │  Analytics  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Python    │
                    │   Pandas    │
                    └──────┬──────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │ Business Analytics  │
                 │       & KPIs        │
                 └──────────┬──────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │  CSV / Reports   │
                   └──────────────────┘
```

Docker is used to provide the infrastructure required by the data platform.

---

# 🛠️ Technologies

## Data Engineering

- Airbyte
- Docker
- PostgreSQL
- SQL

## Data Analysis

- Python
- Pandas
- NumPy
- Matplotlib

## Database Connectivity

- psycopg2
- SQLAlchemy
- python-dotenv

## Development & Version Control

- Visual Studio Code
- Git
- GitHub
- PowerShell

---

# 📂 Project Structure

```text
ecommerce-data-engineering-pipeline/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── pipeline.py
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_insert_data.sql
│   └── 03_analysis.sql
│
├── python/
│   └── analyse.py
│
├── data/
│   └── README.md
│
├── output/
│   ├── sales_by_category.csv
│   ├── sales_by_country.csv
│   ├── sales_by_customer.csv
│   └── sales_by_product.csv
│
└── logs/
    └── README.md
```

---

# 🔄 Pipeline Workflow

## 1. Data Integration

Airbyte is used as the data integration layer to synchronize e-commerce data into the PostgreSQL destination.

The main entities are:

- Customers
- Products
- Orders

## 2. PostgreSQL

PostgreSQL is used as the destination database.

The project contains the following main tables:

- customers
- products
- orders

An analytical SQL view is also created:

- sales_analysis

This view combines customer, product and order information.

## 3. SQL Analytics

SQL is used to calculate:

- Total sales
- Number of orders
- Revenue by product
- Revenue by customer
- Revenue by country
- Revenue by category

## 4. Python Data Analysis

Python extracts the analytical dataset from PostgreSQL.

Pandas is used for:

- Data inspection
- Filtering
- Sorting
- GroupBy operations
- Aggregation
- Missing-value detection
- Duplicate detection
- Date transformation
- KPI calculation

---

# 📊 Business KPIs

Current dataset results:

| KPI | Result |
|---|---:|
| Total Revenue | 3333.00 |
| Total Orders | 7 |
| Units Sold | 11 |
| Average Order Value | 476.14 |

---

# 🏆 Business Results

| Metric | Result |
|---|---|
| Best Product by Revenue | iPhone 15 |
| Most Sold Product | Wireless Mouse |
| Best Customer | Sara Amrani |
| Best Country | Morocco |
| Best Category | Phones |

---

# 📈 Generated Outputs

The pipeline generates analytical CSV files:

```text
output/
├── sales_by_country.csv
├── sales_by_product.csv
├── sales_by_customer.csv
└── sales_by_category.csv
```

These datasets can be used with:

- Power BI
- Tableau
- Excel
- Python
- Other BI tools

---

# ⚙️ Pipeline Automation

The complete pipeline can be executed with:

```bash
python pipeline.py
```

The pipeline performs:

1. PostgreSQL connection
2. Data extraction
3. Data inspection
4. Data transformation
5. Business analysis
6. KPI calculation
7. CSV export
8. Pipeline logging
9. Final summary

---

# 🔐 Environment Configuration

Database credentials are stored locally in `.env`.

Example:

```env
PG_HOST=localhost
PG_PORT=5432
PG_DATABASE=airbyte_destination
PG_USER=postgres
PG_PASSWORD=your_password
```

The `.env` file is excluded from GitHub through `.gitignore`.

**Never commit database passwords or other secrets.**

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/CHABAB23/ecommerce-data-engineering-pipeline.git
```

Enter the project:

```bash
cd ecommerce-data-engineering-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Pipeline

Make sure PostgreSQL and the required Airbyte/Docker infrastructure are running.

Configure the `.env` file.

Then execute:

```bash
python pipeline.py
```

---

# 📋 Requirements

Main Python dependencies:

- pandas
- numpy
- matplotlib
- psycopg2-binary
- SQLAlchemy
- python-dotenv

All dependencies are listed in:

```text
requirements.txt
```

---

# 🧪 Data Quality Checks

The Python analysis includes checks for:

- Missing values
- Duplicate records
- Data types
- High-value orders
- Date components
- Data consistency

---

# 📁 Outputs

Generated analytical datasets are stored in:

```text
output/
```

Pipeline execution logs are stored locally in:

```text
logs/
```

Log files are excluded from Git version control where appropriate.

---

# 🔮 Future Improvements

Potential improvements include:

- Apache Airflow orchestration
- Data quality testing with Great Expectations
- Incremental data loading
- Star-schema data warehouse
- Power BI dashboard
- CI/CD with GitHub Actions
- Cloud deployment
- Pipeline monitoring
- Automated alerts
- Larger datasets
- Unit and integration testing

---

# 💼 Career Relevance

This project demonstrates practical skills relevant to:

- Data Engineer
- Junior Data Engineer
- Data Analyst
- BI Analyst
- Analytics Engineer
- ETL Developer

The project is particularly relevant to organizations looking for professionals capable of working across data integration, databases, programming, analytics and automation.

---

# 🇲🇦 Professional Context

This project was developed as a practical Data Engineering portfolio project with the objective of demonstrating skills applicable to the Moroccan job market, particularly opportunities in Casablanca and multinational companies.

The project focuses on technologies and practices commonly encountered in modern data teams:

- ETL / ELT
- Data integration
- Relational databases
- SQL analytics
- Python data processing
- Pipeline automation
- Data quality
- Business intelligence
- Version control
- Reproducible data workflows

---

# 👤 Author

**CHABAB khalid**

Data Engineering Portfolio Project

Morocco 🇲🇦

---

# 📄 License

This project is intended for educational and portfolio purposes.