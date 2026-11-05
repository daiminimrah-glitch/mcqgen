from dotenv import load_dotenv
load_dotenv()

import os

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore


from .embeddings import get_embedding_model
def get_pinecone_index():
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

    index_name = "quizforge-rag"

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    return pc.Index(index_name)

def store_documents(chunks, namespace):
    index = get_pinecone_index()
    embeddings = get_embedding_model()

    vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings,
    namespace=namespace
)

    vector_store.add_documents(chunks)

    return vector_store