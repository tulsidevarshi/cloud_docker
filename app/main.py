from fastapi import FastAPI 
import asyncio 
 
#from gcp_module import extract_gcp_data 
from app.azure_module import extract_azure_data 
#from aws_module import extract_aws_data 
 
app = FastAPI(title="Multi-Cloud ETL Extractor") 
 
@app.get("/run-all") 
async def run_all_extractors(): 
    results = await asyncio.gather( 
        extract_azure_data(),
        # extract_gcp_data(),
        # extract_aws_data()
    ) 
    return {
        "Azure": results[0]
        # "GCP": results[1],
        # "AWS": results[2]
    }