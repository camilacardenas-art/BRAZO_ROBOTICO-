# Import of the needed libraries and modules

from transitions import Machine
from Wally import *

robot = Wally

# Creation of the different states for the robot
states=['power_on', 'idle', 'area_reached', 'robot_stuck', 'recollect_mode', 'camera_offline', 'claw_full', 'object_dropped', 'item_analized', 'filling_container', 'object_changed', 'area_cleaned', 'sudden_stop']

# Creation of the transitions between states (possible real use cases)
transitions = [
    { 'trigger': 'startbutton', 'source': 'power_on', 'dest': 'idle' },
    { 'trigger': 'continuebutton', 'source': 'idle', 'dest': 'area_reached' },
    { 'trigger': 'cbrobotstuck', 'source': 'idle', 'dest': 'robot_stuck' },
    { 'trigger': 'movementfailed', 'source': 'robot_stuck', 'dest': 'idle' },
    { 'trigger': 'objectdetected', 'source': 'area_reached', 'dest': 'recollect_mode' },
    { 'trigger': 'cameradisconnected', 'source': 'recollect_mode', 'dest': 'camera_offline' },
    { 'trigger': 'systemerror', 'source': 'camera_offline', 'dest': 'idle' },
    { 'trigger': 'grabbedobject', 'source': 'recollect_mode', 'dest': 'claw_full' },
    { 'trigger': 'itemdropped', 'source': 'claw_full', 'dest': 'object_dropped' },
    { 'trigger': 'aianalysis', 'source': 'claw_full', 'dest': 'item_analized' },
    { 'trigger': 'objectcollected', 'source': 'item_analized', 'dest': 'filling_container' },
    { 'trigger': 'objectdeposited', 'source': 'filling_container', 'dest': 'recollect_mode' },
    { 'trigger': 'emergencystop', 'source': 'recollect_mode', 'dest': 'sudden_stop' },
    { 'trigger': 'failedtograb', 'source': 'recollect_mode', 'dest': 'object_changed' },
    { 'trigger': 'objectreselected', 'source': 'object_changed', 'dest': 'recollect_mode' },
    { 'trigger': 'nomoreobjects', 'source': 'recollect_mode', 'dest': 'area_cleaned' },
    { 'trigger': 'movementactive', 'source': 'area_cleaned', 'dest': 'area_reached' }
]

# Initialize
machine = Machine(robot, states=states, transitions=transitions, initial='power_on')

# Use cases

def case1(*args):
    machine.set_state('claw_full')
    robot.itemdropped()
    print(robot.state)
    pass

def case2(*args):
    machine.set_state('claw_full')
    robot.itemdropped()
    print(robot.state)
    pass

def case3(*args):
    machine.set_state('idle')
    robot.cbrobotstuck()
    print(robot.state)
    pass

def case4(*args):
    machine.set_state('recollect_mode')
    robot.emergencystop()
    print(robot.state)
    pass

def case5(*args):
    machine.set_state('idle')
    robot.continuebutton()
    print(robot.state)
    pass

def case6(*args):
    machine.set_state('power_on')
    robot.startbutton()
    print(robot.state)
    pass

def case7(*args):
    machine.set_state('item_analized')
    robot.objectcollected()
    print(robot.state)
    pass

def case8(*args):
    machine.set_state('claw_full')
    robot.aianalysis()
    print(robot.state)
    pass

def case9(*args):
    machine.set_state('robot_stuck')
    robot.movementfailed()
    print(robot.state)
    pass

def case10(*args):
    machine.set_state('recollect_mode')
    robot.nomoreobjects()
    print(robot.state)
    pass

def case11(*args):
    machine.set_state('recollect_mode')
    robot.cameradisconnected()
    print(robot.state)
    pass

def case12(*args):
    machine.set_state('recollect_mode')
    robot.failedtograb()
    print(robot.state)
    pass

def case13(*args):
    machine.set_state('claw_full')
    robot.aianalysis()
    print(robot.state)
    pass
