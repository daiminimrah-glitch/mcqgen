from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):
    """
    Load a PDF and return its pages as LangChain Document objects.
    """

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents