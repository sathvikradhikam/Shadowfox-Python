australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Function to calculate BMI and determine the category
def calculate_bmi():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    
    bmi = weight / (height ** 2)

    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"

    print(f"Your BMI is {bmi:.2f}, which is considered '{category}'.")

# Function to determine the country of a city
def find_country():
    city = input("Enter a city name: ")
    
    # Check which country the city belongs to
    if city in australia:
        country = "Australia"
    elif city in uae:
        country = "UAE"
    elif city in india:
        country = "India"
    else:
        country = "Unknown"

    if country != "Unknown":
        print(f"{city} is in {country}.")
    else:
        print(f"{city} is not in the predefined list of cities.")

# Function to check if two cities belong to the same country
def check_same_country():
    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")
    
    # Determine the country for both cities
    country1 = None
    country2 = None
    
    if city1 in australia:
        country1 = "Australia"
    elif city1 in uae:
        country1 = "UAE"
    elif city1 in india:
        country1 = "India"
    
    if city2 in australia:
        country2 = "Australia"
    elif city2 in uae:
        country2 = "UAE"
    elif city2 in india:
        country2 = "India"
    
    # Check if both cities belong to the same country
    if country1 and country2:
        if country1 == country2:
            print(f"Both cities are in {country1}.")
        else:
            print("They don't belong to the same country.")
    else:
        print("One or both cities are not in the predefined list of cities.")

print("BMI Calculation:")
calculate_bmi()
print("\nCity Country Lookup:")
find_country()
print("\nCheck Same Country:")
check_same_country()