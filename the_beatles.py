beatles = [
    {"name": "John Lennon", "birth_year": 1940,
        "death_year": 1980, "instrument": "piano"},
    {"name": "Paul McCartney", "birth_year": 1942,
        "death_year": None, "instrument": "bass"},
    {"name": "George Harrison", "birth_year": 1943,
        "death_year": 2001, "instrument": "guitar"},
    {"name": "Ringo Starr", "birth_year": 1940,
        "death_year": None, "instrument": "drums"}
]

# 1. John Lennon also plays guitar. Access the `instrument` key in his dictionary and change its value:


beatles[0]["instrument"] == "guitar"
print(beatles[0])


# 2. Write a function which takes in the list of band members as a parameter,
#    and returns a list of all the Beatles' names:
# Expected result: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr']


def get_all_names(the_band):
    all_names = []
    for person in the_band:
        all_names.append(person["name"])
    return all_names


print(get_all_names(beatles))


# 3. Write a function which takes in the list of band members as a parameter,
#    and returns a list of the members who are still alive
#    (i.e. they have no value for `death_year`)
#    Return the full dictionary for each member
# Expected result: [
#    {'name': 'Paul McCartney', 'birth_year': 1942, 'death_year': None, 'instrument': 'bass'},
#    {'name': 'Ringo Starr', 'birth_year': 1940, 'death_year': None, 'instrument': 'drums'}
# ]


def alive_band_members(all_band_memebers):
    alive = []
    for person in all_band_memebers:
        if person["death_year"] == None:
            alive.append(person)

    return alive


print(alive_band_members(beatles))


# 4. Combine the above two functions to return the names of all the members who are alive:
# Expected result: ['Paul McCartney', 'Ringo Starr']

names_of_living = alive_band_members(beatles)
print(get_all_names(names_of_living))
