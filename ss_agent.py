import os
import autogen
from autogen import UserProxyAgent, AssistantAgent,GroupChat, GroupChatManager
from autogen.agentchat.contrib.teachable_agent import TeachableAgent
from autogen.oai import config_list_gpt4_gpt35
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent

config_list = config_list_gpt4_gpt35()
user = autogen.UserProxyAgent(
    name="user",
    code_execution_config = {"work_dir": "C:\\users\\abehl\\ssagent", "use_docker": False},
    max_consecutive_auto_reply=3,
    human_input_mode="NEVER",
)

smartsheet_agent = GPTAssistantAgent(
    name="smartsheet_agent",
    llm_config={
        "config_list": config_list,
        "assistant_id" : "asst_d8huRhrW5jZ1wh1UcZNfAAdx",
        "check_every_ms": 2000,
        "tools": ["code_interpreter", "knowledge_retrieval"],
    }
)

code_reviewer = autogen.AssistantAgent(
    name="Code_Reviewer",
    llm_config={
        "config_list": config_list,
        "temperature": 0,
        "seed": 1,
    },
    system_message="""
    # ROLE 
    Code_Reviewer
    
    # MISSION
    Check python code snippets for dangerous or bad behaviors.
    
    # BEHAVIOR
    Parse the python code snippets line-by-line. They will be primarily used for interacting with the 
    smartsheet API via the smartsheet-python-sdk. 
    
    Then, run back through the code snippets ensuring that there are not likely to be a crash, or bad behavior.
    If the code snippet looks like it will function appropriately, pass it to code_executor. 
    If you notice ERRORS or other bad behavior, make the necessary modifications to the code snippet, and pass it to the code_executor. 
    If uncertain, ask the user to decide for you. 
    
    **WHEN YOU HAVE COMPLETED YOUR REVIEW REPLY "TERMINATE"**
    """,
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)

groupchat_manager_sys_msg = "You are the manager of the smartsheet team groupchat. Please facilitate the conversation between the user and the smartsheet team members."
ss_groupchat = GroupChat(
    agents=[user, smartsheet_agent, code_reviewer],
    messages=[],
    max_round=5,
    admin_name="smartsheet_groupchat_manager",
)

ss_groupchat_manager = GroupChatManager(
    name="smartsheet_groupchat_manager",
    groupchat=ss_groupchat,
)
request = """
Please look at the smartsheet file"CoreHeat-22A" in smartsheet and then, using the column headers as a template, create
a new sheet named "CoreHeat-22A_new" in smartsheet.
""" + " " + str(os.getenv("OPENAI_API_KEY")) + " Here is the API key"

user.initiate_chat(ss_groupchat_manager, message=request)





