from agents.abstract import AgentAI
from models import Agent, Location, Action


"""
y 
^
|
|
------> x

"""


class DummyAgent(AgentAI):
    ActionToShift = {
        Action.Forward: (0, -1),
        Action.Left: (-1, 0),
        Action.Right: (0, -1)
    }

    async def move(self, my_agent: Agent, other_agents: list[Agent], obstacles: list[Location]) -> Action:
        for action in [Action.Forward, Action.Left, Action.Right]:
            is_empty = True
            new_position = Location(
                x=my_agent.position.x + self.ActionToShift[action][0],
                y=my_agent.position.y + self.ActionToShift[action][1]
            )
            for obstacle in obstacles:
                if new_position.x == obstacle.x and new_position.y == obstacle.y:
                    is_empty = False
            if is_empty:
                return action
        return Action.Idle
