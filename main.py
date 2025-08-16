import uvicorn
from agents.dummy_agent import DummyAgent
from models import Request, Response
from fastapi import FastAPI

app = FastAPI()

agents = {
    '1': DummyAgent(), '2': DummyAgent(), '3': DummyAgent(), '4': DummyAgent()
}


@app.post('/api/v1/next_move')
async def get_next_move(request: Request) -> Response:
    return Response(
        id=request.my_agent.id,
        move=agents[request.my_agent.id].move(request.my_agent, request.other_agents, request.obstacles)
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=0, log_level="info")
