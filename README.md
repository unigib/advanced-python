# Advanced Python Assignments

The exercises are organized as separate assignments. Each assignment has its
own Python file so you can work through one concept at a time.

## Assignment 1: Load and explore JSON

[`assignment_01_json_exploration.py`](assignment_01_json_exploration.py) loads
[`data/library.json`](data/library.json) and prints a guided tour of its
structure:

- JSON objects become Python dictionaries, and JSON arrays become lists.
- Dictionaries can be inspected with `.keys()` and accessed by key.
- Lists can be traversed with `for` loops.
- Nested dictionaries and lists can be combined to inspect categories and books.

Run it from the project directory with:

```powershell
python assignment_01_json_exploration.py
```

The script locates its sample JSON file relative to itself, so it can also be
run from another working directory.

### Try it yourself

After running the script, modify it to:

1. Print the total number of books in the top-level categories.
2. Print the ISBN of each book.
3. Find the book titled `Practical JSON` and print its year.
4. Add another category or book to the JSON file and observe how the output
   changes.

This first assignment deliberately walks the category list and one level of
subcategories. Later assignments can build on this data to practice recursion
and lambdas.

## Assignment 2: Recursion or a loop?

[`assignment_02_recursion_vs_loop.py`](assignment_02_recursion_vs_loop.py)
counts all books in the same nested library in two ways:

- `count_books_recursive()` handles a category, then calls itself for that
  category's subcategories.
- `count_books_iterative()` uses a `while` loop and a list as an explicit
  stack of categories still to visit.

Run it with:

```powershell
python assignment_02_recursion_vs_loop.py
```

Both approaches should report the same count. Compare their implementations
and consider:

1. Which version makes the nested structure easier to understand?
2. What extra state does the loop version need to keep track of?
3. What could happen if the nesting were extremely deep?
4. Would you use recursion for a simple fixed repetition, such as counting
   from 1 to 10? Why or why not?

Recursion often fits naturally when each item contains more items with the
same structure, as these categories do. A loop is usually simpler for
straightforward repetition, and the iterative version avoids Python's
recursion-depth limit by managing its own stack. Neither approach is always
better; choose the one that makes the problem clearest while accounting for
the possible depth and size of the data.

## Assignment 3: Lambda callbacks in Tkinter

[`assignment_03_tkinter_lambda.py`](assignment_03_tkinter_lambda.py) creates
buttons that update a message in a small window. Run it with:

```powershell
python assignment_03_tkinter_lambda.py
```

Tkinter's `command` expects a function it can call when the button is clicked.
The greeting function takes an argument, so each greeting button uses a
`lambda` to provide a no-argument callback:

```python
command=lambda: show_greeting("Hello!")
```

The lambda delays the call and supplies `"Hello!"` after the click. In
contrast, `command=show_greeting("Hello!")` calls the function immediately
while the button is being created, rather than waiting for a click. A callback
that takes no arguments, such as `reset_message`, can be passed directly as
`command=reset_message`; it does not need a lambda.

### Try it yourself

1. Add another button that shows a greeting of your choice.
2. Change `show_greeting` so the message includes a name, then use a lambda to
   pass both the greeting and name.
3. Explain why the Reset button can use its function directly, while the
   greeting buttons use lambdas.

Use a regular `def` for reusable or multi-step behavior. A lambda is useful
here as a small adapter between a button's no-argument callback and a function
that needs an argument.

## Assignment 4: Iterating over lists and tuples

[`tuples-lists-1.py`](tuples-lists-1.py) compares the memory size of a small
list and tuple, then creates a large list and tuple and times indexed access
through each one. Run it with:

```powershell
python tuples-lists-1.py
```

The first pair of numbers comes from `sys.getsizeof()`. It reports the size of
the container itself, not the total memory used by the objects it refers to.
The script then measures elapsed nanoseconds for one pass through each
collection using `range(len(...))` and indexing. It repeats each test five
times and prints the average time. This is a comparison of indexed access
inside a loop, not a complete benchmark of every way to iterate.

Treat the timings as an experiment, not a universal result. This script runs
the tuple timing first and the list timing second. Averaging multiple runs can
reduce the effect of one unusually fast or slow run, but it does not remove
all sources of variation or make this a rigorous benchmark. Results can still
vary with the computer, Python version, background activity, and run order.
You can increase `TRIALS` in the script to collect more samples. Also,
creating both collections with 100,000,001 integers can require several
gigabytes of memory; use a much smaller range if your computer does not have
enough available memory.

Lists and tuples both support iteration and indexing. A list is mutable, so
its contents can be changed; a tuple is immutable after creation. Choosing
between them should primarily depend on whether the collection needs to
change, rather than assuming that one will always be faster.

### Think about the results

1. Which collection used less container memory according to the first
   measurements? Does that number include the integer objects?
2. Which indexed loop had the lower average on your computer? How did the
   result change when you increased the number of trials?
3. How might the measurements change if you used `for item in collection`
   instead of indexing with `range(len(collection))`?
4. Why might you choose a tuple even if your timing does not show it to be
   faster?

### Challenge yourself

Try these extensions, using a smaller collection size such as 100,000 or
1,000,000 so the experiments finish in a reasonable time:

1. **Compare iteration styles:** Time both `for item in values` and
   `for i in range(len(values))` for lists and tuples. Make each version
   calculate the same checksum so you know they did equivalent work.
2. **Test different sizes:** Compare several sizes and print a table of the
   list and tuple averages. Does the difference stay the same as the
   collections grow?
3. **Improve the benchmark:** Add a warm-up run, alternate which type is
   measured first, and report the median as well as the average. Explain
   whether the results are more consistent.
4. **Measure referenced objects:** Extend the memory comparison to include
   the objects stored in each collection. How does this differ from the
   shallow size reported by `sys.getsizeof()`?
5. **Explore mutability:** Try changing one item, adding an item, and removing
   an item. Which operations can each type perform directly? What would you
   choose for data that must not change?

## Individual coding challenges

Complete each challenge in its own file. Use the supplied library data for
the first two challenges. Each challenge has a clear result you can check
without relying on execution speed.

### Challenge 1: Query the JSON library

Create `challenge_01_json_query.py`. Load `data/library.json` and ask the user
for an author's name. Print every matching book's title and year, searching
books in categories and subcategories at any depth. The search should ignore
letter case. If there are no matches, print a clear message.

**Check your result:** Searching for `AVERY CHEN` should find two books;
searching for an unknown author should report no matches.

### Challenge 2: Recursively count books

Create `challenge_02_recursive_count.py`. Write a recursive function that
takes a list of categories and returns the total number of books, including
books in all nested subcategories. Do not use a loop-based stack or call the
function from Challenge 1.

**Check your result:** The supplied library should contain five books. Also
check that an empty category list returns zero.

### Challenge 3: Filter with a lambda

Create `challenge_03_lambda_filter.py`. Load the library, collect its books
using your recursive function from Challenge 2 (or copy that function into
this standalone file), then use `filter()` and a `lambda` to find books
published after a year entered by the user. Print each matching title and
year.

**Check your result:** Entering `2021` should find `Python Patterns`,
`Practical JSON`, and `Recursive Clues`. The lambda should perform the year
comparison; do not replace it with a named predicate function.

### Challenge 4: Choose a tuple for fixed data

Create `challenge_04_tuple_memory.py`. Make a list and a tuple containing the
same fixed set of values, compare their shallow sizes with `sys.getsizeof()`,
and explain in a printed message why the tuple may be appropriate when the
data should not change. Use a modest number of values; do not recreate the
hundred-million-item benchmark.

**Check your result:** Confirm that the values are equal, that the list can
be changed, and that attempting to assign to a tuple element raises
`TypeError` (catch it and print an explanation). State that `getsizeof()`
reports the container's shallow size, not the complete memory used by all
referenced objects.
