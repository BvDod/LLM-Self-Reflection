#%%
import langchain_community
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



#%%
from langchain_community.llms import Ollama
llm = Ollama(model="llama3.1")


# %%
llm.invoke("how can langsmith help with testing?")


# %%
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert on the field of psychology and psychotherapy."),
    ("user", "{input}")
])
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# %%
chain.invoke({"input": "Do you think its a smart idea for LLM's to play any kind of role in the field of mental health therapy?"})

# %%
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")

docs = loader.load()
# %%
from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings()


# %%
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)

# %%
from langchain.chains.combine_documents import create_stuff_documents_chain

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)


# %%
from langchain.chains import create_retrieval_chain

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# %%
response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
print(response["answer"])
# %%
