from bedrock_agentcore_starter_toolkit import Runtime

# 1. Connect to your active runtime instance
agentcore_runtime = Runtime()

print("Configuring local session context...")
# 2. Re-verify the local tracking context so the SDK knows which endpoint to call
agentcore_runtime.configure(
    entrypoint=r"C:\Users\yuvra\OneDrive\YUVRAJ FILES\Coding\langgraph_bedrock.py",
    agent_name="langgraph_claude_agent",
    auto_create_execution_role=True
)

print("\n🚀 Sending payload to your live cloud LangGraph agent...")
# 3. Invoke the agent with a test prompt
invoke_response = agentcore_runtime.invoke({"prompt": "How much is 2+2?"})
invoke_response