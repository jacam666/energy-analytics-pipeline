from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

STORAGE_ACCOUNT_NAME = "jclabstorage26"
CONTAINER_NAME = "raw-data"

files_to_upload = [
    {
        "local_path": "data/processed_energy.csv",
        "blob_name": "processed_energy.csv"
    },
    {
        "local_path": "data/charges_summary.csv",
        "blob_name": "reports/charges_summary.csv"
    },
    {
        "local_path": "data/monthly_summary.csv",
        "blob_name": "reports/monthly_summary.csv"
    },
    {
        "local_path": "data/energy_summary.csv",
        "blob_name": "reports/energy_summary.csv"
    }
]

account_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"

credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url, credential=credential)

for file in files_to_upload:
    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER_NAME,
        blob=file["blob_name"]
    )

    with open(file["local_path"], "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"Uploaded {file['local_path']} to {file['blob_name']}")

print("All files uploaded successfully!")