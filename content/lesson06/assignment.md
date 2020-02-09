# Lesson 6 Assignment

You have received a support request to fix a Python program that is performing poorly.

Ever since it was implemented it has taken at least 5-10 minutes to run, and often a lot longer.

Lately it has been receiving more use than ever, and users are experiencing increased run times. Some say that's because of the increased usage. Others say it's because the program is being asked to do more work in each run.

Your job is to diagnose and fix the poor performance. And you will need to use an evidence-based approach, using timing, profiling, and any other tools you may need. You will need to document this as you go, and submit this documentation with your assignment.

All code is in lesson06_assignment in this repo.

## Important constraints
Many, many teams use this program. So many in fact, that no-one knows who uses it. This means that you must not change the way the program is called in any way at all, so that you don't break dependencies.

Unfortunately, this includes the csv files that the program creates, as some people use these without running the program at all.

## What you must do
1. For the first part of this assignment you must only use poor_pref.py and any code you may chose to write.
1. Run the poor_pref.py program, and study it. It may take quite a while to run!
1. Document how long it takes in its current form.
1. Identify which parts of the program are a problem and will need speeding up. Provide evidence that shows why these parts are the problem.
1. Develop a strategy to improve the program (what code changes will you make, and how will you prove that they are successful).
1. Make the changes, and demonstrate the impact you have made by showing before and after performance figures. Hopefully you will be able to make this program run significantly faster than is does now. BUT REMEMER that you cannot change the way the calc function is called, and you can not change the names or content of the csv files.

## Part 2
1. In the lunch room, you are telling your coworkers about how you managed to improve the performance of calc significantly. Alice, a long time and experienced developer tells you that she has also worked on calc, and improved performance such with default parameters calc runs in well under one second. She claims she did this by adding only two lines to poor_perf.py
1. Study alice_ut.py and try to understand what it does.
1. Alice also provided alice.py which is the same as poor_perf.py for now. Identify and implement in alice.py the two changes you think she made, based on what you see in alice_ut.py.
1. Show evidence of the performance you are able to obtain. Explain why this works.

## Part 3
1. If you could rewrite the API for calc, how would you do this, and re-implement the code.
1. Submit new_perf.py that shows this, along with evidence of the performance improvements you made.


# Your submission
All code should score at least 9/10 when linted. Include tests if you wish. Provide a document that describes the before and after performance as described above for all 3 parts.

