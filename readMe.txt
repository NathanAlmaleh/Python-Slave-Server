Created by Nathan Almaleh 23/01/2021

Slave Server:
A Server on localhost port 8080
manages get request with amount of slaves and duration time
and returns slave as a JSON if it has available slaves otherwise return the time to wait for the request.

Classes:
    main --> Server initialize with Pool

    pool --> Manage requests and returning slaves/comeBack
                self.total_workers =  how many slaves this server has
                self.slaves_available = stack containing all the available slaves
                self.slaves_unavailable = stack containing all unavailable slaves
                self.request_log = stack containing all the time request

    slave --> Slave object with ip, name, sleep methode
                self.name = name of the slave
                self.ip = ip of the slave
                self.isWorking = Bool status working yes or not