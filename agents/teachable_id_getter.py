import os
import autogen
from autogen.agentchat.contrib.multimodal_conversable_agent import MultimodalConversableAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent
from autogen.agentchat.contrib.text_analyzer_agent import TextAnalyzerAgent
import os

openai_api_key = "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"

# workspace ids
admin_reports_id = 6756768966567812
schedule_id = 1388770797873028
dev_info_id = 5590471268427652
master_lists_id = 5416846410180484
nluf_id = 7890482492663684
pi_target_lists_id = 8931955019409284
target_inventory_id = 277269500454788
wfh_info_id = 6928551149627268



print(openai_api_key)
file_id_teachable_agent = TeachableAgent(
    name="file_id_getter",
    system_message="""
    You are a helpful AI assistant that can remember information taught to you by the user, or that you learn of 
    your own choosing. Only learn information that is relevant to your overarching goal, stated below:
    
    # MISSION
    Internally map the file names of the files in the Smartsheet_Specialist's Smartsheet account to their corresponding file IDs.
    Remember them so you can provide them to the user or to other agents when a particular file ID is needed, and only a
    natural language file name is provided.
    
    ## STRATEGY
    SMARTSHEET_API_KEY=7GJWGNGb7PaQ28tcSHYbwD1PkysZbzVHyv8dF
    -Utilize this API key to access the Smartsheet account via the smartsheet-python-sdk API. 
    -Gather and correspond the file names to their corresponding file IDs.
    -Remember them, and any information about them, so you can accurately provide them again. 
    
    ## RULES
    -Prioritize use of smartsheet SDK for all smartsheet-based interactions.
    -Always create a copy of a file before making modifications.
    -NEVER use a placeholder such as "your-api-key-here" or anything like that where the smartsheet api key should be.
    """,
    llm_config={
        "api_key":  openai_api_key,
        "model": "gpt-4-1106-preview",
        "temperature": 0,
    },
    teach_config={
        "verbosity": 1,
        "reset_db": False,
        "path_to_db_dir": "/home/abehl/ssagent/db",
        "prepopulate": False,
        "recall_threshold": 1.0,
    }
)

