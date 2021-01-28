# Hands-on tutorial on code testing for researchers [![Build Status](https://travis-ci.com/joacorapela/pyClubCI.svg?branch=master)](https://travis-ci.com/joacorapela/pyClubCI) [![codecov](https://codecov.io/gh/joacorapela/pyClubCI/branch/master/graph/badge.svg?token=WYRS7XNOHN)](https://codecov.io/gh/joacorapela/pyClubCI)

## Introduction
- Old and new approaches to testing
- Relevance for researchers (that are not software developers)
    - Catch bugs early
    - Safe net for code modification

We will illustrate testing with a simple calculator application. First we will:
- Create a simple Python calculator application
- Program tests for your code
- Run test locally with `pytest`
- Verify your tests coverage locally with `coverage.py`

Then, to automate these tasks, we will:
- Create a Github repository for your calculator application and push it
- Automate the run of your tests and their coverage analysis with [TravisCI](https://travis-ci.org/)
- Integrate coverage analysis reports into your Github repository (e.g., show a tests-covering badge in your README.md) with [codecov](https://about.codecov.io/)

I will conclude with
- Comments on why tests are important to my work
- Suggestions on how to write good tests
## Manual approach

### Create conda environment

- Create and activate a `TutorialCI` conda environment
```
conda create --name TutorialCI
conda activate TutorialCI
```
- Add relevant packages `pytest`, `coverage` to conda
```
conda install pytest coverage
```
- Create `requirements.txt` with the following content
```
pytest
coverage
```
### Program the calculator

- In a directory called `TutorialCI` write the first version of `calculator.py`
```python
"""
Calculator library containing basic math operations.
"""

def add(first_term, second_term):
    return first_term+second_term

def subtract(first_term, second_term):
    return first_term-second_term
```
### Test your calculator

- Write test for the first version of `calculator.py` in module `test_calculator.py`
```python
"""
Unit tests for the calculator library
"""

import pytest
import calculator


def test_addition():
    assert 4 == calculator.add(2, 2)


def test_subtraction():
    assert 2 == calculator.subtract(4, 2)
```
- Run the tests
```
pytest
```
- Examine the tests report
- Introduce a bug in `subtract` and see if the tests catch it. Modify `subtract` as follows
```
def subtract(first_term, second_term):
    return first_term*second_term
```
and run the test again
```
pytest
```
- Let's experiment with [Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) and write tests before implementing new functionality. Add the following test function to module `test_calculator.py`
```
def test_division():
    assert 2 == calculator.divide(4, 2)
```
- Run the tests again and see what happens
```
pytest
```
- Fix the failing test by implementing divide in the calculator
```
def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError()
    return numerator / denominator
```
- To complete our basic calculator add the multiply functionality (but let's forget to add a test for it)
```
def multiply(first_factor, second_factor):
    return first_factor * second_factor
```

### Measure the coverage of your tests

So far we implemented a calculator with all the basic arithmetic functions, and tests for most of these functions. Now let's measure how well our tests probe or cover our code.

- Measure coverage
```
coverage run -m pytest
```
- Report coverage in HTML format
```
coverage html
```
- Open in your browser the file `htmlcov/index.html`
- Add a test for the multiply function
```
def test_multiplication():
    assert 8 == calculator.multiply(4, 2)
```
- Measure coverage
```
coverage run -m pytest
```
- Report coverage in HTML format
```
coverage html
```
- Open in your browser the file `htmlcov/index.html`
<br></br>
- We have not yet achieved 100% coverage. Let's add a test for the exception if branch of `divide`
```
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(4, 0)
```
- Finally check that your tests completely cover you calculator implementation. Measure coverage
```
coverage run -m pytest
```
- Report coverage in HTML format
```
coverage html
```

## Automatic approach

### Create a Github repository TutorialCI
- Create a git repository in the directory `TutorialCI`
```
git init
```
- Create the .gitignore file with the following content
```
*~
*.swp
htmlcov/
__pycache__/
```
- Create a `README.md` for your repository with the following content
```
# Tutorial on code testing for researchers
```
- Add all files in the directory `TutorialCI` to the repository
```
git add .
```
- Commit the added files
```
git commit -m "Added"
```
- Create a new repository called `TutorialCI` in Github
- Add the reference to the `TutorialCI` Github repository to your local git repository
```
git remote add origin https://github.com/<your-github-username>/TutorialCI.git
```
- Push your `master` branch to Github
```
git push -u origin master
```

### Automate testing
Now we have our calculator application under version control in Github. Next we will use [Travis CI](https://travis-ci.org/) to automate our tests
- Sign-up to Travis-CI and choose *Activate all repositories*
- Add a file named `.travis.yml` with the following content to the root of your git repo
```
language: python

install:

  - pip install -r requirements.txt

script:

  - pytest
```
- Add `.travis.yml` to your git, commit and push
```
git add .travis.yml
git commit -m "Added"
git push
```
- Watch what happens in Travis CI
- Check in your email the notification from Travis CI about your test results
- To add a badge to your `README.md` to indicate the outcome of your latest test:
    - Go to your repository Travis CI page https://travis-ci.com/github/your-Github-username/TutorialCI. 
    - Click on the badge next to the title
    - In the next dialog box select form the dropbox `FORMAT` the option `Markdown`
    - Copy to the clipboard the contents of box `RESULT`
    - Edit your `README.md` and paste the content of the clipboard at the end of the title line
    - The title of your `README.md` should be as follows
    ```
    # Lessons from the tutorial on code testing for researchers [![Build Status](https://travis-ci.com/<your-Github-user-name>/TutorialCI.svg?branch=master)](https://travis-ci.com/<your-Github-user-name>/TutorialCI)
    ```
- Commit all changes to your local repository and push them to Github
- Look at the new badge in the `README.md` of your TutorialCI repository
- Let's play a little 
    - add a new bug to the calculator
    - add, commit and push
    - check the Travis CI email
    - check the build badge

### Automate coverage reports
After every commit we want to have a measure of how well our tests probe or cover our code. For this we will use [codecov](https://about.codecov.io/)

- Signup to [codecov](https://about.codecov.io/) and add the TutorialCI Github repository
- Modify your `.travis.yml` to perform code coverage analysis and submit its results to codecov. You modified `.travis.yml` should look as follows
```
language: python

install:

  - pip install -r requirements.txt

script:

  - pytest
  - coverage run -m pytest # tell Travis CI to do coverage analysis

after_success:
  - bash <(curl -s https://codecov.io/bash) # send coverage results to codecov
```
- To add the `codecov` badge:
    - Go to [codecov](https://about.codecov.io/)
    - Login
    - Select your repository from the list
    - Select Settings on the top right
    - Select Badge from the left navigation bar
    - Copy the Mardown code
    - Paste the copied code into the title of your `README.md`.
    - The title of your `README.md` should be as follows
    ```
    # Lessons from the tutorial on code testing for researchers [![Build Status](https://travis-ci.com/your-Github-user-name/TutorialCI.svg?branch=master)](https://travis-ci.com/your-Github-user-name/TutorialCI)[![codecov](https://codecov.io/gh/your-Github-user-name/TutorialCI/branch/master/graph/badge.svg?token=NNIS1SSK7L)](https://codecov.io/gh/your-Github-user-name/TutorialCI)
    ```
- Add, commit and push your local changes to your Github repository.
```
git add .travis.yml
git commit -m "Added coverage automatization"
git add README.md
git commit -m "Added coverage badge"
git push
```
- Look at your test coverage in the `README.md` of your repository.
- Let's play a little more
    - add a new function to the calculator, without a corresponding test
    - add, commit and push
    - check the codecov badge
    - check the codecov reports

## Other options

Here we used `pytest` for testing, `coverage.py` to analyze code coverage, Travis CI to automate testing and `codecov` to automate coverage measures. However, there are other options, possibly better ones than the ones I chose.

- Testing: unitest, nose
- Coverage: pytest-cov
- CI: CircleCI, Github Actions
- Code coverage reports: coveralls, sonaclouds

## Final remarks
### My experience using CI
- [svGPFA](https://github.com/joacorapela/svGPFA)
- Why is CI relevant to my work?
    - My supervisor would not trust on my code
    - Safe net for code modification

### Suggestions about how to write tests:
- When you know you your code is working well, generate input-output test for most functions (to build a safe net for future code updates)
- If you are extending another code, use the original code to generate input-output tests for your code

## Summary
- Bugs in research code can have catastrophic consequences
- There are excellent and easy to use tools that will help you find bugs early
- Test provide you a safe net to modify your code without introducing bugs into older code

Note: please help me improve this tutorial. If you find any problem running it, please open an issue and/or submit a pull request with a fix. Thanks.
