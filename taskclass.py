class Task():
    def __init__(self, proc_name, arrival_time, runtime, color):
        self.proc_name = proc_name
        self.arrival_time = arrival_time
        self.runtime = runtime
        self.wait_time = 0
        self.color = color

    def __eq__(self, other):
        return self.runtime == other.runtime

    def __lt__(self, other):
        return self.runtime < other.runtime
    
    def __gt__(self, other):
        return self.runtime > other.runtime
    
    def __str__(self):
        return str(self.proc_name)

    def w_inc(self):
        self.wait_time += 1