# Description
In this problem, you will be given a list of items represented as a dictionary with two entries:  the item's value and the item's weight.  Additonally you'll be given a number that represents the maximal weight you can put in your knapsack.  To solve the problem, return the maximum value that can be created from the list of items within your weight limit.

# Input
## items
An array of dictionaries with two entries, weight and value.

## sack
The number representing the maximum weight you can carry in your sack.

# Output
Your output will be a singular number, representing the maximum possible value of the knapsack.

# Examples
## Example 1
```
items = [{"weight": 5, "value":6}, {"weight": 6, "value": 1}, {"weight": 5, "value": 10}, {"weight": 1, "value": 1}]

sack = 10

expected_result = 16
```
Explanation:  
The best value can be created by combining the first and third items.  This will reach the maximal weight, while also giving a higher value than any other possible value.

## Example 2
TODO
