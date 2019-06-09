import requests
import datetime
import calendar
import argparse

def date(today): # Gets todays date and the start date of the start of the month
    year = today.year
    month = today.month

    if month < 10:
        month = "0%s" %month

    start_date = "%s-%s-01" %(year,month)
    return start_date

def configure_parser():
    parser = argparse.ArgumentParser(description="if need specific dates for bill")
    parser.add_argument('-m', help='which month', default="")
    parser.add_argument('-y', help='which year',  default="")
    args = parser.parse_args()

    #global method
    month = args.m
    year = args.y
    return month, year


def azure():
    month= ""
    month, year = configure_parser()

    if month != "":
        
        days = calendar.monthrange(int(year),int(month))[1]
        start_date = "%s-%s-01" %(int(year),int(month))
        end_date = "%s-%s-%s" %(int(year),int(month),days)
        #print(start_date)
        #print(end_date)
    else:
        end_date   = datetime.date.today()
        start_date = date(end_date)
        #print(start_date)
        #print(end_date)
        
    
    accesskey =""
    enrol  = ""
    headers_key = {
        'Authorization' : "Bearer %s" %accesskey
    }

  
    response = requests.get(
        'https://consumption.azure.com/v3/enrollments/%s/usagedetails/download?startTime=%s&endTime=%s' %(enrol, start_date, end_date),
        headers=headers_key)
    print(response.text)
    
azure()