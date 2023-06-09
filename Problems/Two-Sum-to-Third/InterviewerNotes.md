# Why
This question is a favorite because of the fact that it has three separate solutions, and one of the alternative formulations of the question can provide a segway into dynamic programming (an important pattern to know).  It's great to use to try and see how well an interviewee can reason through a problem, as well as consider alternative ways for approaching the problem, while hopefully still being relatively easy to follow.

# Possible Solutions
## Brute Force
The brute force solution is simply to check every element versus every other element.  This has time complexity of O(n<sup>2</sup>), with constant space complexity.  In short, it's a pretty bad solution unless all you care about is space.  Here's the code (written in Python):
```
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == third:
                return True
    return False
```

## Optimal Time Solution
Here, we choose to use a data structure, namely a dictionary in order to reduce our time complexity.  The basic idea is that we store the number of times that we see a given number within the dictionary in one for loop, then check to see if the number is present (more than once in the edge case described below) in a second for loop.  The time complexity is O(n), with space complexity being O(n) as well.

Example code:
```
nums = dict()
# Create lookup table
for x in arr:
    y = third - x
    if y not in nums:
        nums[y] = 0
    nums[y] += 1
# Search Lookup Table
for x in arr:
    if x in nums:
        # check for edge case
        if 2*x != third:
            return True
        # deal with edge case
        elif nums[x] >= 2:
            return True
return False
```
A more succinct version (credit to Victoria Tran for coming up with this one)
```
hashmap = {}
for i in arr:
    answer = third - i
    if answer not in hashmap:
        hashmap[i] = i
    else:
        return True
return False
```


## Balanced Solution
This works on the principal that if I have a sorted list, I can search from both ends to see if my solution is present.  This solution has a time complexity of O(nlogn), while keeping space complexity to O(1).  Doing this allows for a vast improvement on the brute force solution in terms of time complexity without sacrificing spatial complexity.

Example code:
```
sorted_list = sorted(arr)
i = 0
j = len(sorted_list) - 1
while i != j:
    if sorted_list[i] + sorted_list[j] == third:
        return True
    elif sorted_list[i] + sorted_list[j] < third:
        i += 1
    else:
        j -= 1
return False
```

# Things to Ask
## Edge Case
The primary edge case to worry about is double counting.  In particular, bring up two scenarios: arr = [1, 1, 4] and arr = [1, 2, 4] with third = 2 for both.  Often, interviewees might not consider that their solution for the second arr might return True because it's looking at the 1 twice.  Alternatively, in fixing this they might accidentally break their solution such that it can no longer recognize duplicates, as in the first arr, and would return False even though it should return True.

## When they've come up with their first solution
Ask if they can think of other ways to solve the problem, or why they believe their solution to be optimal.

## Hint for Balanced Solution
Usually, you could either mention that it involves sorting or that the time complexity is O(nlogn) which will usually imply that sorting is involved.


# Notes on Other Formulations
## Artibtrary Elements
Interviewee should mention something along the lines of it being far more complex time-wise, as well as that the function signature will change to accomodate having to check n elements.  One possible solution involves recursion, where they essentially iterate over the array and call the function again checking for n-1 element sums, and holding out an element.  Bonus points if they mention (or come up with) a dynamic programming solution.

## Third as an array index
Nothing much changes here actually, you simply query arr[third] at some point towards the beginning of your solution.