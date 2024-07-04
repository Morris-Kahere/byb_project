# Define the hotel cost per night (you can adjust this value)
HOTEL_COST_PER_NIGHT = 100

# Define flight costs for different cities (you can adjust these values)
CITY_FLIGHT_COSTS = {
    "Ayr": 100,
    "Leeds": 150,
    "Manchester": 200,
    "Chester": 180
}

# Define the daily car rental cost (you can adjust this value)
DAILY_RENTAL_COST = 46

def hotel_cost(num_nights):
    return num_nights * HOTEL_COST_PER_NIGHT

def plane_cost(city_flight):
    return CITY_FLIGHT_COSTS.get(city_flight, 0)  # Return 0 if city not found

def car_rental(rental_days):
    return rental_days * DAILY_RENTAL_COST

def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    total_cost = total_hotel_cost + total_plane_cost + total_car_rental_cost
    return total_cost

# Get user inputs
city_flight = input("Enter the city you will be flying to (e.g., Ayr, Leeds, Manchester, Chester): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculate the holiday cost
total_holiday_cost = holiday_cost(num_nights, city_flight, rental_days)

# Print holiday details
print("\nHoliday Details:")
print(f"City of Flight: {city_flight}")
print(f"Number of Nights at Hotel: {num_nights}")
print(f"Number of Days for Car Rental: {rental_days}")
print(f"Total Holiday Cost: {total_holiday_cost}")

    
