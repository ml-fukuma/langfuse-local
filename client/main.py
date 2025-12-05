from langfuse import Langfuse
import time

# ---------------------------
# ★ここに Langfuse UI のキーをそのまま書く（v2 は直接渡す方式 OK）
# ---------------------------
langfuse = Langfuse(
    public_key="LF_PK_XXXX",
    secret_key="LF_SK_XXXX",
    host="http://localhost:3000",  # self-host
)

# ---- trace（1会話・1リクエスト単位）----
trace = langfuse.trace(
    name="sample-trace",
    user_id="user-123",
)

# ---- span（内部処理ステップ）----
span = trace.span(
    name="sample-span",
    input="User asked: Hello?",
)

time.sleep(1.2)

span.end(
    output="AI response: Hi, nice to meet you!"
)

# ---- generation（LLM 応答ログ）----
gen = trace.generation(
    model="gpt-4-turbo",
    input="Tell me a joke",
    output="Why did the cat sit on the computer? To keep an eye on the mouse!"
)

trace.end()

langfuse.flush()
print("sent!")
