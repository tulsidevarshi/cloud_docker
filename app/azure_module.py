import os
from fastapi import FastAPI 
from azure.storage.blob.aio import BlobServiceClient 
import asyncio 

 
app = FastAPI(title="Async Azure Blob Extractor") 

# Use the URL of your storage account instead of a connection string
STORAGE_ACCOUNT_NAME = "sgupgradpratice"
STORAGE_ACCOUNT_URL = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"

# connection string
CONN_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

if not CONN_STRING or len(str(CONN_STRING).strip()) <= 0:
    try:
        with open("azure_connection_string.txt", "r") as f:
            CONN_STRING = f.read().strip()
    except FileNotFoundError:
        raise ValueError("Azure connection string is not set in environment variables or azure_connection_string.txt file.")

# 3. Last resort sanity check
if not CONN_STRING or "placeholder" in CONN_STRING:
    raise ValueError("Azure connection string is invalid, empty, or missing.")
    
# 
# Automatically authenticates using Azure App Service's identity
blob_service_client = BlobServiceClient(STORAGE_ACCOUNT_URL, credential=CONN_STRING)

# Create async blob client 
# blob_service_client = BlobServiceClient.from_connection_string(CONN_STRING) 

@app.get("/extract-from-azure") 
async def extract_azure_data(): 
    # 1. Connect to container + blob 
    container_client = blob_service_client.get_container_client("fastapi-practice-azure") 
    blob_client = container_client.get_blob_client("Enterprise_GenAI_Adoption_Impact.csv") 
 
    # 2. Download blob asynchronously 
    stream = await blob_client.download_blob() 
    content = await stream.readall() 
 
    # 3. Simulate async ETL work 
    await asyncio.sleep(1) 
 
    # 4. Return response 
    return { 
        "message": "Azure blob extracted successfully", 
        "size": len(content) 
    }

# Output received:
"""
{
  "message": "Azure blob extracted successfully",
  "size": 18116386
}
"""