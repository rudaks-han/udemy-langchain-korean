from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)


def split_text():
    loader = TextLoader("sample.txt")
    document = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=20, chunk_overlap=0)
    texts = text_splitter.split_documents(document)

    for i, text in enumerate(texts):
        print(f"{i} : {text.page_content}")


if __name__ == "__main__":
    split_text()

# 동해물과 백두산이 마르고 닳도록
# 하느님이 보우하사 우리나라 만세
# 무궁화\n\n삼천리\n\n화려 강산
# 대한사람 대한으로 길이 보전하세
