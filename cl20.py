"""Current date and time
Outline:
Write a program to check the current date and time?

Random date and time
Outline:
Write a program to generate a random date and time from the given start and end dates

Trip expenditure
Outline:
Write a program to calculate the total trip expenditure:
Calculate the hotel cost per day Calculate the plane cost Price of
the vehicle rented during the trip"""


"""from datetime import date,time,datetime 
today=date.today()
print(today)
time1=datetime.now()
print(time1)"""

"""import time
import random
def generate(stardate,enddate):
    print("printing random date",stardate,"and",enddate)
    rd=random.random()
    dateformat='%m/%d/%Y'
    starttime =time.mktime(time.strptime(stardate,dateformat))
    endtime =time.mktime(time.strptime(enddate,dateformat))
    randomtime =starttime+rd*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate 


print("random date = ",generate("1/1/2020", "12/12/2024"))"""

def hotel_cost(nights):
    return 140*nights

#Define a function called plane_ride_cost that takes a string, city, as input.
def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475

#Define a function called rental_car_cost with an argument called days    
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days
        
#Define a function called trip cost with argument day, money and city
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
	
print("Cost of car rental: ",rental_car_cost(6))

print("Cost of plane ride: ",plane_ride_cost("Los Angeles"))

print("Cost of hotel room: ", hotel_cost(7))

print("Total cost of the trip:",trip_cost("Los Angeles",7,500))

print(trip_cost("Tampa",6,500))