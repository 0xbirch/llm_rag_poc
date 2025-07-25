import sqlite3
import pandas as pd
import os 
from langchain_community.utilities.sql_database import SQLDatabase
from langchain.chat_models import init_chat_model
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from dotenv import load_dotenv

load_dotenv()

def load_trade_signals(csv_file_path, database_name, table_name):
    df = pd.DataFrame()

    for file in os.listdir(csv_file_path):
        if file.endswith('.csv'):
            file_path = os.path.join(csv_file_path, file)
            df = pd.concat([df, pd.read_csv(file_path)], ignore_index=True)
    print(f"Loaded {len(df)} rows from {csv_file_path}")

    conn = sqlite3.connect(database_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def connect_to_db(database_name):
    db = SQLDatabase.from_uri(f"sqlite:///{database_name}")
    llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    print(toolkit.get_tools())



load_trade_signals("rag_data/trades", "rag_poc_database.db", "trades")
connect_to_db("rag_poc_database.db")