from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json
from transformers import pipeline
from datetime import datetime
import datetime as dt
from typing import Annotated
from fastapi import FastAPI, APIRouter, Query, Body

app = FastAPI()
df = pd.read_csv('./new_data.csv')


# Load pre-trained text classification pipeline
classifier = pipeline('text-classification', model='distilbert-base-uncased-finetuned-sst-2-english')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Feddit app!"}

def get_data(id):
  sub_df= df[df['id']==int(id)]
  print(sub_df)
  return sub_df

#date format should be yyyy-mm-dd
def filter_date(sub_df, start_date, end_date):
    sub_df['Date'] = pd.to_datetime(sub_df['Date'])
    mask = (sub_df['Date'] > start_date) & (sub_df['Date'] <= end_date)
    sub_df = sub_df.loc[mask]
    return sub_df


def parse_csv(df):
    res = df.to_json(orient="records")
    parsed = json.loads(res)
    return parsed


def process(out):
  labels = []
  score = []
  print("length of intermediate is ", str(len(out)))
  for index, row in out.iterrows():
    result = classifier(row['subreddit_comments'])
    labels.append(result[0]['label'])
    score.append(result[0]['score'])
    print(labels, score)
  print(labels)
  print(score)
  out['classification_of_comment'] = labels
  out['classification_score'] = score
  return out

@app.get("/subfedditid1/")
async def read_item(subfedditid=2):
        print("length of df is ", int(len(df)))
        sub_df = get_data(subfedditid)
        output = process(sub_df)
        #return {"subfedditid is": output}
        if len(output)>0:
            return parse_csv(output)
        else:
            {"message": "Output data is empty use some other filter conditions"}


@app.get("/subfedditid2/")
async def read_item2(subfedditid=3,  start_date='2020-12-02', end_date='2025-12-01'):
        print("Start date is ", start_date)
        print("end date is ", end_date)
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        sub_df = get_data(subfedditid)
        sub_df = filter_date(sub_df, start_date, end_date)
        output = process(sub_df)
        output['Date']= output['Date'].dt.strftime('%Y-%m-%d')
        if len(output)>0:
            return parse_csv(output)
        else:
            {"message": "Output data is empty use some other filter conditions"}

@app.get("/subfedditid3/")
async def read_item2(subfedditid=3,  start_date='2020-12-01', end_date='2025-12-01', sort_flag= False):
        print("Start date is ", start_date)
        print("end date is ", end_date)
        print('sort flag is ', sort_flag)
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        sub_df = get_data(subfedditid)
        sub_df = filter_date(sub_df, start_date, end_date)
        output = process(sub_df)
        output['Date']= output['Date'].dt.strftime('%Y-%m-%d')
        sort_flag = False if  sort_flag.lower()=='flase' else sort_flag
        if sort_flag:
            print("srting data since flag is true")
            output = output.sort_values(by=['classification_score'], ascending=False)
        if len(output)>0:
            return parse_csv(output)
        else:
            {"message": "Output data is empty use some other filter conditions"}
