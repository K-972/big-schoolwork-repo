three_proporties = """A base case: There must be at least one case in the recursion that does not make a recursive call and provides an answer directly.
A recursive case: In the recursive algorithm, the problem is broken down into smaller, similar subproblems.
Convergence towards the base case: Each recursive call should move the problem closer to the base case."""

quest_two = "The purpose of the calc routine is to calculate the sum of all positive integers from 1 to 'n'."

#question three
result = calc(5)
print(result)

#  The output will be 15 since it calculates the sum of integers from 1 to 5.

"""
Advantages and disadvantages of iterative and recursive routines:
Advantages of iterative routines:
They are often more memory-efficient.
They are generally faster and have lower overhead.
They are easier to understand and implement for some problems.
Disadvantages of iterative routines:
They may require more code for certain problems.
They can be less elegant and intuitive for problems that naturally have a recursive structure.
Advantages of recursive routines:
They can be more elegant and intuitive for problems with a recursive structure.
They may require less code for certain problems.
They can simplify complex problems by breaking them into smaller subproblems.
Disadvantages of recursive routines:
They can be less memory-efficient due to the function call stack.
They might be slower and have higher overhead for some problems.
"""

pos   output
0     John
2     Alan
3     Chris
1     Peggy
4     Sue
5     Ken