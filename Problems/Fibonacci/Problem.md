# Description
In this problem, the goal is to calculate the nth Fibonacci number, where Fibonacci[0] = 0 and Fibonacci[1] = 1.  In case you're unfamiliar with Fibonacci numbers, the recursive formula for them is:
Fibonacci[x] = Fibonacci[x-1] + Fibonacci[x-2]

# Inputs
## n
How far into the sequence we want to go, will always be zero or greater.

# Outputs
## Integer
The nth Fibonacci number.

# Examples
## Example 1
Inputs: n = 5
Expected Output: 5
## Explanation: 
F[5] = F[3] + F[4] = F[1] + F[2] + F[2] + F[3] = 1 + F[1] + F[0] + F[1] + F[0] + F[1] + F[2] = 4 + F[0] + F[1] = 5

# Extensions for Interview Preparation
## Other Solutions
Once you've arrived at one solution, try to find other solutions.  What are the trade-offs for each?

## Other Formulations

### Negative n
Notice that in our formulation, we simply add the last two numbers in the sequence to get the next number.  Therefore, by that logic:
Fibonacci[x-2] = Fibonacci[x] - Fibonacci[x-1]

Modify your code to deal with the possibility that n will be less than zero, you may need to use helper functions for this but bonus points if you manage to do it with one generalized algorithm.

### Modified Definition: y-Fibonacci
Now suppose we want to generalize a bit.  Let's suppose that, for the first y terms in our new sequence, we have:
S[0] = 0
S[1] = 1
S[x] = sum(S[i] for i in range(0, x)) for all x < y

That is, supposing y=5:
S[2] = 1
S[3] = 2
S[4] = 4

Then, for any terms of S[n] where n >= y, we calculate S as follows:
S[n] = sum(S[n-i] for i in range(1, y+1))

That is, again supposing y=5, that:
y[5] = 8
y[6] = 16
y[7] = 31
and so on.  Note that y=2 is the Fibonacci sequence.

### Modified Definition: z-Fibonacci
We'll define z-Fibonacci as being the sum of all y-Fibonacci series up to z.  How will this impact how you write your code?