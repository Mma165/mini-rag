from enum import Enum

class ResponseSignals(Enum):
    """
    Enum for response signals.
    """
    File_Validation_Success = "File validation successful."
    File_Validation_Failed = "File validation failed."
    File_Type_Not_Supported = "File type is not supported."
    File_Size_Exceeded = "File size exceeded the maximum allowed size."
    File_Upload_Success = "File uploaded successfully."
    File_Uploaded_Failed = "File upload failed."
    File_Save_Error = "Error saving file."