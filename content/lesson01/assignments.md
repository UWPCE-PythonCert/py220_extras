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

# Assignments

We will discuss and explain the assignment completion and submission process during lesson 1.

## Setup steps

The files you need for the assignments in Canvas are obtained by cloning this repo:
https://github.com/UWPCE-PythonCert-ClassRepos/py220_assignments

You should fetch this periodically to ensure you receive any updates.

After cloning, all files will be stored on your local computer. Each week, you will create a new project in which to complete your assignment for that week. The files from the cloned repo will need to be copied from the respective lesson to that week's project.

You will use a tool called pyscaffold to create the project for each
 assignment on your computer. You will complete each assignment commiting to your local repository, and pushing to your own personal github account (not a UW account).

Here's how we create a project (see https://pypi.org/project/PyScaffold/ to learn more):

## First time only

`pip install pyscaffold`

or (if using anaconda / spyder)

```
conda activate base
conda install -c conda-forge pyscaffold
```

## Creating projects (every project)
```
putup --no-skeleton lesson01
cd lesson01
```

For python on Mac / Linux:

```
python -m venv venv
source venv/bin/activate
```

For python on Windows:

```
python -m venv venv
venv\scripts\activate
```

OR for anaconda (same on Mac, Linux, and Windows):

```
conda create -n lesson01 python=3.7
conda activate lesson01
```


Then, on all:

`python setup.py develop`


For python:

```
pip install pytest
pip install pytest-cov
````

For anaconda:
```
conda install pytest
conda install pytest-cov
```

For mocks

`pip install pytest-mock` or `conda install pytest-mock`


## Now launch your IDE
If using Spyder, use anaconda-navigator to select the lesson01 (or whatever)
virtual environment. Then upgrade, install and launch spyder (using the navigator icon)

You can also load psyder from the terminal:
```
conda activate lesson01
cd projects/lesson01
spyder
```
Then open the files in spyder

## Submitting your work

To submit your work you will upload a zip file to canvas, containing all your work.

The process is really simple, represents how we work on projects, and will allow you to focus on Python development. And at the end of class you will have a portfolio of your work to share as you chose.

Be sure to follow along again on the lesson 1 video if you need help.

On this course you can chose to do the assignments described in canvas, or for certain lessons you may do an alternative assignment instead of the canvas one, or in addition to it.
