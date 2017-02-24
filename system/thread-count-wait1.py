#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# import _thread as thread
import thread

TOTAL_THREAD = 10
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(TOTAL_THREAD)]


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
        # 如果发生异常，则程序就不会结束
        # if myId == 2 and i == 4:
        #     raise Exception('exception on thread!')
    exitmutexes[myId].acquire()

for i in range(TOTAL_THREAD):
    thread.start_new_thread(counter, (i, TOTAL_THREAD))

for mutex in exitmutexes:
    while not mutex.locked():
        pass

print('Main thread exiting.')
