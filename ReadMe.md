# Code to collect specified monthly usage data from EA

## Run Code
For getting usage to the current month to date:
    ```
    python python.py > usage.csv
    ```

For getting selected month:
    ```
    python python.py -m <monthnumber> -y <yearnumber>
    ```

Example for Jan 2019s usage:
    ```
     python python.py -m 01 -y  2019
    ```

## Variables
The can be found in the EA Portal 
From Reports > Access Keys
- accesskey =""
From the Manage page
- enrol  = ""
