from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session

boto_session = Session()
region = boto_session.region_name

agentcore_runtime = Runtime()

agent_name = "langgraph_claude_getting_started"
response = agentcore_runtime.configure(
    entrypoint = r"C:\Users\yuvra\OneDrive\YUVRAJ FILES\Coding\langgraph_bedrock.py",
    auto_create_execution_role=True,
    auto_create_ecr=True,
    requirements_file=r"C:\Users\yuvra\OneDrive\YUVRAJ_FILES\Coding\requirements.txt",
    region="us-east-1",
    agent_name="langgraph_claude_agent",
)
print("\n🚀 Launching agent to AWS CodeBuild for remote ARM64 compilation...")
launch_result = agentcore_runtime.launch()

print("\n Deployment initiated successfully!")
print(f"Agent ID: {launch_result.agent_id}")
