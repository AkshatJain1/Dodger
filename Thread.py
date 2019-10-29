import threading
from queue import Queue
import time

#ref locking ability of thread module
print_lock  = threading.Lock()

def exampleJob(worker):
    time.sleep(0.5)

    with print_lock:
        print(threading.current_thread().name, worker)

def threader():
    while True:
        worker =  q.get()
        exampleJob(worker)
        q.task_done()

q = Queue()

for x in range(10):
    #def threads and target of threads
    t = threading.Thread(target = threader)

    # die when main thread dies
    t.daemon = True

    #starts thread
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('Entire job took: ',time.time() - start)
