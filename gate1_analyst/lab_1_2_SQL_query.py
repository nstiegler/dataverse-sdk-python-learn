'''
Docstring for lab_1_2_SQL_query

'''


# IMPORTS 
from azure.identity import AzureCliCredential
from dotenv import load_dotenv
import os   
from PowerPlatform.Dataverse.client import DataverseClient
from PowerPlatform.Dataverse.core.errors import SQLParseError, HttpError
import pandas as pd

# CONFIGS
load_dotenv() # loading .env (environment) file
dataverse_url = os.getenv("DATAVERSE_URL") # get URL from .env file
configs_client = DataverseClient(dataverse_url, AzureCliCredential())


# FUNCTIONS
def test_connection(client: DataverseClient) -> bool:
    """Test that we can connect to Dataverse."""
    try:
        client.list_tables() # most efficent option for determining access 
        print("The 'az_cli_credentials_test' function was a success")
        return True
    except HttpError:
        print("HttpError — API failure (network, auth, server error)")
        return False
    

def query_to_excel(client: DataverseClient, query_statement: str, file_name: str) -> bool:
    """
    Execute SQL query and save results to Excel.

    Returns True on success, False on failure.
    """
    try:
        # step 1: Run query
        query_results = client.query_sql(query_statement)

        # step 2: Convert to DataFrame
        df_formatted_query_result = pd.DataFrame(query_results)

        # step 3: Export to Excel
        df_formatted_query_result.to_excel(file_name)

        # step 4: Report success 
        print(f"✓ Exported {len(df_formatted_query_result)} rows to {file_name}")
        return True

    except SQLParseError as e:
        print(f"✗ SQL syntax error: {e}")
        return False
    
    except HttpError as e:
        print(f"✗ API error: {e}")
        return False



# MAIN EXECUTION 
if test_connection(configs_client):
    # define query
    sql_query = "SELECT TOP 10 accountid, name FROM account" # OOTB table

    # define path 
    output_file = "outputs/lab_1_2_accounts.xlsx"

    # run it
    query_to_excel(configs_client, sql_query, output_file)
else:
    print("Cannot proceed wihtout connection")

