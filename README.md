\# Student Grade Manager (v1)



This is a simple command line program I made to manage students and their marks. No GUI yet, just plain terminal stuff. I'll probably make a proper GUI version later but for now this works.



\## What it does



\- Add a student

\- Add marks for a student

\- See all students and their marks

\- Calculate a student's average

\- Find who has the highest and lowest average in the class

\- Saves everything to a file so you don't lose data when you close it



\## What you need



\- Python 3 installed on your computer (any recent version should work, I used 3.x)

\- That's literally it, no extra libraries to install



If you're not sure if you have Python, open your terminal/command prompt and type:



```

python3 --version

```



If that gives an error try just `python --version`. If neither works you need to install Python first (just google "install python" and download from python.org).



\## How to run it



1\. Download/clone this repo

2\. Open a terminal in the folder where `grade\_manager.py` is

3\. Run:



```

python3 grade\_manager.py

```



(if `python3` doesn't work try `python grade\_manager.py` instead)



\## How to use it



When you run it you'll see a menu like this:



```

===== Student Grade Manager =====

1\. Add student

2\. Add mark

3\. Show all students

4\. Calculate average for a student

5\. Show highest/lowest scorer

6\. Save and exit

==================================

```



Just type the number of what you want to do and press enter.



\- \*\*Press 1\*\* to add a new student, it'll ask for their name

\- \*\*Press 2\*\* to add a mark, it'll show you the list of students first so you can pick the number of the one you want, then type the mark

\- \*\*Press 3\*\* to just see everyone you've added so far and their marks

\- \*\*Press 4\*\* to get a student's average (pick their number same as before)

\- \*\*Press 5\*\* to see who's top of the class and who's at the bottom (based on average)

\- \*\*Press 6\*\* when you're done, this saves everything and closes the program



Make sure you press 6 to exit instead of just closing the terminal window, otherwise your data won't save.



\## Notes / things to know



\- It saves to a file called `students.txt` in the same folder, don't delete that file or you'll lose your data

\- Marks should be numbers between 0-100 ish but I didn't add strict validation for that yet

\- If you type something invalid at a prompt (like letters where it wants a number) it'll just tell you it's invalid and you have to try again

\- This is the basic version, planning to add a proper GUI in a future version



\## Why I made this



Wanted to practice working with functions, file saving/loading (JSON), and basic program structure in Python before trying to build a GUI version of the same idea. Figured a CLI version first would help me get the logic right before worrying about how it looks.

