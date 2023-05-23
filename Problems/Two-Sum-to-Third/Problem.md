# Description
In this problem, the goal is to see if there exists a combination of two numbers in an array will sum to a third given number.

# Inputs
## arr
An array of numbers of any length, with the numbers being able to be any real number (though for practical purposes integers only is fine).

## third
A number, which we want to see if the array can produce using some combination of two array entries.

# Outputs
## Boolean
The output should be True if two elements in arr will  sum to third, False otherwise.

# Examples
## Example 1
Inputs: arr = [1, 2, 4], third = 5  
Expected Output: True
## Explanation: 
The first and third elements in arr sum to our third.

## Example 2
Inputs: arr = [1, 2, 6], third = 5  
Expected Output: False
## Explanation: 
None of the combinations will sum to third.

## Example 3
Inputs: arr = [1, 2, 5], third = 5  
Expected Output: False
## Explanation: 
While 5 is present, 0 is not.

## Example 4
Inputs: arr = [1, 2, 4], third = 8  
Expected Output: False
## Explanation: 
This is potentially a corner case, depending on the solution, but ultimately no two elements in arr sum to 8.

# Extensions for Interview Preparation
## Other Solutions
Once you've arrived at one solution, try to find two other solutions.  What are the trade-offs for each?

## Other Formulations
What if we want to be able to select an arbitrary number of elements within the array to check?  Or if third is instead an index within the array, which indicates the third number we want to check to?  How would this change the function or the way we approach the problem?