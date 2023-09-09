from lib2to3.pgen2.token import OP
from langchain.document_loaders import UnstructuredFileLoader, WebBaseLoader
from langchain.vectorstores import Chroma, FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import  CharacterTextSplitter
import os
from constant import *

class ChatBot():
    def __init__(self) -> None:
        os.environ["OPENAI_API_KEY"] = API_KEY
        self.read_file()
    
    def read_file(self):
        load = WebBaseLoader(WEBSITE)
        doc = load.load()
        
        test_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
        web_doc = test_splitter.split_documents(doc)
        print(web_doc)
        
        self.emb = FAISS.from_documents(web_doc, embedding=OpenAIEmbeddings())
        
    def chain(self, question):
        chain = ConversationalRetrievalChain.from_llm(
            llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo"),
            retriever = self.emb.as_retriever(),
            verbose = False
        )
        query = BASE_PROMPT + question
        answer = chain({"question": query, "chat_history": ''})
        return answer["answer"]
    
if __name__ == "__main__":
    obj = ChatBot()
    print(obj.chain("what is l1 point?"))
    