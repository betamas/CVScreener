import os
import json
from openai import OpenAI
from fastapi import FastAPI
from typing import Dict
from pipeline.lmm import OpenAILMM
from prompt import CV_SCREENING_PROMPT

# Initialize FastAPI app
app = FastAPI()

# Stateful counter variable
openai_client = OpenAI(api_key=os.getenv("openaikey"))

# Create LLM Pipeline
MAX_OUTPUT_TOKENS = 600

llm = OpenAILMM("gpt-4o", max_tokens= MAX_OUTPUT_TOKENS)

@app.get("/answer")
async def get_answer_with_citations(message_json: str) -> Dict[str, str]:
    incoming_query = str(json.loads(message_json)['message'])
    
    filled_prompt = CV_SCREENING_PROMPT.format(text=incoming_query)

    prediction = llm(filled_prompt, None)
    print(f"Question: {incoming_query[:10]}")
    
    print(f"Predicted Answer: {prediction[:10]}")
    
    return {"result": prediction}

    
# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)

