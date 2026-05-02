from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignals
import os 
import re

class DataController(BaseController):
    def __init__(self):
        super().__init__()

    async def validate_uploaded_file(self,file: UploadFile):
        if file.content_type not in self.settings.File_Allowed_Types: 
            return False, ResponseSignals.File_Type_Not_Supported.value
        
        if file.size >self.settings.File_Max_Size:
            return False, ResponseSignals.File_Size_Exceeded.value
        return True, ResponseSignals.File_Upload_Success.value
    
    
    def generate_unique_file_name(self,orginal_file_name:str,project_id:str):
        # I will generate a unique file name by adding a random string to the original file name.
        random_key=self.generate_random_string()
        project_path=ProjectController().get_project_path(project_id=project_id)# I will get the project path to save the file in the correct location.
        cleaned_file_name=self.clean_file_name(orginal_file_name=orginal_file_name)
        new_file_path=os.path.join(project_path,f"{random_key}_{cleaned_file_name}")
        while os.path.exists(new_file_path):
            random_key=self.generate_random_string()
            new_file_path=os.path.join(project_path,f"{random_key}_{cleaned_file_name}")
        return new_file_path

    def clean_file_name(self,orginal_file_name:str):
        # I will clean the file name by removing any special characters and spaces to avoid any issues with file systems.
        cleaned_file_name=re.sub(r'[^\w\-_\. ]', '_', orginal_file_name) #replace any special characters with underscores
        cleaned_file_name=re.sub(r'\s+', '_', cleaned_file_name) # replace spaces with underscores
        return cleaned_file_name