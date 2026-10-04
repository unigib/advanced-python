import sys
import time
from collections.abc import Sequence

# A list is mutable; a tuple is immutable after it has been created.
a = []
b = ()

# Both can hold the same values, but their container sizes may differ.
a = ["Students", "For", "Students"]
b = ("Students", "For", "Students")

# getsizeof reports the container's shallow size; it does not add the sizes
# of the objects referenced by the container.
print(sys.getsizeof(a))
print(sys.getsizeof(b))


# Timing experiment: this compares indexed access in a loop, not every form
# of iteration or overall performance in all situations.

# Caution: 100,000,001 integers in both collections can use several GB of
# memory. Reduce this number if your computer does not have enough RAM.
a = list(range(100000001))
b = tuple(range(100000001))

def average_indexing_time(values: Sequence[int], trials: int) -> float:
    """Return the average nanoseconds for one indexed pass over values."""
    elapsed_times = []

    for _ in range(trials):
        start = time.perf_counter_ns()
        for i in range(len(values)):
            x = values[i]
        elapsed_times.append(time.perf_counter_ns() - start)

    return sum(elapsed_times) / trials


# Repeat each test and compare the averages rather than relying on one run.
# Increase TRIALS to collect more samples; timings still vary with the machine,
# Python version, background activity, and which collection runs first.
TRIALS = 5
tuple_average = average_indexing_time(b, TRIALS)
list_average = average_indexing_time(a, TRIALS)

print(f"Tuple average over {TRIALS} runs: {tuple_average:.0f} ns")
print(f"List average over {TRIALS} runs: {list_average:.0f} ns")

