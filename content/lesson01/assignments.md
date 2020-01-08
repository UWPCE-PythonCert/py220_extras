# Assignments
## Working and submitting

We will discuss and explain the assignment completion and submission process during lesson 1.

## Setup steps

The files you need for the assignments in Canvas are obtained by cloning this repo:
https://github.com/UWPCE-PythonCert-ClassRepos/py220_assignments

You should fetch this periodically to ensure you receive any updates.

After cloning, all files will be stored on your local computer. Each week, you will create a new project in which to complete your assignment for that week. The files from the cloned repo will need to be copied from the respective lesson to that week's project.

You will use a tool called pyscaffold to create the project for each
 assignment on your computer. You will complete each assignment commiting to your local repository, and pushing to your own personal github account (not a UW account).

Here's how we create a project (see https://pypi.org/project/PyScaffold/ to learn more):

`pip install pyscaffold`

or

`conda install -c conda-forge pyscaffold
`
Then:

## Creating projects
`putup --no-skeleton project_name`

`python -m venv venv`

`source venv/bin/activate`
`source venv/bin/deactivate`

or on Windows

`venv\scripts\activate`
`venv\scripts\deactivate`


`python setup.py develop`


2: pytest and coverage

`pip install pytest`

`pip install pytest-cov`

3: mocks

`pip install pytest-mock`

## Submitting your work

To submit your work you will upload a zip file to canvas, containing all your work.

The process is really simple, represents how we work on projects, and will allow you to focus on Python development. And at the end of class you will have a portfolio of your work to share as you chose.

Be sure to follow along again on the lesson 1 video if you need help.

On this course you can chose to do the assignments described in canvas, or for certain lessons you may do an alternative assignment instead of the canvas one, or in addition to it.
