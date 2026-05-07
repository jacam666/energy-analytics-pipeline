import subprocess

# Run the processing script first
subprocess.run(["python", "scripts/process_data.py"])

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

STORAGE_ACCOUNT_NAME = "jclabstorage26"
CONTAINER_NAME = "raw-data"
LOCAL_FILE_PATH = "data/processed_energy.csv"
BLOB_NAME = "processed_energy.csv"

account_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"

credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url, credential=credential)

blob_client = blob_service_client.get_blob_client(
    container=CONTAINER_NAME,
    blob=BLOB_NAME
)

with open(LOCAL_FILE_PATH, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("Upload successful!")