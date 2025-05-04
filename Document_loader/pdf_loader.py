from langchain_community.document_loaders import WebBaseLoader,PyPDFLoader
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os,time

start=time.time()
pdf_obj=PyPDFLoader('Agentic AI.pdf')

docs=pdf_obj.load()
print(type(docs))
print(len(docs))
print('*****************************************************')
# print(docs[0])
print('*****************************************************')
print("contents of page")
print(docs[0].page_content)
print('*****************************************************')
print("Metadata of page")
print(docs[0].metadata)

load_dotenv()

os.environ['HF_HOME'] = 'D:\Data_Science_Learnings\Langchain'

llm=HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen2-0.5B-Instruct',
    task='text-generation', 
    pipeline_kwargs={
        'max_new_tokens': 300,  # Increased to avoid truncation
        'temperature': 0.1,
        'do_sample': True }
)

parser=StrOutputParser()

prompt=PromptTemplate(
    template="summarize the content from the document  \n{document}",
    input_variables=['document']
)

chain= prompt | llm | parser

res=chain.invoke({'document':docs[0].page_content})
print('*****************************************************')

print(res)
print(f'time taken :{time.time()-start}')