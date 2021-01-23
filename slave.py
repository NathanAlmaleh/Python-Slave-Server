import time
import threading

'#slave class contains a slave with the name ip and working status'


class Slave:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.isWorking = False

    def thread_function(self, duration):
        self.isWorking = True
        time.sleep(duration)
        self.isWorking = False

    def working_time(self, duration):
        #print("worker function: " + self.name + " for: " + str(duration))
        work = threading.Thread(target=self.thread_function, args=(duration,))
        work.start()

    def is_working(self):
        return self.isWorking

    def tostring(self):
        return self.name + " " + self.ip+" status working: " + str(self.isWorking)
