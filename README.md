# Summary
This is meant to be used by Northwestern's Chicago Field Studies program in order to allow Student Consultants to conduct practice technical interviews for their peers.  At present, the problems are written in Python, in the future support for other languages might be added.

# How to Use This Repository
## As a CFS Student Consultant
To use this repository as an SC, simply pick a problem.  There will be notes for you to help you get an idea of what to ask, or how to prompt your student, as well as examples of what correct code looks like.

To actually conduct the interview, pick as many questions as time allows (a good guideline is to give about 15 minutes per question).  When it's time to interview, provide your interviewee with a link to this repository, and tell them to fork the repository and clone it to their device, then screen-share with you as they open it in their favorite text editor or IDE.  If they don't use an IDE, they will need to run the response.py script from a terminal, which I don't recommend.  

They should (hopefully) know what this means, Git is a huge part of the software engineering industry and everyone uses an IDE such as Visual Studio Code, so there shouldn't be too many issues with setup (though I need to conduct some user testing to be certain, sorry).

## As an Interviewee
To use this repository as an interviewee, you should fork and then clone the repository onto your computer.  DO NOT OPEN InterviewerNotes.md FROM ANY DIRECTORY!!!!

Your SC will select a problem that should correspond to one of the directories.  You'll want to open Problem.md and response.py, you'll see an empty function for you to fill out with a pass statement in it.

When you have what you believe to be a working solution, you should be able to run response.py, which should print out whether the test cases have passed or not.  If they fail, also printed will be the expected value and your output.

# Structure
For now, the structure is basically nonexistent, however, in the future, I plan to structure each problem as its own directory, with essentially a "main" file where students should put their code, which when run will have a feature that allows access of either a JSON file or a generated answer imported from another file within the directory.  Thus will come the other two files within each directory, a "generator" file that will essentially be able to generate input for the function, as well as the expected output based on the problem description, and lastly the JSON file that will contain a pre-generated example.  Lastly, each file will have a README that describes the problem and expected outputs.  Additionally, I'll include a separate .md file with notes on solutions/reasoning/extraneous notes, meant to be utilized by interviewers who either don't have a technical background or just don't have familiarity with the particular problem.  

# Contact
Should anything be broken, or you just have suggestions, feel free to reach out to me at matthewschilling2023@u.northwestern.edu!
