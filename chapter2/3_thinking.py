import boto3
from dotenv import load_dotenv

# envからの情報読み取り
load_dotenv()

# boto3のライブラリを使って、bedrockサービスへのクライアントオブジェクト作成
client = boto3.client('bedrock-runtime')

#converse APIを実行
response = client.converse(
    modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages=[{
        "role":"user",
        "content" : [{
            "text" : "こんにちは"
        }]
    }],
    additionalModelRequestFields={
        "thinking" : {
            "type" : "enabled",
            "budget_tokens" : 1024
        },
    },
)

for content in response["output"]["message"]["content"]:
    if "reasoningContent" in content:
        print("<thinking>")
        print(content["reasoningContent"]["reasoningText"]["text"])
        print("</thinking>")
    elif "text" in content:
        print(content["text"])
