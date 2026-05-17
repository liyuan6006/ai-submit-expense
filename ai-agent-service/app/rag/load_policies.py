from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.db.vector_db import (
    vector_store
)

import os

POLICY_FOLDER = "policy-docs"

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

all_docs = []

for file in os.listdir(POLICY_FOLDER):

    if file.endswith(".pdf"):

        path = os.path.join(
            POLICY_FOLDER,
            file
        )

        loader = PyPDFLoader(path)

        docs = loader.load()

        split_docs = splitter.split_documents(
            docs
        )

        all_docs.extend(split_docs)

vector_store.add_documents(
    all_docs
)

print(
    "Policies loaded into pgvector"
)