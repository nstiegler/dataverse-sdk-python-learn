from azure.identity import AzureCliCredential
from dotenv import load_dotenv
import os
from PowerPlatform.Dataverse.client import DataverseClient

load_dotenv()
url = os.getenv("DATAVERSE_URL")
credential = AzureCliCredential()
client = DataverseClient(url, credential)

# Now explore
tables = client.list_tables()
print(type(tables))
print(len(tables))
print(tables[0])