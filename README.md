# Summary
This is meant to be used by Northwestern's Chicago Field Studies program in order to allow Student Consultants to conduct practice technical interviews for their peers.  At present, the problems are written in Python, in the future support for other languages might be added.

# How to Use This Repository
## As a CFS Student Consultant
To use this repository as an SC, simply pick a problem.  There will be notes for you to help you get an idea of what to ask, or how to prompt your student, as well as examples of what correct code looks like.

## As an Interviewee
To use this repository as an interviewee, you should ideally download only three files, Problem.md, response.py, and solutions.json.  These files were created with the intent that you could feasibly solve and check your solutions without seeing possible answers.  This will hopefully allow your SC to better guide you, regardless of whether they've got coding experience or not!

When you have what you believe to be a working solution, you should be able to run response.py, which should print out whether the test cases have passed or not.  If they fail, also printed will be the expected value and your output.

# Structure
For now, the structure is basically nonexistent, however, in the future, I plan to structure each problem as its own directory, with essentially a "main" file where students should put their code, which when run will have a feature that allows access of either a JSON file or a generated answer imported from another file within the directory.  Thus will come the other two files within each directory, a "generator" file that will essentially be able to generate input for the function, as well as the expected output based on the problem description, and lastly the JSON file that will contain a pre-generated example.  Lastly, each file will have a README that describes the problem and expected outputs.  Additionally, I'll include a separate .md file with notes on solutions/reasoning/extraneous notes, meant to be utilized by interviewers who either don't have a technical background or just don't have familiarity with the particular problem.  

# Contact
Should anything be broken, or you just have suggestions, feel free to reach out to me at matthewschilling2023@u.northwestern.edu!
