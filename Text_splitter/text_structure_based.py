from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

pdf_obj=PyPDFLoader('Agentic AI.pdf')

docs=pdf_obj.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=50
)

## Perform split

chunks=splitter.split_documents(docs)

for i,chunk in enumerate(chunks[:5]):
    print(f'chunk_{i+1}')
    print(chunk.page_content)
    print(f'**********************End of Chunk_{i+1}**************************')