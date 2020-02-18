import threading
import time


# create a mutable object that is shared among threads
class Shared:
    val = 1


def func():
    y = Shared.val
    time.sleep(0.00001)
    y += 1
    Shared.val = y


threads = []
# with enough threads, there's sufficient overhead to
# cause a race condition
for i in range(100):
    thread = threading.Thread(target=func)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(Shared.val)
