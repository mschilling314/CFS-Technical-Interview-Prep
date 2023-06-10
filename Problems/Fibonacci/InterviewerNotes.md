# Why
This question is a favorite because of the fact that it has three separate solutions, and one of the alternative formulations of the question can provide a segway into dynamic programming (an important pattern to know).  It's great to use to try and see how well an interviewee can reason through a problem, as well as consider alternative ways for approaching the problem, while hopefully still being relatively easy to follow.

# Possible Solutions
## Recursive Brute Force
This is the worst solution.  It will work, but will take forever because you're literally going to be solving the same problem over and over again.
```
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```

## Looped Brute Force
This is technically speaking a perfect solution.  That said, I'd encourage the interviewee to keep going to try and consider the dynamic programming approaches to this problem.
```
def fibonacci(n):
    prev = 0
    curr = 1
    for _ in range(2, n+1):
        temp = curr
        curr += prev
        prev = temp
    return curr
```

## Explicit Formula
This uses an explicit formula to calculate the Fibonacci sequence's nth number.  While mathematically it's correct, for large n the interviewee will fail test cases because of computer rounding errors.  Feel free to ask the interviewee about that!  (In particular, ask them why they think they're failing test cases so you don't give away the answer.)

Also worth noting is that they do import a module here, which is generally frowned upon in an assessment setting, but if properly explained (such as benefits of the import) it could work well in showing the depth of a candidate's knowledge on their particular software language.
```
def fibonacci(n):
    import math
    phi = (1 + math.sqrt(5)) / 2
    return round((math.pow(phi, n) - (math.pow(-phi, -n))) / math.sqrt(5))
```

## Top-Down Approach
This adds in a table, allowing there to be fewer recursions than the Recursive Brute Force solution, because rather than keep solving the same sub-problem over and over, you can simply notice that you've already solved the sub-problem, look up the solution, and return without having to resolve the sub-problem's sub-problems.  This is the staple of dynamic programming.
```
TAB = [0, 1]


def fibonacci(n):
    if n < len(TAB):
        return TAB[n]
    TAB.append(fibonacci(n-1) + fibonacci(n-2))
    return TAB[-1]
```


## Bottom-Up Approach
This approach uses a loop rather than recursion.  The table is kind of unnecessary in this approach, see Looped Brute Force.  The reason I included this here is because the table is a useful concept to understand how bottom-up dynamic programming works in general, for questions more complex than simple Fibonacci.
```
def fibonacci(n):
    tab = [0]
    for i in range(1, n+1):
        tab.append(1)
    for i in range(2, n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[-1]
```

## Bottom-Up Approach with Memory Optimization
This approach basically uses the fact that in most dynamic programming problems, you only really care about some previous state and some current state.

Here, that's because to calculate the next Fibonacci number, we just need the previous two, and we can overwrite our previous state with our newly calculated "future" state.
```
def fibonacci(n):
    tab = [0, 1]
    for i in range(0, n):
        tab[i%2] = tab[0] + tab[1]
    return tab[n%2]
```

# Things to Ask
## Memory/Run-time optimization with Approximation
Ask them if there's a way that they can make the program run faster, with less memory, but only arriving at an approximate solution rather than an exact solution.  While that's a bit silly for this particular problem, in other dynamic programs that could actually matter quite a bit.

Note that doing this will not pass test cases, as the answer will be somewhat wrong, but encourage them to reflect on how off it is.  The correct answer here is essentially to use "Buckets", that is to say, rather than adding up all of the Fibonacci numbers, or basically come up with ways to estimate say, every ten Fibonacci numbers instead of actually calculating all ten.  While that doesn't make much sense in this context, for others in dynamic programming such as the knapsack problem, it might make a lot of sense.

# Extensions
## Negative n
For this, I just wanted to have a little fun.  Let them run a bit wild, ask questions as appropriate.

## y-Fibonacci
For this, you'll want to ask them if they need to modify their table, especially pertinent to Bottom-Up with Memory Optimization as a solution.  In fact, it will sort of force people towards that since to do otherwise would either be unweildy or generalize pretty poorly.

## z-Fibonacci
Same as above, just on steroids.
