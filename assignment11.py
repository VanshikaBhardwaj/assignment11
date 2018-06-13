import thread
import time
#1
def fun(t):
    time.sleep(5)
    print("I have woken up!")    
try:
    thread.start_new_thread(fun,("t1",))
except:
    print("ERROR IN MAKING THREAD!")

#2
def number(t):
    for i in range (1,11):
        print(i)
        time.sleep(1)
try:
    thread.start_new_thread(number,("count_thread",))
except:
    print("ERROR IN MAKING THREAD!")

#3
def prin(t1,expDelay):
    a=[12,3,21,4,54]
    for i in a:
        print(i)
        time.sleep(expDelay)
        expDelay=expDelay*2
try:
    thread.start_new_thread(prin,("thread",2))
except:
    print("ERROR IN MAKING THREAD!")

#4
def fact(t,n):
   fac=1
   for i in range(1,n+1):
       fac*=i
   print(fac)
try:
    thread.start_new_thread(fact,("thread",5))
except:
    print("ERROR IN MAKING THREAD!")