import queue

a = queue.Queue()
a.put("hello")
a.task_done()
a.get()
