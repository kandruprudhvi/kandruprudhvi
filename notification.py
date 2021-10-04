import json
import requests
import time
import os
from datetime import datetime

TIME_INTERVAL_IN_HOUR =72


# for private repo add token as an env variable
headers = {"Authorization": "Bearer "+os.environ["var1"]  }

# for private repo to pass the auth token directly
#headers = {"Authorization": "Bearer ghp_0Di8eEjt4fMFB4lhCnZPndgMdzfg2V36"}


github_data= requests.get('https://api.github.com/repos/kandruprudhvi/code_server/pulls',headers=headers)

# for public repo
# github_data= requests.get('https://api.github.com/repos/kandruprudhvi/code_server/pulls')

github_josn_data = json.loads(github_data.text)
# github_josn_data


def send_slack_notification(String):


    headers = {
        'Content-type': 'application/json',
    }

    data = {'text':String }

    response = requests.post('https://hooks.slack.com/services/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', headers=headers, json=data)
    response

total_pull_req=str( len(github_josn_data))
counter=0
for pull_request_data in github_josn_data:

    if(counter==0):
        String= "======= Total Pull Request = "+ str(total_pull_req)+ "======= \n -----Current Pull Request No - "+str(pull_request_data['number'])+ " Found --------  \nBranch :"+pull_request_data['head']['ref']+"\nRepo : "+pull_request_data['head']['repo']['name']+"\nStatus : "+pull_request_data['state']+"\nTitle For pull request : "+pull_request_data['title']+"\nCreated At : "+pull_request_data['created_at']
    else :
         String= "---------Current Pull Request No - "+str(pull_request_data['number'])+ " Found ---------  \nBranch :"+pull_request_data['head']['ref']+"\nRepo : "+pull_request_data['head']['repo']['name']+"\nStatus : "+pull_request_data['state']+"\nTitle For pull request : "+pull_request_data['title']+"\nCreated At : "+pull_request_data['created_at']
    counter= counter+1
    
    date_string1 = pull_request_data['created_at'].replace("T"," ")
    date_string2 = pull_request_data['created_at'].replace("Z"," ")
    date_string1[:-1]
    date1=datetime.fromisoformat(date_string1[:-1])
    date2= datetime(date1.year,date1.month,date1.day,date1.hour,date1.minute,date1.second)
    date_now=datetime.now()

    timediff=date_now-date2
    current_interval=int(timediff.total_seconds()/3600)
    print(current_interval)
    if(TIME_INTERVAL_IN_HOUR<current_interval):
        send_slack_notification(String)

