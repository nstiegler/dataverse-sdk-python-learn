#!/usr/bin/env python3

"""
Lab 1.1 — Credential Validator

Test connectivity to a Dataverse environment using multiple authentication
methods and report success/failure for each.

This script validates two credential types (AzureCliCredential and
ClientSecretCredential) by attempting to instantiate a ServiceClient and
perform a basic connection test. All credentials are loaded from environment
variables—nothing is hardcoded.

Required Environment Variables:
    DATAVERSE_URL       : The Dataverse environment URL (e.g., https://org.crm.dynamics.com)
    AZURE_TENANT_ID     : Azure AD tenant ID
    AZURE_CLIENT_ID     : Application (client) ID
    AZURE_CLIENT_SECRET : Client secret (for ClientSecretCredential tests)

Usage:
    $ python lab_1_1_credentials.py

Exit Codes:
    0 - All tested credential types authenticated successfully
    1 - One or more credential types failed authentication
"""

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
        client.list_tables() # most efficent option for determining access 
        print("The 'az_cli_credentials_test' function was a success")
    except:
        print("You failed you loser")


def client_secret_credentials_test(url: str, tenant_id, client_id, client_secret): 
    try:
        secret_credentials = ClientSecretCredential(tenant_id, client_id, client_secret)
        client = DataverseClient(url, secret_credentials)
        client.list_tables()
        print("success")
    except:
        print("The 'client_secret_credentials_test' failed but we will be okay")


# Test cerdentials 
az_cli_credentials_test(dataverse_url, AzureCliCredential())
client_secret_credentials_test(dataverse_url, az_tenant_id, az_client_id, az_client_secret)