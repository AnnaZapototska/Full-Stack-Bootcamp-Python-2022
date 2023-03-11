# ex8

def age_on_planet(seconds, planet):
    earth_year = 31557600
    if planet == "Earth":
        age_in_years = seconds / earth_year
    elif planet == "Mercury":
        mercury_year = 0.2408467 * earth_year
        age_in_years = seconds / mercury_year
    elif planet == "Venus":
        venus_year = 0.61519726 * earth_year
        age_in_years = seconds / venus_year
    elif planet == "Mars":
        mars_year = 1.8808158 * earth_year
        age_in_years = seconds / mars_year
    elif planet == "Jupiter":
        jupiter_year = 11.862615 * earth_year
        age_in_years = seconds / jupiter_year
    elif planet == "Saturn":
        saturn_year = 29.447498 * earth_year
        age_in_years = seconds / saturn_year
    elif planet == "Uranus":
        uranus_year = 84.016846 * earth_year
        age_in_years = seconds / uranus_year
    elif planet == "Neptune":
        neptune_year = 164.79132 * earth_year
        age_in_years = seconds / neptune_year
    else:
        return "Invalid planet name."
    print(f'Age on planet {planet} is {age_in_years}')


age_on_planet(1000000000, "Mercury")
age_on_planet(1000000000, "Venus")
age_on_planet(1000000000, "Mars")
age_on_planet(1000000000, "Jupiter")
age_on_planet(1000000000, "Saturn")
age_on_planet(1000000000, "Uranus")
age_on_planet(1000000000, "Neptune")

# ex 9
users = []
from faker import Faker

fake = Faker()


def add_user(num_users):
    for _ in range(num_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)


add_user(5)
print(users)
