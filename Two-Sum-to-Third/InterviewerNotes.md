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