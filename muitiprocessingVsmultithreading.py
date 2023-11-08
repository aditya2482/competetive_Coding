import multiprocessing
# import threading

shared_value = []

def sq(array,shared_value):
    for idx,n in enumerate(array):
        shared_value[idx] = n*n
        print(f"{n}:{n*n}")
    # print(shared_value)
    return shared_value


# shared variable cant be accessed by tarditional methods, need to run iterator and enumerate function to work on it
def cub(array,shared_var):
    ans_cub = []
    for idx,n in enumerate(array):
        shared_var[idx]= n*n*n
    return shared_var

# daemon thread - Once you have created a daemon thread, it will start running in the background. The thread will not block the main program, and it will terminate automatically when the main thread exits.
# Daemon threads can be useful for a variety of tasks. For example, you could use a daemon thread to:
# Download files in the background
# Process data in the background
# Perform other tasks that are not critical to the main program 
# ie - process args, daemon = True

# ' d - double integer, i - integer

if __name__ == '__main__':
    multiprocessing.freeze_support()
    array = [1,23,4,5,6,10000000000000000000000990009900000]

    shared_value = multiprocessing.Array('i',6)
    shared_var = multiprocessing.Array('i',6)

    process1 = multiprocessing.Process(target=sq,args = (array,shared_value),daemon=True)
    process2 = multiprocessing.Process(target= cub,args = (array,shared_var),daemon=True)
    print("hello-world")

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print(shared_value[:])
    print(shared_var[:])
    
# print(ans)