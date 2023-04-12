# Why
The reason for using this question is to evaluate how the interviewee might tackle a somewhat larger design problem.  Hopefully, it enables you to discuss implementation choices, or notice some holes in reasoning if they exist.

# Possible Solutions
## Just One (lightly commented) Example
```
# Create databases for account information, who's online, and your responses to actions.
login_info = dict()
users_online = set()
responses= []
# Iterate over each action in actions.
for action in actions:
    # Sign Up Case
    if action[0] == 0:
        # Checks to see if user exists.
        if action[1] in login_info:
            responses.append("Username taken")
        else:
            login_info[action[1]] = action[2]
            responses.append("Success")
    # Sign In Case
    elif action[0] == 1:
        # Checks to see if user exists.
        if action[1] in login_info:
            # Checks to see if password is correct.
            if action[2] == login_info[action[1]]:
                users_online.add(action[1])
                responses.append("Success")
            else:
                responses.append("Password incorrect")
        else:
            responses.append("User doesn't exist")
    # Sign Out Case
    elif action[0] == 2:
        # Checks to see if user is online.
        if action[1] in users_online:
            users_online.remove(action[1])
            responses.append("Success")
        else:
            responses.append("Internal error: user not signed in")
    # Invalid Command Case
    else:
        responses.append("Internal error: not a valid command")
return responses
```


# Things to Ask
## Ask why they use particular data structures for particular applications.
For example, are they considering time complexity that looking through a list for login info would have?  Are they using too much space by introducing redundancy through, say, having one dictionary for username/password combinations but a set for registered usernames?  If they haven't explained why they're doing something a particular way, prod them for it!

## Ask if they've considered security at all.
If they seek certain positions, they may need to consider how secure the data they're working with is.  Ask if they've considered how they plan to protect the data if you run out of time and have nothing else to ask.  That's a valid extension to this prompt!


# Notes on Extensions