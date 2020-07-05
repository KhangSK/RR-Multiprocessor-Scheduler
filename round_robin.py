from taskclass import Task
from input_reader import read_input
from circular_queue import CircularQueue

class CPU:
    def __init__(self, cpuname):
        self.cpuname = cpuname
        self.history = []
        self.currentproc = None
        self.time_elapsed = 0

    def exec(self, ready_q, wait_q, finish_proc_list, quantum):
        # get proc from ready q
        if self.currentproc is None:
            if not ready_q.empty():
                self.currentproc = ready_q.dequeue()
            else:
                # if ready q is empty, refill with wait q
                #transfer_q(wait_q, ready_q)
                # if both are empty, this timeslice the cpu is idle
                #if ready_q.empty():
                self.history.append(None)
                return False

        self.time_elapsed += 1
        self.currentproc.runtime -= 1
        self.history.append(self.currentproc.color)

        if self.time_elapsed == quantum or self.currentproc.runtime == 0:
            if self.currentproc.runtime == 0:
                finish_proc_list.append(self.currentproc)
                self.currentproc = None
                self.time_elapsed = 0
            else:

                wait_q.enqueue(self.currentproc)
                self.currentproc = None
                self.time_elapsed = 0
        
        return True

    def __str__(self):
        return self.cpuname

    def working(self):
        return self.currentproc is not None



def rr(CPUs, numProcessor, proclist, finish_proc_list, quantum):
    # initial time
    time = 0

    # create cpus timeline
    for i in range(numProcessor):
        CPUs.append(CPU("CPU " + str(i+1)))

    ready_q = CircularQueue()
    wait_q = CircularQueue()

    while True:
        while len(proclist) != 0 and proclist[0].arrival_time == time:
            task = proclist.pop(0)
            ready_q.enqueue(task)

        for cpu in CPUs:
            cpu.exec(ready_q, wait_q, finish_proc_list, quantum)

        w_inc(ready_q)
        #if ready_q.empty():
        transfer_q(wait_q, ready_q)

        time += 1

        cpu_not_working = all([not cpu.working() for cpu in CPUs])
        # to finish working, all queue must be empty and no cpu is working 
        if ready_q.empty() and wait_q.empty() and len(proclist) == 0 and cpu_not_working:
            print("All processes executed!")
            break

    return time
        
def transfer_q(qfrom, qto):
    while not qfrom.empty():
        qto.enqueue(qfrom.dequeue())

def w_inc(q):
    q.w_inc()