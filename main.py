import sys
import time
import environments, agents

max_iters = 100
agentname = 'RandomBot'
filename = 'squareworld.txt'
csv_mode = False
time_to_90 = False
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
    sys.argv.remove('--graph')
    csv_mode = True
    print("time,dirt")
if '--time-to-90' in sys.argv:
    sys.argv.remove('--time-to-90')
    time_to_90 = True

if len(sys.argv) > 1:
    agentname = sys.argv[1]
if len(sys.argv) > 2:
    filename = sys.argv[2]
if len(sys.argv) > 3:
    max_iters = int(sys.argv[3])

agent = getattr(agents, agentname)()
env = environments.VacuumWorld(filename)
for i in range(max_iters):
    if not csv_mode and not time_to_90:
        time.sleep(.5)
    env.print_state(csv_mode, time_to_90)
    percepts = env.get_percepts()
    action = agent.act(percepts)
    env.update(action)
