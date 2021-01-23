from slave import Slave

import datetime

class SlavePool:
    def __init__(self, slaves):
        self.total_workers = slaves
        self.slaves_available = []
        self.slaves_unavailable = []
        self.request_log = []
        for x in range(slaves):
            self.slaves_available.append(Slave("ip" + str(x + 1), "192.168.0.10" + str(x + 1)))

    def request_slaves(self, slaves, duration):
        now = datetime.datetime.now()
        full_time = now + datetime.timedelta(seconds=duration)
        current_time_st = now.strftime("%H:%M:%S")
        full_time_st = full_time.strftime("%H:%M:%S")
        print("i have available slaves " + str(self.available_workers()))
        if self.available_workers() >= slaves:
            self.request_log.append(full_time)
            return self.manage_request(slaves, duration)
        else:
            print("i don't have slaves please come back ") # return the time to coma back
            for time in self.request_log:
                if time < now:
                    self.request_log.remove(time)
                elif time >= now:
                    comeback = time-now
                    comeback_st_array = str(comeback).split(':')
                    print(comeback_st_array[2])
                    return {'slaves': '[]', 'come back': comeback_st_array[2]}
            return {'slaves': '[]', 'come back': 'try again'}

    def manage_request(self, slaves, duration):
        ans = []
        for x in range(slaves):
            slave = self.slaves_available.pop()
            self.slaves_unavailable.append(slave)
            print(slave.tostring())#return the slave string
            ans.append(slave.name)
            slave.working_time(duration)
        return {'slaves': ans}

    def available_workers(self):
        for worker in self.slaves_unavailable:
            if not worker.isWorking:
                slave = worker
                self.slaves_unavailable.remove(worker)
                self.slaves_available.append(slave)
        for worker in self.slaves_available:
            if worker.isWorking:
                slave = worker
                self.slaves_available.remove(worker)
                self.slaves_unavailable.append(slave)
        return self.slaves_available.__len__()

    def tostring(self):
        print("The Array is: ")
        for worker in self.slaves_available:
            print(worker.name, worker.ip, worker.isWorking)
        for worker in self.slaves_unavailable:
            print(worker.name, worker.ip, worker.isWorking)

