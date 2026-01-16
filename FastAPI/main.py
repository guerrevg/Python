from fastapi import FastAPI, HTTPException
from typing import Any
from datetime import datetime

app = FastAPI(root_path="/api/v1")

@app.get('/')
async def root():
    return {"message":"Hello World !"}

data : Any = [
    {
        "campaogn_id":1,
        "name":"Summer Launch",
        "due_date" : datetime.now(),
        "created_at" : datetime.now()
    },
    {
        "campaogn_id":2,
        "name":"Black Friday",
        "due_date" : datetime.now(),
        "created_at" : datetime.now()
    }
]


@app.get("/campaigns")
async def read_campaigns():
    return {"Campaigns",data}

@app.get("/campaigns/{id}")
async def read_campaign(id:int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return {"campaign":campaign}
    raise HTTPException(status_code=404)



#------------------------------------------Loading Code It Can Take longer than Usual---------------------------------------------------------