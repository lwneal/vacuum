import time
import environments, agents

MAX_ITERS = 100

agent = agents.HumanBot()
env = environments.VacuumWorld()

for i in range(MAX_ITERS):
    percepts = env.get_percepts()
    action = agent.act(percepts)
    env.update(action)
    env.print_state()
    time.sleep(.5)
