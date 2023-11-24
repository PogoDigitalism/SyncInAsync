# SyncInAsync

## Call synchronous functions in asynchronous coroutines without blocking the event loop! ☑️
Especially useful for asynchronous libraries like FastAPI, Discord.py etc.


## HOW IT WORKS:
1. SyncInAsync creates a ThreadPoolExecutor (or uses a passed one) to execute these synchronous functions in seperate threads. It also takes the running event loop.
2. This execution happens through Async IO's run_in_executor.
3. run_in_executor returns a Future object which is then used to return the Future's result.
4. This result is the result of your synchronous function!


⚠️Try to prevent too many threads running concurrently: 
*If max_workers is None or not given, it will default to the number of processors on the machine, multiplied by 5, assuming that ThreadPoolExecutor is often used to overlap I/O instead of CPU work and the number of workers should be higher than the number of workers for ProcessPoolExecutor.* [concurrent.futures docs](https://docs.python.org/3/library/concurrent.futures.html)
