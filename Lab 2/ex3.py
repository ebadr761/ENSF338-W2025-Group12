import cProfile
import timeit

#sub function that calculates the factorial of n
def sub_function(n):
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

# third function that calculates the square of the numbers from 0 to 999
def third_function():
    return [i**2 for i in range(100000000)]
test_function()
third_function()

#QUESTION 1. 
# A profiler determines how long and how often various parts of a program is run, which is gathered to stats.

#QUESTION 2. 
#   Profiling differs from benchmarking in that benchmarking is a measure of a system's overall performance,
#   similar to how timeit module works. Profiling is different, in that it measures how long it takes and how
#   often various parts of the program runs so profiling is more specific, for finding out how many
#   resources your program consumes at a certain area of the code and exactly where it spends the most time.

#QUESTION 3. 
# Use a profiler to measure execution time of the program (skip function definitions)
cProfile.run('sub_function')
cProfile.run('test_function()')
cProfile.run('third_function()')

#QUESTION 4. Discuss a sample output. Where does execution time go? 
#   The execution time says that there were 4 function calls for the third_function() and it ran in 4.11 seconds,
#   compared to the test_function which had many calls but ran in 0.000 seconds.

#   This sample output shows that the vast majority of the time is spent on the third_function, and not the
#   sub_function or the test_function.
