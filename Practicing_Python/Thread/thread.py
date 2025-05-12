# Threading 

import threading
import time
from concurrent.futures import ThreadPoolExecutor

# indicates some task being done

def fun(seconds):
  print(f"sleeping for {seconds} seconds")
  time.sleep(seconds)
  
def demo():

  time1=time.perf_counter()
  # fun(2)
  # fun(4)
  # fun(1)

  # same code using thread
  t1=threading.Thread(target=fun,args=[1])
  t2=threading.Thread(target=fun,args=[2])
  t3=threading.Thread(target=fun,args=[2])
  t4=threading.Thread(target=fun,args=[3])

  t1.start() #start the thread
  t2.start()
  t3.start()
  t4.start()

  t1.join()
  t2.join()
  t3.join()
  t4.join()

  # calculating Time
  time2=time.perf_counter()
  print((time2-time1))

def poolingDemo():
  