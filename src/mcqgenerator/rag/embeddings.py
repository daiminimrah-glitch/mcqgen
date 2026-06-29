from langchain_openai import OpenAIEmbeddings


def get_embedding_model():
    """
    Create and return the OpenAI embedding model.
    """

    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    return embedding_model