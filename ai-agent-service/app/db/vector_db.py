from urllib.parse import quote_plus
from sqlalchemy import create_engine
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import PGVector

from app.config import *

encoded_password = quote_plus(
    POSTGRES_PASSWORD
)

CONNECTION_STRING = (
    f"postgresql+psycopg2://"
    f"{POSTGRES_USER}:"
    f"{encoded_password}@"
    f"{POSTGRES_HOST}:"
    f"{POSTGRES_PORT}/"
    f"{POSTGRES_DB}"
)

embeddings = OpenAIEmbeddings(
    api_key=OPENAI_API_KEY,
    model="text-embedding-3-small"
)

vector_store = PGVector(
    connection_string=CONNECTION_STRING,
    embedding_function=embeddings,
    collection_name="expense_policies"
)