# PRACTICAL TASK 

city_flight = input("Which city are you flying into (e.g Ayr, Leeds, Manchester, Chester)? ")
num_nights = int(input("How many nights are you staying at the hotel? "))
rental_days = int(input("How many days do you need a rental car? "))

def hotel_cost(num_nights): # assuming that the hotel cost is the same price £135
    return num_nights * 135
def plane_cost(city_flight):
    if city_flight == "Ayr":
        return 100
    elif city_flight == "Leeds":
        return 125
    elif city_flight == "Manchester":
        return 150
    elif city_flight == "Chester":
        return 145
    else:
        return 130
def car_rental(rental_days):
    return rental_days * 46 #assuming the daily car rental cost is the same £46
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = int(hotel_cost(num_nights)) + int((plane_cost(city_flight)) + int(car_rental(rental_days))) #Have to cast all variables to integers
    return total_cost

total_cost = holiday_cost(hotel_cost, plane_cost, car_rental) #call the function

print("Below are your holiday details!")
print(f"You are flying to {city_flight}")    #use the f' function    
print(f"You are spending {num_nights} days there.")        #use the f' function
print(f"The total cost of your holiday is £: {total_cost} .")     #use the f' function