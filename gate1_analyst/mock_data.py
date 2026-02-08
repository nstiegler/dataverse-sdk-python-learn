import pandas as pd

data = {
    "id": list(range(1, 27)),
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry", 
             "Ivy", "Jack", "Karen", "Leo", "Mia", "Noah", "Olivia", "Paul", 
             "Quinn", "Rachel", "Sam", "Tina", "Uma", "Victor", "Wendy", "Xavier", 
             "Yara", "Zach"],
    "age": [25, 32, 28, 45, 23, 38, 29, 51, 34, 27, 42, 31, 26, 39, 33, 48, 
            24, 36, 30, 44, 22, 41, 35, 29, 37, 28],
    "department": ["Sales", "Engineering", "Marketing", "HR", "Engineering", 
                   "Sales", "Marketing", "Finance", "Engineering", "Sales", 
                   "HR", "Engineering", "Marketing", "Finance", "Sales", 
                   "Engineering", "HR", "Marketing", "Finance", "Sales", 
                   "Engineering", "Marketing", "HR", "Finance", "Sales", "Engineering"],
    "salary": [55000, 78000, 62000, 71000, 85000, 59000, 64000, 92000, 81000, 
               57000, 68000, 76000, 61000, 88000, 54000, 79000, 66000, 63000, 
               84000, 58000, 73000, 65000, 69000, 87000, 56000, 77000]
}


df = pd.DataFrame(data)

print(df)

#######################################

# Imports
from azure.identity import AzureCliCredential, ClientSecretCredential
from dotenv import load_dotenv
import os   
from PowerPlatform.Dataverse.client import DataverseClient


# Configs 
load_dotenv() # loading .env (environment) file
dataverse_url = os.getenv("DATAVERSE_URL") # get URL from .env file
az_tenant_id = os.getenv("AZURE_TENANT_ID") 
az_client_id = os.getenv("AZURE_CLIENT_ID")
az_client_secret = os.getenv("AZURE_CLIENT_SECRET") 


# Functions
def az_cli_credentials_test(url: str, az_cli_credential):
    try:
        client = DataverseClient(url, az_cli_credential)
        print(client.list_tables())
    except:
        print("You failed you loser")

# List tables
az_cli_credentials_test(dataverse_url, AzureCliCredential())        