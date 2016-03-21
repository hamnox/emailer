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
    count = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.active = True
        self.availability = None
        count += 1
    def deactivate(self):
        self.active = False






def brute_pair_people(people, constraints):
    """list of people objects, list of constraint functions -> tuples of pairings that match"""
    return (people[0], people[1])

#stub 
    available_pool = people
    tries = 0
    while avilable_pool != None:
        while tries < 5:
            pass
        # incomplete

    # assert constraints

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

