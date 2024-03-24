from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def base():
    return {"message": "Hey Fast Api getting added to my resume."}
