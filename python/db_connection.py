import pyodbc

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=amazon_fulfillment;"
        "Trusted_Connection=yes;",
        autocommit=True
    )
