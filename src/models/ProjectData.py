from BaseDataModel import BaseDataModel
from db_schemes import Project
class ProjectModel(BaseDataModel):
    def __init__(self,db_client:object):
        super().__init__(db_client)
        self.collection = self.db_client['projects']
        async def create_project(self,project_data:dict)->str:
            project = Project(**project_data)
            result = await self.collection.insert_one(project.dict())
            return str(result.inserted_id)