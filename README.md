# PyClub on Continuous Integration [![Build Status](https://travis-ci.com/joacorapela/pyClubCI.svg?branch=master)](https://travis-ci.com/joacorapela/pyClubCI) [![codecov](https://codecov.io/gh/joacorapela/pyClubCI/branch/master/graph/badge.svg?token=WYRS7XNOHN)](https://codecov.io/gh/joacorapela/pyClubCI)

##  Introduction
. Why avoiding bugs is important?

## Testing and Continuous Integration
### Introduction
- The old and new approaches to testing
    - Formal program testing (a waste of time?)
- Relevance for researchers (that are not software developers)
    - Catch bugs early
    - Safe net for code modification
### Simple calculator example
- Create and activate an environment
```
conda create --name PyClubCI
conda activate PyClubCI
```
- Add relevant packages
- Write code
- Run tests
- Test coverage
    - Coverage run
        - Statement coverage: coverage run -m pytest
        - Branch coverage: coverage run --branch -m pytest
    - Coverage report
        - Coverage html
    - Exclude code from coverage statistics
- Travis-CI
- codecov

- Other options
    - Testing
    - Coverage
    - CI
    - Code coverage reports

- My experience using CI
    - svGPFA
    - Why is CI relevant to my work?
        - My supervisor would not trust on my code
        - Safe net for code modification
    - My test-writing style: black-box
    - Suggestions about how to write tests:
        - When you know you your code is working well, generate input-output test for most functions (to build a safe net for future code updates)
        - If you are extending another code, use the original code to generate input-output tests for your code

## Good Github practices
- Frequent commits with informative messages
- Recover image of your code at a given date

## Plotting

