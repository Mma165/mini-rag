from pydantic import BaseModel 
from typing import Optional
class ProcessRequest(BaseModel):
    file_id:str 
    chunk_size:Optional[int]=1048576 # 1MB default chunk size for processing the file in chunks to avoid memory issues.
    overlap_size:Optional[int]=256 # 256 bytes default overlap size to ensure that we don't miss any data when processing the file in chunks. This is important for cases where the data is split across chunks and we need to ensure that we capture all relevant information.
    do_reset:Optional[bool]=False # flag to indicate whether to reset the processing state for the file. This can be useful in cases where we want to reprocess a file from the beginning or if there was an error during processing and we want to start fresh.
    