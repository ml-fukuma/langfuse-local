from langfuse import Langfuse
import time, os

# Langfuse クライアント（v3 SDK）
langfuse = Langfuse(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)

# ---- trace（1リクエスト単位のまとまり）----
trace = langfuse.trace(
    name="sample-trace-v3-sdk-on-v2",
    user_id="user-123",
)

# ---- span（処理ステップ）----
span = trace.span(
    name="db-step",
    input={"query": "SELECT * FROM users"},
)

# 実処理っぽく待機
time.sleep(0.8)

# span 終了（v3 SDKでは output をここで渡す）
span.end(
    output={"result": ["Alice", "Bob"]},
)

# ---- LLM generation ログ（ChatGPT API 等の応答記録）----
generation = trace.generation(
    model="gpt-4-turbo",
    input="Hello, joke please.",
    output="Why did the cat sit on the computer? To keep an eye on the mouse!",
)

generation.end()  # generation は end が必要

# ---- 送信確定（flush）----
langfuse.flush()

print("sent to langfuse v2 server!")
