import threading

created_timers = []

def cancel_timers():
    #print("Canceling")
    for timer in created_timers:
        timer.cancel()

class MockTimer(threading.Timer):
    def __init__(self, interval, target, args=None, kwargs=None):
        #print("MockTimer __init__")
        created_timers.append(self)
        super().__init__(interval, target, args, kwargs)

    def start(self):
        #print("MockTimer start {}".format(self.args))
        super().start()
    
    def cancel(self):
        #print("MockTimer cancel {}".format(self.args))
        super().cancel()