from langfuse import get_client

langfuse = get_client(
    public_key="LF_PK_XXXX",
    secret_key="LF_SK_XXXX",
    host="http://localhost:3000"
)

with langfuse.start_as_current_observation(as_type="span", name="sample-span") as span:
    # 任意の処理
    span.update(input={"event": "start"})
    # もし LLM の出力があれば generation をネスト
    with langfuse.start_as_current_observation(as_type="generation", model="gpt-4o", name="llm-call",
                                               input={"prompt": "Hello"}, output={"response": "Hi"}) as gen:
        pass

langfuse.flush()
