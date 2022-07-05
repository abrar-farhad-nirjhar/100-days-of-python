from secrets import choice


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lillie", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country=None, visits=None, cities = None):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })

    print(travel_log)

while True:
    country = input("Which country did you go to?\n")
    visits = int(input("How many times did you go there?\n"))
    cities = input("Which cities did you visit?\n").split(' ')

    add_new_country(country=country, visits=visits, cities=cities)

    choice = input("Do you want to enter another entry to the travel log? y/n: ")
    if choice == 'n':
        break
    else:
        continue

