import argparse
import requests
import json
parser=argparse.ArgumentParser(description="Weather CLI Tool")
parser.add_argument("city" , help="Please, enter the city you live in mate.")
parser.add_argument("--unit" , type=int , help="Enter the unit u want ur temprature to be shown in.")
parser.add_argument("--farenhiet" , action="store_true")
parser.add_argument("--save" , action="store_true")
args=parser.parse_args()


try:
    url=f"https://wttr.in/{args.city}?format=j1"

    response=requests.get(url , timeout=10)

    if response.status_code==200:
        data=response.json()
    
        temp = data["current_condition"][0]["temp_C"]
        description = data["current_condition"][0]["weatherDesc"][0]["value"]
        print(f"City: {args.city}" )

       
        if args.farenhiet:
            temp_faren = (int(temp) * 9/5) + 32
            print(f"Temprature in Farenhiet: {temp_faren}")
        else:
            print(f"Temprature in Celsius: {temp}")
        print(f"Description: {description}")



        if args.save:
            weather_data={"City":args.city , "Temprature" : temp , "description" : description}

            with open("weather.json" , "w") as l:
                json.dump(weather_data , l)

    elif response.status_code in  [400,401,403,404,408,409,429,500,502,503,504]:
        print("Some Problem occured")

        

except requests.exceptions.ConnectionError:
    print("Failed to connect")

except requests.exceptions.Timeout:
    print("Try again later")

except ValueError:
    print("This type is not supported")

except requests.exceptions.JSONDecodeError:
    print("OOPS, Unsupported data type returned")


