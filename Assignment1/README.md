# Sentiment App

## Introduction

This project is to create an streamlit app to predict the sentiment of movie review interactively.

## Prerequisites

To run this app, please make sure `Docker`, `Git`, and other essential python packages mentioned in the `requirements.txt` are installed. 

## How to run this app 

- Download the entire folder by `git clone git@github.com:jiansfoggy/4705_jiansun_assignment.git`

- Enter the folder `cd Assignment1`

- Data Preparation and Model Training `python3 train_model.py`

- Directly Building the Streamlit Application `streamlit run app.py`

- Use Docker Build the Streamlit Application 
  
  1. In the `./Assignment1`, Run `make build` to build the Docker image

  2. Run `make run` to process the container from the image

  3. There are three URL links shown on the screen

     ```
     Local URL: http://localhost:8501
     Network URL: http://172.17.0.3:8501
     External URL: http://97.228.134.68:8501
     ```

  4. Copy Local URL to the browser and hit enter or return button to enjoy this app.