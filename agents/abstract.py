from abc import ABC, abstractmethod
from models import Agent, Location, Action


class AgentAI(ABC):
    @abstractmethod
    async def move(self, my_agent: Agent, other_agents: list[Agent], obstacles: list[Location]) -> Action:
        pass
