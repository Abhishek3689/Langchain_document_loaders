from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

pdf_obj=PyPDFLoader('Agentic AI.pdf')
docs=pdf_obj.load()

splitter=CharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=0,
    separator=''
)

result=splitter.split_documents(docs)

print(len(result))
print("********************************************************************")
for i,res in enumerate(result):
    print(f'record_{i+1}')
    print(res.page_content)
    print('***************************New record*************************')