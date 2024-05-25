import os
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Pinecone
import pinecone

# from langchain_community.vectorstores import Pinecone as PineconeLangChain

# pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
from consts import INDEX_NAME

pinecone.Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENVIRONMENT"),
)


def run_llm(query: str):
    # print(f"key: {os.environ["PINECONE_API_KEY"]}")
    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index(
        index_name=os.getenv("PINECONE_INDEX_NAME"), embedding=embeddings
    )
    chat = ChatOpenAI(verbose=True, temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=chat,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True,
    )
    return qa({"query": query})


if __name__ == "__main__":
    print(run_llm("What is vector store?"))
