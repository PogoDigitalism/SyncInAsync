# SyncInAsync

## Call synchronous functions in asynchronous coroutines without blocking the event loop! ☑️
Especially useful for asynchronous libraries like FastAPI, Discord.py etc.


## HOW IT WORKS:
1. SyncInAsync creates a ThreadPoolExecutor (or uses a passed one) to execute these synchronous functions in seperate threads. It also takes the running event loop.
2. This execution happens through Async IO's run_in_executor.
3. run_in_executor returns a Future object which is then used to return the Future's result.
4. This result is the result of your synchronous function!
