from pydantic import BaseModel
from enum import Enum


class Action(str, Enum):
    Forward = 'Forward'
    Backward = 'Backward'
    Left = 'Left'
    Right = "Right"
    Idle = "Idle"


class Status(str, Enum):
    Active = "Active"
    Crushed = "Crushed"
    Interrupted = "Interrupted"


class Location(BaseModel):
    x: int
    y: int


class Agent(BaseModel):
    id: str
    position: Location


class Request(BaseModel):
    my_agent: Agent
    other_agents: list[Agent]
    obstacles: list[Location]
    status: Status


class Response(BaseModel):
    id: str
    move: Action
