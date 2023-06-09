# Why
The reason for using this question is to test the interviewee for knowledge on how to perform dynamic programming.  This is not an easy problem by any stretch of the imagination, and should not be treated as such.  Test to see how they design as well, a good approach might be to start with basic recursion, then add a table to catch redundant cases of execution.  There are also a few optimizations that can be performed.


# Possible Solutions
## Brute-Force Recursion
```
def knapsack
    if len(items) == 1:
        if items[0]["weight"] < sack:
            return items[0]["value"]
        else:
            return 0
    if items[0]["weight"] > sack:
        return knapsack(items[1:], sack)
    return max(knapsack(items[1:], sack), items[0]["value"] + knapsack(items[1:], sack-items[0]["weight"]))
```

## Top-Down


## Bottom-Up


## Optimized Table Bottom-Up


## Bucket Top-Down


## Bucket Bottom-Up



# Things to Ask
## Ask about bottom-up versus top-down approaches.
Basically, what this boils down to is that in top-down, they still recurse, but they also pass in a table that holds the optimal solution to specific states for earlier recursive termination.  Bottom-up on the other hand is loop based, and builds out the table intentionally as the program runs.

If they get stuck, one way to offer help is to state that such a table would have states where you consider the index of the item you're considering and the maximum value you've found so far at that index.

## Ask about approximating instead of exact solutions.
Note that the table takes up at least O(n) memory space.  There are two optimizations that can be performed:
1. In the bottom-up approach, you can get away with the table only having two rows, essentially representing the current and previous states.
2. In either approach, instead of exact calculations, you can essentially create "buckets" where, for example, weight and value are rounded to different numbers to reduce the number of entries the table needs.  In this case, the solution will not actually be exact (100% correct), but the memory and runtime savings should be pretty drastic which is why this is often justified.

# Notes on Extensions