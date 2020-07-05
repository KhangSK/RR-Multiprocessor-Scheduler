from circular_queue import CircularQueue
from taskclass import Task
from input_reader import read_input
from round_robin import rr, CPU
from draw_gantt import draw_gantt
import sys

def run(filename, quantum):
    proclist = []
    (ncpu, nprocs) = read_input(filename, proclist)
    total_wait_time = 0
    total_turnaround_time = 0

    for proc in proclist:
        total_turnaround_time += proc.runtime

    CPUs = []
    finish = []
    proclist1 = proclist.copy()
    time = rr(CPUs, ncpu, proclist1, finish, quantum)
    draw_gantt(CPUs, time, proclist, quantum)

    print("Whole exeution time: ", time)

    for proc in finish:
        total_wait_time += proc.wait_time
        total_turnaround_time += proc.wait_time

    avg_wait_time = total_wait_time / nprocs
    avg_turnaround_time = total_turnaround_time / nprocs

    print("Average wait time: ", avg_wait_time)
    print("Average turnaround time: ", avg_turnaround_time)

run(sys.argv[1], int(sys.argv[2]))