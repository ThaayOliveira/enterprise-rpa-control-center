import sqlite3
import pandas as pd

def get_executions():
    conn = sqlite3.connect("rpa.db")

    df = pd.read_sql_query(
        "SELECT * FROM executions ORDER BY id DESC",
        conn
    )

    conn.close()

    return df