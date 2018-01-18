import time
import environments, agents

MAX_ITERS = 100

agent = agents.HumanBot()
env = environments.VacuumWorld()

for i in range(MAX_ITERS):
    time.sleep(.5)
    env.print_state()
    percepts = env.get_percepts()
    action = agent.act(percepts)
    env.update(action)
