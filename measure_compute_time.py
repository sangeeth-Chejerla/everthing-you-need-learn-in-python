import time

# Start time
start_time = time.perf_counter()

# your function call
# (replace any_function() with the actual function call you want to measure)
any_function()

# End time
end_time = time.perf_counter()

# Calculate and print the elapsed time
print("Elapsed time:", end_time - start_time, "seconds")
