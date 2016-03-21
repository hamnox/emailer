from datetime import datetime, timedelta
from pytz import timezone
# http://pythonhosted.org/pytz/
# list of timezones codes is available here: http://stackoverflow.com/questions/13866926/python-pytz-list-of-timezones

def datestring(time):
    """Takes a datetime object, returns a human readable string"""
    string = time.strftime("%A, %B %d. %I:%M%p")
    if time.tzinfo:
        string = string + time.strftime(" %Z")
    return string

def datefromoffset(nextbasedate, offset):
    """Takes base date of a new debugging period and offset (format???), returns the datetime"""
# stub
    return datetime.datetime.now()



class Person:
    # want to keep a list of all people
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.active = True
        self.availability = None
    def deactivate(self):
        self.active = False


def hard_constraint_check(people, constraints):
    """takes list of people, list of constraint functions -> tuple of person &
        list of people matching their hard constraints"""
# stub
    return (people[0], people)

# never mind about this, no time
#    failed_matches = {}
    matches = []
    for person in people:
        person_matches = []
        for possible_partner in people:
            for function in constraints:
                if not function(person, possible_partner): # returns true
                    break
            else:
                person_matches.append(possible_partner)
        matches.append((person, person_matches))
    return matches 

def pair_people(people, constraints):
    """take list of people, constraint functions, return list of 2-tuples of people"""
# stub
    return [(people[0], people[1])]

    hard_oks = hard_constraint_check(people, constraints)
    # would prefer these were sorted by number of constraints
    pool = people
    matched = []

    while len(pool) > 0:
        pass


__test_person_1 = Person("paul", "werd@gmail.com")
__test_person_2 = Person("me", "me@me.org")
__test_pairing = pair_people([__test_person_1, __test_person_2], lambda x: True)

# these only pass by coincidence right now
# assert len(__test_pairing) == 1
# assert __test_person_1 in __test_pairing[0]
# assert __test_person_2 in __test_pairing[0]

# ----------------------------------------------
#                    TESTS
# ----------------------------------------------

# apparently pytz in the datetime constructor screws stuff up. ref:
# http://stackoverflow.com/questions/24856643/unexpected-results-converting-timezones-in-python
pt = timezone('America/Los_Angeles')
__test_date = pt.localize(datetime(2016,03,21,15,30,0,0))
assert datestring(__test_date) == "Monday, March 21. 03:30PM PDT"



# TODO: how on earth do I test the people pairings?
# assert each person in given people is in there, and that no duplicates exist
# assert each person in given people is in there, and that no duplicates exist

