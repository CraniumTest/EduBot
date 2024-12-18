from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()

# Load your OpenAI API key
OPENAI_API_KEY = "your-api-key"
openai.api_key = OPENAI_API_KEY

class Query(BaseModel):
    question: str

@app.post("/ask/")
async def ask_question(query: Query):
    try:
        # Interact with the LLM
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query.question,
            max_tokens=150
        )
        return {"answer": response['choices'][0]['text'].strip()}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Additional routes for learning paths and more can be appended here.
