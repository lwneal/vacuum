import time
import environments, agents

MAX_ITERS = 100
agent = 'RandomBot'
filename = 'bigworld.txt'

agent = getattr(agents, agent)()
env = environments.VacuumWorld(filename)
for i in range(MAX_ITERS):
    time.sleep(.5)
    env.print_state()
    percepts = env.get_percepts()
    action = agent.act(percepts)
    env.update(action)
