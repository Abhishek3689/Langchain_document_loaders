import os
from langchain_community.document_loaders import TextLoader,csv_loader

text_loader=TextLoader('genai.txt')

print(text_loader)

docs=text_loader.load()

print(type(docs))
print(len(docs))
print(docs)
print('******************************************************************')
print(docs[0].page_content)
