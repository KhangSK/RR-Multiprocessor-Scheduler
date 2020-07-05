from taskclass import Task
import random

def read_input(filename, proclist):
    """ Read file with filename, return (numProcessors, numProcesses) and read modify proclist"""
    f = open(filename, 'r')
    numProcessors = int(f.readline())
    numProcesses = int(f.readline())
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    temp = 0
    for _ in range(numProcesses):
        line = f.readline()
        parts = line.split(';')
        # rgb = (random.random(), random.random(), random.random())
        rgb = colors[temp]
        temp += 1
        proclist.append(Task(parts[0], int(parts[1]), int(parts[2]), rgb))
    
    proclist.sort(key=sort_key)
    
    return (numProcessors, numProcesses)

def sort_key(task):
    return task.arrival_time