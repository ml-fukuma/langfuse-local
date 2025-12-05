from langfuse import Langfuse
import time, os

# Langfuse クライアント（v3 SDK）
langfuse = Langfuse(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)


trace = langfuse.trace(
    name="sample-trace",
    user_id="user-123"
)

span = trace.span(
    name="db-step",
    input={"query": "SELECT * FROM users"}
)
span.end(output={"result": "ok"})

gen = trace.generation(
    model="gpt-4",
    input="Tell me a joke",
    output="Funny joke result"
)

langfuse.flush()
print("sent!")
