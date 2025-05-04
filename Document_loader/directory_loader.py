from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
import time
start=time.time()

pdf_docs=DirectoryLoader('doc_folder',glob='*.pdf',loader_cls=PyPDFLoader)

docs=pdf_docs.lazy_load()

# print(len(docs))
print('**********************************************************************************************')
print('**********************************************************************************************')
# print(docs[0].page_content)
# print('**********************************************************************************************')
# print('**********************************************************************************************')
# print(docs[2].page_content)
for i, doc in enumerate(docs):
    print(f"\nDocument {i + 1}:")
    print(f"Metadata:\n {doc.metadata}")
    print(f"Content (first 200 characters): \n{doc.page_content[:500]}...")
print('**********************************************************************************************')
print('**********************************************************************************************')
# print(docs[0].page_content)
print(f'Time taken:{time.time()-start}')