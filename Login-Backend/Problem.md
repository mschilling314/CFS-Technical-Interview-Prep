# Description
In this problem, you will be given a series of actions taken by theoretical users of a login page.  Your job is to return an array of outputs corresponding to their actions if valid, or that their action is invalid.

# Input
## requests
An array of entries with three transaction types: sign up, sign in, or sign out.  Each entry will have only one type, and each will be formatted as specified below.

### Sign Up
Entries of this type will have the format [0, username, password].  The 0 indicates that this is a sign up attempt.  This is a valid action if the username is not yet taken, otherwise the error message should be "Username taken".

### Sign In
Entries of this type will have the format [1, username, password].  The 1 indicates that this is a sign in attempt.  For the action to be valid, two things must occur in this order, otherwise give the error message specified:
- The username must exist (i.e. in a previous action the user signed up).
    - For a failure of this type, the error message should be "User doesn't exist".
- The password must be correct for the username.
    - For a failure of this type, the error message should be "Password incorrect".

### Sign Out
Entries of this type will have the format [2, username].  The 2 indicates that this is a sign out attempt.  For the action to be valid, the user must be signed in.  If the user is not signed in, the error message should be: "Internal error: user not signed in".

# Output
Your output will be a list of strings, either "Success" if the action at the corresponding input index is successful, or the appropriate error message as specified within the Inputs section.

# Examples
## Example 1
```
requests = [[0, "matt", "password"],
            [1, "matt", "password"],
            [2, "matt"]]

expected_result = ["Success",
                   "Success",
                   "Success"]
```
Explanation:  
The first action is a valid sign up, there are no users so the username can't be taken.  The second action is also valid, as "matt" isn't signed in yet and the password is correct.  The final action is valid because "matt" is signed in.

## Example 2
```
requests = [[1, "matt", "password"],
            [0, "matt", "password"],
            [2, "matt"]]

expected_result = ["User doesn't exist",
                   "Success",
                   "Internal error: user not signed in"]
```
Explanation:  
The first action is a login attempt, but no users have signed up yet, so this is invalid.  The second action is a sign-up attempt, which is valid because no other users have signed up.  The third action is invalid because that user isn't signed in.
