from fastapi import FastAPI,APIRouter,Depends ,UploadFile,File,status
from fastapi.responses import JSONResponse
from helpers import get_settings, Settings
from controllers import DataController, ProjectController, ProcessController
from models import ResponseSignals
from routes import ProcessRequest
import os 
import aiofiles
import logging 
logger=logging.getLogger("uvicorn.error")  
data_router=APIRouter(
  prefix="/api/v1/data",
    tags=["api_v1","data"]
)
@data_router.post("/upload/{project_id}")

async def upload_data(project_id:str, file: UploadFile = File(...),
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
    file_path,file_id=DataController().generate_unique_file_path(orginal_file_name=file.filename,project_id=project_id)
    try:
      async with aiofiles.open(file_path, 'wb') as f: # Open the file asynchronously for writing binary data
          while chunks  := await file.read(settings.File_Default_Chunk_Size):  # Read the file content asynchronously
            await f.write(chunks)  # Write the content to the new file asynchronously
    except Exception as e:
         logger.error(f"Error saving file: {e}") 
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                              content={"result_signal": ResponseSignals.File_Save_Error.value})
    return JSONResponse( content={"result_signal": ResponseSignals.File_Upload_Success.value,
                                  "file_id": file_id})


@data_router.post("/process/{project_id}")

async def process_endpoint(project_id:str,process_request:ProcessRequest):
    file_id=process_request.file_id
    chunk_size=process_request.chunk_size
    overlap_size=process_request.overlap_size
    process_controller=ProcessController(project_id=project_id)
    file_content=process_controller.get_file_content(file_id=file_id)
    file_chunks=process_controller.split_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap_size=overlap_size
    )
    if file_chunks is None or len(file_chunks)==0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"result_signal": ResponseSignals.File_Processing_Error.value})
    return file_chunks