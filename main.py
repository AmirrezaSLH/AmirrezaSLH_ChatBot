from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS to allow requests from your domain
origins = [
    "https://AmirrezaSLH.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/receive")
async def receive_message(request: Request):
    # Extract the string from the incoming request
    data = await request.json()
    message = data.get("message", "")
    print(f"Received message: {message}")
    return JSONResponse(content={"response": "Message Received"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
