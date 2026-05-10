from .BaseDataModel import BaseDataModel
from .enums import DataBaseEnums
from .db_schemes import Project,DataChunk
#from bson.objectid import ObjectID 
from pymongo import InsertOne
class ChunkModel(BaseDataModel):
    def __init__(self,db_client:object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DataBaseEnums.COLLECTION_CHUNK_NAME.value]
    
    async def create_chunk(self,chunk:DataChunk):
        result=await self.collection.insert_one(dict(chunk))
        return chunk
    async def get_chunk(self,chunk_id:str):
        result =await self.collection.find_one({
            "_id":result.inserted_id 
        })
        if result is None:
            return None 
        return DataChunk(**result)
    


    
