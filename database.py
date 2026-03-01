from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv(
    "postgresql://product_db_p5ew_user:wdzQAkaoGaocbFn3Koc5pRI6LSk6530H@dpg-d6ht1eogjchc73cumf80-a/product_db_p5ew",
    "postgresql://postgres:password@localhost:5432/mydb"
)
engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}  # Required for Render
)
session = sessionmaker(autoflush=False,autocommit=False,bind=engine)