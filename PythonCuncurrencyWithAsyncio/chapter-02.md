📘 Chapter 2: *Asyncio Basics* 🚀

Chapter 2 delves into the foundational aspects of asyncio in Python, focusing on how it enables single-threaded concurrency using coroutines, tasks, and event loops. Here’s a breakdown:


🌀 2.1 **Introducing Coroutines**
- **Coroutines** are special Python functions that can pause and resume execution when encountering a potentially long-running task. 
- When a coroutine pauses to wait for an operation, other tasks can run concurrently, providing concurrency. 💡
- **`async` and `await`** are the two essential keywords:
  - `async` defines a function as a coroutine.
  - `await` pauses the coroutine until a result is available from an asynchronous operation.

⚙️ Example of Creating a Coroutine
```python
async def my_coroutine() -> None:
    print("Hello world!")
```
This is similar to a normal Python function but can pause its execution.


⏳ 2.2 **Introducing Long-Running Coroutines with `sleep`**
- Asyncio’s `sleep` function allows us to pause execution, simulating real-world, long-running operations like web requests or database queries 🌐.
- When `await asyncio.sleep()` is called, other tasks can be executed during the pause.

⚙️ Example of Using `asyncio.sleep`
```python
async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return "Hello World!"
```
This coroutine pauses for 1 second before returning "Hello World!". During that second, other coroutines can run concurrently.


🔄 2.3 **Running Concurrently with Tasks**
- A **task** is a wrapper around a coroutine that schedules it to run on the event loop 🕑.
- Tasks allow coroutines to be run concurrently, as they don’t block the event loop, unlike `await`, which pauses until a result is returned.

⚙️ Example of Creating a Task
```python
import asyncio
from util import delay

async def main():
    task = asyncio.create_task(delay(3))
    await task
```
Here, the task `delay(3)` runs concurrently, while other code can execute.


⛔ 2.4 **Canceling Tasks and Setting Timeouts**
- Tasks can be canceled using `task.cancel()`, raising a `CancelledError` within the task. If a task is taking too long, we can also set timeouts using `asyncio.wait_for` 🕒.

⚙️ Example of Cancelling a Task
```python
async def cancel_task(task):
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")
```


💼 2.5 **Tasks, Coroutines, Futures, and Awaitables**
- **Futures** represent a value that will be available in the future but might not exist yet. They are used internally in asyncio and can be awaited 🎯.
- Coroutines and tasks can both be used in `await` expressions.

⚙️ Example of Working with Futures
```python
from asyncio import Future

my_future = Future()
my_future.set_result(42)
print(my_future.result())  # Outputs: 42
```


⏱️ 2.6 **Measuring Coroutine Execution Time with Decorators**
- By using decorators, we can measure the execution time of coroutines for performance analysis. ⌛


⚠️ 2.7 **Pitfalls of Coroutines and Tasks**
- Be cautious with CPU-bound code inside coroutines, as it will block the event loop.
- Avoid using blocking I/O APIs; use asyncio-compatible libraries to ensure the event loop runs smoothly 🛠️.


🔧 2.8 **Accessing and Manually Managing the Event Loop**
- You can access the event loop directly using `asyncio.get_event_loop()`, though `asyncio.run()` is recommended for running main coroutines.


🛠️ 2.9 **Using Debug Mode**
- Debug mode helps in identifying long-running coroutines or tasks that block the event loop 🧐. You can enable it with:
```bash
python3 -X dev program.py
```
Or by setting the `PYTHONASYNCIODEBUG` environment variable.

⚙️ Example of Running in Debug Mode
```python
asyncio.run(main(), debug=True)
```

#PythonConcurrencyWithAsyncio
#Chapter_02
#Notes #Book