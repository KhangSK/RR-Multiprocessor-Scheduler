import sys
import matplotlib.pyplot as plt
from cv2 import cv2
from PIL import Image

def draw_gantt(CPUs, time, proclist, quantum):
    """ Draw gantt chart based on CPUs history and time elapsed"""
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()

    # Setting labels for x-axis and y-axis 
    gnt.set_xlabel('Gantt Chart')
    gnt.set_ylabel('Processor')

    arrPosition = []
    arrCPU = []
    y_tick_range = 10
    for i in range(len(CPUs)):
        arrPosition += [y_tick_range]
        y_tick_range += 10
        arrCPU.append(CPUs[i].cpuname)

    # Setting Y-axis and X-axis limits
    gnt.set_ylim(0, y_tick_range)
    gnt.set_xlim(0, time + 1)
    # Setting ticks on y-axis 
    gnt.set_yticks(arrPosition) 
    # Labelling tickes of y-axis 
    gnt.set_yticklabels(arrCPU)
    # Setting graph attribute 
    gnt.grid(True)

    writeProcess = {}
    quantumProcess = {}
    for i in proclist:
        writeProcess[i.color] = [False, i.proc_name]
        quantumProcess[i.proc_name] = 0
    for x in range(time):
        for y in range(len(CPUs)):
            if CPUs[y].history[x] is not None:
                color = CPUs[y].history[x]
                gnt.broken_barh([(x, 1)], (8 + y * 10, 4), color=color)
                if writeProcess[color][0] == False and quantumProcess[writeProcess[color][1]] == 0:
                    gnt.annotate(writeProcess[color][1], (x , 10 + 10 * y))
                    quantumProcess[writeProcess[color][1]] = 0
                quantumProcess[writeProcess[color][1]] += 1
                if quantumProcess[writeProcess[color][1]] == quantum:
                    quantumProcess[writeProcess[color][1]] = 0

    plt.savefig("gantt1.png") 
    Image.open("gantt1.png").show()
