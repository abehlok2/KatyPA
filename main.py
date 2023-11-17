import os
from openai import OpenAI
import autogen
from autogen import UserProxyAgent, AssistantAgent, GroupChat, GroupChatManager
from autogen.agentchat.contrib.teachable_agent import TeachableAgent
from autogen.oai import config_list_from_json
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
import smartsheet

from agents.ssagent2 import smartsheet_agent
from agents.teachable_id_getter import file_id_teachable_agent


admin_reports_id = 6756768966567812
schedule_id = 1388770797873028
dev_info_id = 5590471268427652
master_lists_id = 5416846410180484
nluf_id = 7890482492663684
pi_target_lists_id = 8931955019409284
target_inventory_id = 277269500454788
wfh_info_id = 6928551149627268
id_list = [admin_reports_id, schedule_id, dev_info_id, master_lists_id, nluf_id, pi_target_lists_id, target_inventory_id, wfh_info_id]
id_dict = {
    "Admin Reports": admin_reports_id, "Assembly Schedule": schedule_id, "Development Information": dev_info_id, "Master Lists": master_lists_id, "nluf_id": nluf_id, "PI Target Lists": pi_target_lists_id, "Target Inventory": target_inventory_id, "Work From Home Info": wfh_info_id,
}
openai_api_key = "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"
smartsheet_api_key = ""

config_list = config_list_from_json("/home/abehl/ssagent/OAI_CONFIG_LIST.json")
user = autogen.UserProxyAgent(
    name="user",
    code_execution_config = {"use_docker": False},
    max_consecutive_auto_reply=5,
    human_input_mode="NEVER",
)

# Set up the Group Chat
smartsheet_group_chat = GroupChat(
    agents=[user, smartsheet_agent, file_id_teachable_agent],
    messages=[
        {
            "role": "user",
            "content": "Here are the workspace mappings: " + str(id_dict)
        }
    ],
    max_round=6,
    admin_name="Smartsheet_Team_Group_Chat_Manager",
)


manager = GroupChatManager(
    name="Smartsheet_Team_Group_Chat_Manager",
    groupchat=smartsheet_group_chat,
    system_message="Group Chat Manager. Facilitiate the conversation between the user and the Smartsheet Team. Utilize the \
                    file_id_getter to make sure file IDs are correctly specified for code snippets that will execute \
                    locally.",
    llm_config={
        "api_key": openai_api_key,
        "model": "gpt-4-1106-preview",
        "temperature": 0,
    }
)

request = """
How many campaigns were there in FY2022?'
"""

def setup_request(request:str) -> str:
    new_request = ("Rather than attempting to execute any code, please produce the code snippet that you would execute \
    to carry out the user's stated objectives, if you were capable of executing code. The user will execute the code \
    themselves, locally.")
    request += "ENVIRONMENT VARIABLES:\n SMARTSHEET_API_KEY=\n"
    request += """"**FOR THE FILD ID TO NAME CORRELATOR ONLY**:\n\nCorrelate the following workspace IDs to their respective workspace names:\n\n'Admin Reports': 6756768966567812, 'Assembly Schedule': 1388770797873028, 'Development Information': 5590471268427652, 'Master Lists': 5416846410180484, 'nluf_id': 7890482492663684, 'PI Target Lists': 8931955019409284, 'Target Inventory': 277269500454788, 'Work From Home Info': 6928551149627268}"""
    new_request += f"""
    BEGIN NEW REQUEST:
    {request}
    """
    return new_request
print(str(id_dict))


message = setup_request(request)

user.initiate_chat(manager,message=message)





