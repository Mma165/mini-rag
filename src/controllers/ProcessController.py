from .BaseController import BaseController 
from .ProjectController import ProjectController
from models import ProcessingEnum
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter # I will use RecursiveCharacterTextSplitter because it is a powerful and flexible text splitter that can handle various types of documents and allows for customizable chunk sizes and overlaps. This will help us to effectively split the content of the files into manageable chunks for processing while preserving the context and structure of the original document.
import os
class ProcessController(BaseController):
    def __init__(self,project_id:str):
        super().__init__()
        self.project_id=project_id
        self.project_path=ProjectController().get_project_path(project_id=project_id)
    
    def get_file_extension(self,file_id:str):
        return os.path.splitext(file_id)[-1]
    
    def get_file_loader(self,file_id:str):
        file_path=os.path.join(self.project_path,file_id)
        file_extension=self.get_file_extension(file_id=file_id)
        if file_extension==ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path) # I will use PyMuPDFLoader to load PDF files because it is a powerful and efficient library for handling PDF documents. It allows us to easily extract text and metadata from PDF files, which is essential for our processing tasks. Additionally, PyMuPDFLoader provides robust support for various PDF features, making it a reliable choice for our application.
        elif file_extension==ProcessingEnum.TXT.value:
            return TextLoader(file_path,encoding="utf-8") # I will use utf-8 encoding to ensure that we can handle a wide range of characters in the text files. This is important for cases where the text files may contain special characters or non-English text. By using utf-8 encoding, we can ensure that we can properly read and process the content of the text files without encountering any encoding issues.
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
    def get_file_content(self,file_id:str):
        loader=self.get_file_loader(file_id=file_id)
        return loader.load()
    
     #This is the function that Eng. Abo bkr choose to split but I found that the scond one is better in documentation 
    def split_file_content(self,file_content:list,file_id:str,chunk_size:int,overlap_size:int):     
        text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len
            )
        
        file_content_text=[
            record.page_content 
            for record in file_content
        ]    
        file_content_metadata=[
            record.metadata 
            for record in file_content
        ]
        chunks=text_splitter.create_documents(
            file_content_text,
            file_content_metadata
        )

        return chunks
    
    
    
    
    
    
    
    
