from multiprocessing import Process, Value, Array, Lock, Pool
from multiprocessing import Queue
import os
import time

#The Queue is a linear data structure that follows the first in first out principle

def square_numbers():
    for i in range(1000):
        i*i

#if __name__ == "__main__":
    #processes = []
    #num_processes = os.cpu_count()
    #number of CPUs on the machine. Usually a good choice for the number of processes
    
    #create processes and asign a function for each process
    #for i in range(num_processes):
        #process = Process(target=square_numbers)
        #processes.append(process)

    #start all the processes
    #for process in processes:
        #process.start()

    #wait for all processes to finish
    #block the main program until the processes are finished
    #for process in processes:
        #process.join()  

#def add_100(number,lock):
        #for i in range(100):
            #time.sleep(0.01)
            #with lock:
                #number.value += 1


#if __name__ == "__main__":
    #lock = Lock()
    #shared_number = Value("i", 0)
    #print("Number at beginning is", shared_number.value)

    #p1 = Process(target=add_100, args=(shared_number,lock))
    #p2 = Process(target=add_100, args=(shared_number,lock))

    #p1.start()
    #p2.start()

    #p1.join()
    #p2.join()

    #print("number at end is", shared_number.value)

def add_100(numbers,lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

#if __name__ == "__main__":
    #lock = Lock()
    #shared_array = Array('d', [0.0, 100.0, 200.0])
    #print("array at the begining is", shared_array[:])

    #p1 = Process(target=add_100, args=(shared_array,lock))
    #p2 = Process(target=add_100, args=(shared_array,lock))

    #p1.start()
    #p2.start()

    #p1.join()
    #p2.join()

    #print("array at the begining is", shared_array[:])


def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

#if __name__ == "__main__":

    #q = Queue()
    #numbers = range(1,6)

    #p1 = Process(target=square, args=(numbers, q))
    #p2 = Process(target=make_negative, args=(numbers, q))

    #p1.start()
    #p2.start()

    #p1.join()
    #p2.join()

    #while not q.empty():
        #print(q.get())

def cube(numbers):
    return numbers * numbers * numbers 


if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()


    #map, apply, join, close
    result = pool.map(cube, numbers)
    #pool.apply(cube, numbers[0])
    #This is used to apply the function on a selected element


    pool.close()
    pool.join()

    print(result)
