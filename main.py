import os, sys
path = os.path.abspath((os.path.dirname(__file__)))

if path not in sys.path:
    print('Adding path to PythonPath:', path)
    sys.path.append(path)

from sg_py import hello_world

def run():
    hello_world.hello_world()

if __name__ == '__main__':
    run()