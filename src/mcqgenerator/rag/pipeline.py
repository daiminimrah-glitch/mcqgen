from .loader import load_pdf
from .chunker import chunk_documents
from .vector_store import store_documents
from .retriever import retrieve_documents

import uuid


def build_rag_pipeline(pdf_path):
    # Step 1: Extract text from the PDF
    documents = load_pdf(pdf_path)

    # Step 2: Split text into chunks
    chunks = chunk_documents(documents)

    # Step 3: Generate a unique namespace
    namespace = f"pdf-{uuid.uuid4().hex}"

    # Step 4: Create embeddings and store chunks
    vector_store = store_documents(chunks, namespace)

    return vector_store

def get_relevant_context(vector_store, query, k=5):
    # Retrieve relevant PDF chunks
    documents = retrieve_documents(
        vector_store,
        query,
        k=k
    )

    # Combine the retrieved text
    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    return context