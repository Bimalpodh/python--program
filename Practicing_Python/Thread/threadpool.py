# 🔥 What is ThreadPoolExecutor?
# A ThreadPoolExecutor is a high-level way to manage multiple threads.
# You don't manually create threads.
# You "submit" tasks to a pool, and it automatically assigns free threads.
# Main Module:
# from concurrent.futures import ThreadPoolExecutor

# 🎉 Why Use ThreadPool?
# Automatic management of threads.
# Reduces memory and CPU overhead.
# Makes parallel execution super easy.
# Best for I/O bound tasks (API calls, file operations).

# 🔹 Basic Methods

# Purpose                                       # Method                                  
# submit(func, *args)                 # Submit a single function with arguments
# map(func, iterable)                 # Submit a list of tasks
# shutdown(wait=True)                 # Close the pool gracefully
# add_done_callback(fn)               # Add function to call after task finishes





from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, [1, 2, 3, 4, 5])
    for r in results:
        print(r)
