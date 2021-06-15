#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/mycode/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    start_date = input("Enter the start date as YYYY-MM-DD\nStart Date:> ")
    print("---------------------------------------------------------")
    end_date = input("End Date must be within 7 days of starting date. Enter it in the same format as your start date\nEnd Date:> ")
    print("---------------------------------------------------------")
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(f"{NEOURL}start_date={start_date}&end_date={end_date}&{nasacreds}")

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(f"""Asteroid Total: {neodata["element_count"]}""")

    #Hazardous Asteroids
    hazard_count = 0
    for dates in neodata["near_earth_objects"]:
        for items in neodata["near_earth_objects"][dates]:
            print(items["name"])




if __name__ == "__main__":
    main()

