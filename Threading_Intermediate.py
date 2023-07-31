from threading import Thread, Lock, current_thread
import os
import time
from queue import Queue

#def square_numbers():
    #for i in range(100):
        #i*i
        #time.sleep(0.1)


#threads = []
#num_threads = 10

#Create threads
#for i in range(num_threads):
    #t = Thread(target=square_numbers)
    #threads.append(t)

#start
#for t in threads:
    #t.start()

#join
#for t in threads:
    #t.join()

#print("end main")

database_value = 0

def increase(lock):
    global database_value
    lock.acquire()
    local_copy = database_value
    #processing
    local_copy +=1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()
#Always release your lock
#Another way to do it is to use "with lock():"
#The lock function is used to prevent race condition

if __name__ == "__main__":
    print("start value", database_value)
    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
#The join function blocks till all the threads have been processed

    print("end value", database_value)

    #print("end main")

def worker(q, lock):
    while True:
        value = q.get()
        #Processing
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()

if __name__ == "__main__":
    q = Queue()

    #q.put(1)
    #q.put(2)
    #q.put(3)

    # 3 2 1 --->
    #first = q.get(1)
    #print(first)

    #q.task_done()
    #q.join()
#Always end with task done

    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True
        #The daemon thread is a thread that dies when the main threads die
        #We use the daemon thread because of the while loop
        thread.start()

    for i in range(1,21):
        q.put(i)
    
    q.join()
    print("end main")