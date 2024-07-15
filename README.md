# Real-Time Sentiment Classification

## Overview

This project provides a real-time sentiment classification application. Given the name of a subfeddit, the application returns:
- A list of the most recent comments (up to 25 comments).
- For each comment:
  - The unique identifier of the comment
  - The text of the comment
  - The polarity score and the classification of the comment (positive or negative) based on that score.

## APIs

The application generates three APIs:

1. **/subfedditid1**: Filters data based on the subfeddit ID.
2. **/subfedditid2**: Filters data based on the subfeddit ID, start date, and end date.
3. **/subfedditid3**: Filters data based on the subfeddit ID, start date, end date, and a sorting flag on the comment polarity score.

## Source code
app.py contains the source code

## Dummy data
input dummy data is available in the form of csv file

## Requirements

The `requirements.txt` file lists all the dependencies needed to run the application:


## Dockerfile
The `Dockerfile` is used to containerize the application:

## Pytest
to test the code, you can add more test cases here

## Git workflow
.yaml file is added in repo to be used to set the workflow


# To execute
## locally
- clone repo
- build virtual env:
- install requirements: pip install -r requirements.txt
- run execution command : uvicorn app:app --host 0.0.0.0 --port 8000
- check outcome on local server at 8000 port

## using docker setup
- build docker image: docker build -t api_app:latest .
- execute docker command: docker run -p 8000:8000 api_app:latest




