from fastapi import FastAPI,APIRouter,Depends ,UploadFile,File,status
from fastapi.responses import JSONResponse
from helpers import get_settings, Settings
from controllers import DataController, ProjectController
from models import ResponseSignals
import os 
import aiofiles
import logging 
logger=logging.getLogger("uvicorn.error")  
data_router=APIRouter(
  prefix="/api/v1/data",
    tags=["api_v1","data"]
)
@data_router.post("/upload/{project_id}")

async def upload_data(project_id:str,file: UploadFile,
                      settings:Settings=Depends(get_settings)
                      ):
# I need to validate the data to make sure it is in the correct format and 
# the correct size before saving it to the database 

      #I will validate the logic into controllers as follwing MVC architecture. 
    is_valid, result_signal = await DataController().validate_uploaded_file(file)
    if not is_valid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"result_signal": result_signal})
    


# If the file is valid, I will save it to the database and return a success message but now to files in the assets folder for simplicity.

# Also I need to valicate that the file name is unique for each project to avoid overwriting files.
    project_dir_path=ProjectController().get_project_path(project_id=project_id)
    file_path=DataController().generate_unique_file_name(orginal_file_name=file.filename,project_id=project_id)
    try:
      async with aiofiles.open(file_path, 'wb') as f: # Open the file asynchronously for writing binary data
          while chunks  := await file.read(settings.File_Chunk_Size):  # Read the file content asynchronously
            await f.write(chunks)  # Write the content to the new file asynchronously
    except Exception as e:
         logger.error(f"Error saving file: {e}") 
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                              content={"result_signal": ResponseSignals.File_Save_Error.value})
    return JSONResponse( content={"result_signal": ResponseSignals.File_Upload_Success.value})
    