from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os,time

start=time.time()
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
    template="What is the product we are talking about \n{document}",
    input_variables=['document']
)
url='https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader=WebBaseLoader(url)

docs=loader.load()

chain=prompt | llm | parser
print(len(docs))
print('*********************************************************************************************')
# print(docs[0].page_content)

res=chain.invoke({'document':docs[0].page_content})
print(res)
print(f'Time taken:{time.time()-start}')