def retrieve_documents(vector_store, query, k=5):
    """
    Retrieve the most relevant PDF chunks
    for a given query.
    """
    documents = vector_store.similarity_search(
        query,
        k=k
    )

    return documents