import time
from bedrock_agentcore_starter_toolkit import Runtime

# 1. Initialize the instance correctly (creates 'self')
agentcore_runtime = Runtime()

print("Configuring local tracking runtime context...")
# 2. Local configuration setup (Passing this means status() knows who to look for)
agentcore_runtime.configure(
    entrypoint=r"C:\Users\yuvra\OneDrive\YUVRAJ FILES\Coding\langgraph_bedrock.py",
    agent_name="langgraph_claude_agent",
    auto_create_execution_role=True
)

print("\nChecking Bedrock AgentCore Runtime status...")
# 3. REMOVE 'agent_name' HERE: Call status() empty as the SDK expects
status_response = agentcore_runtime.status()
status = status_response.endpoint["status"]

# Terminal loops every 15 seconds until it hits a final state
final_states = ["READY", "CREATE_FAILED", "DELETE_FAILED", "UPDATE_FAILED"]

while status not in final_states:
    print(f"Current Status: {status}... (Checking again in 15 seconds)")
    time.sleep(15)
    
    # Remove 'agent_name' from the loop status call as well
    status_response = agentcore_runtime.status()
    status = status_response.endpoint["status"]

if status == "READY":
    print("\n🎉 Your LangGraph agent is officially LIVE and ready for traffic!")
else:
    print(f"\n❌ Deployment finished with an unexpected status: {status}")