from dotenv import load_dotenv
from langchain_community.document_loaders import csv_loader,CSVLoader


load_dotenv()

#csv_docs=csv_loader('df_date.csv')
CSV_loads=CSVLoader('df_date.csv')
docs=CSV_loads.load()
print(len(docs))
print(type(docs))
print(docs[:10])
print("*************************************************************")
print(docs[0].page_content)
print(docs[0].metadata)