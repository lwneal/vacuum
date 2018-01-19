import sys
import time
import environments, agents

max_iters = 100
agentname = 'RandomBot'
filename = 'squareworld.txt'
csv_filename = None
if '--help' in sys.argv:
    print("Usage: python main.py RandomBot squareworld.txt 200")
    print("    Bots: LeftBot, RandomBot, HumanBot")
    print("    Filename: Defaults to squareworld.txt")
    print("    Iters: Defaults to 100 iterations")
    exit()
if '--no-unicode' in sys.argv:
    sys.argv.remove('--no-unicode')
    environments.robot_char_map = environments.ascii_robot_char_map
    environments.character_map = environments.ascii_character_map
if '--graph' in sys.argv:
    csv_filename = 'graph.csv'

if len(sys.argv) > 1:
    agentname = sys.argv[1]
if len(sys.argv) > 2:
    filename = sys.argv[2]
if len(sys.argv) > 3:
    max_iters = int(sys.argv[3])


agent = getattr(agents, agentname)()
env = environments.VacuumWorld(filename)
for i in range(max_iters):
    time.sleep(.5)
    env.print_state(csv_filename)
    percepts = env.get_percepts()
    action = agent.act(percepts)
    env.update(action)
