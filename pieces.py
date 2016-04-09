from datetime import datetime, timedelta
from pytz import timezone

import sendgrid
import json

# http://pythonhosted.org/pytz/
# list of timezones codes is available here: http://stackoverflow.com/questions/13866926/python-pytz-list-of-timezones

Sendgrid_API_key = None
with open('sendgrid.key', 'r') as keyfile:
    Sendgrid_API_key = keyfile.readline()[:-1]

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
#    def __init__(self, **kwargs):
 #       self.update(kwargs)
        # this is horribly hacky and I don't know if it will work
        # http://stackoverflow.com/questions/1098549/proper-way-to-use-kwargs-in-python

    def __init__(self, email="email@server.com", name="name"):
        self.name = name # want to gen random numbers
        self.email = email # want to make a random number
        self.availability = Availability("All")
        self.active = True
        self.contact_preferences = {"Skype":True, "Google Hangouts":True, "Phone Call":True,
                "SMS":True, "Emails":True, "Face to face":True}
        self.skype = None
        self.hangouts = None
        self.phone = None
        self.mobile = None
        self.location = None
        self.timezone = 'America/Los_Angeles'
        self.other = None
        self.blurb = "This is a person."
        self.metadebug = False # function
        self.notes = None


    def deactivate(self):
        self.active = False
    def to_dict(self):
#        http://www.blog.pythonlibrary.org/2013/01/11/how-to-get-a-list-of-class-attributes/
        return self.__dict__()
    def _serialize_emails(self):
        return json.dumps(self.email)
    # stub
    def make_availability(self, spans):
        """ takes a list of span times as [((day, hour), (day, hour)),..] and returns an Availability
            containing those times. WISHLIST: make a mash availability fn, subtract avail. function"""
        newAvail = Availability()
        for span in spans:
            t1 = span[0][0] * 24 + span[0][1]
            t2 = span[1][0] * 24 + span[1][1]
            newAvail.add_span(t1, t2)
        return newAvail

def person_from_json(data_object):
    """given a JSON object approximating a person, return a person object!"""
    lePerson = Person()
    # dunno if python json object follows same rules as javascript dictionaries
    lePerson.name = data_object['name'] # want to gen random numbers
    lePerson.email = data_object['email'] # want to make a random number
    import re 
    spans = re.findall("\[(\[(\d+), (\d+)\])*?\d\]", data_object['availability'])
                # %i - %i" % (x.total_seconds()/3600, y.total_seconds()/3600) for x, y in self.times].__str__()
    lePerson.availability = lePerson.make_availability(spans)
    # lePerson.active = data_object['active']
    lePerson.active = True
    lePerson.contact_preferences = data_object['contact_preferences']
    lePerson.skype = data_object['skype']
    lePerson.hangouts = data_object['hangouts']
    lePerson.phone = data_object['phone']
    lePerson.mobile = data_object['mobile']
    lePerson.location = data_object['location']
    lePerson.timezone = timezone(data_object['timezone'])
    lePerson.other = data_object['timezone']
    lePerson.blurb = data_object['blurb']
    lePerson.metadebug = data_object['metadebug']
    lePerson.notes = data_object['notes']
    return lePerson



# PLANNING:
# Okay... so each person has a timezone.
# We need an object that's something like (p1, p2, Datetime, Contact Method)
# alternatively a dict: {partners: [p1,p2] , datetime: Datetime,
#       contact_type: [options]}... may not get to contact type this round
    # at some point we need an option to get it by matching up p1/p2
    # availability and picking a random time they both can go
# for each email, we need to get the Readable date for that user,
    # the GoogleCalendar Date, possibly a simple date in the partner's time
    # zone, and possibly some alternate times (given in both TZs) to
    # reschedule to....

    # for inputting, we want an interface to grep people
    # i think we need dynamic python. exec(file) works in python 2.x
    # http://stackoverflow.com/questions/4624416/is-there-a-posibility-to-execute-a-python-script-while-being-in-interactive-mode

# alternatively I want a command line loop to print options,
    # grab people by name, and input <week #> <DayAbbr> <24hr time> in PT
    # this will save as an offset off of pacific time




# for inputting, need a way to print the names of people objects in a list or dict
# DONE: for inputting, need a function to interpret
# for inputting, want a way to save pairings and their offsets to a file


class Availability:
    """represent time spans available for scheduling in hours offset"""
    debug_length = 1
    available_span = 24*14

    def __init__(self, t1=None, t2=None):
        if t1 == None:
            self.times = []
            return
        if t1 == "All":
            t1 = 0
            t2 = Availability.available_span
        elif t2 == None:
            t2 = t1 + Availability.debug_length
        self.test_values(t1,t2)

        self.times = [[timedelta(hours=t1), timedelta(hours=t2)]]

    def _serialize(self):
#        zoo = [("%s - %s" % (x.total_seconds()/3600,
 #           y.total_seconds()/3600)) for x, y in self.times] 
        zoo = [(x.total_seconds()/3600,y.total_seconds()/3600) for x, y in self.times]

        return json.dumps(zoo)


    def __repr__(self):
        return ["%s - %s" % (x.total_seconds()/3600, y.total_seconds()/3600) for x, y in self.times].__str__()


    def add_span(self, t1, t2 = None):
        if t2 == None:
            t2 = t1 + Availability.debug_length
        self.test_values(t1,t2)
        self.times.append([timedelta(hours=t1), timedelta(hours=t2)])

    def remove_span(self, t1, t2):
    # stub
        pass

    def _combine_spans(span1, span2):
        """ combines two 2-tuples/lists that contain or overlap each other
                returns a 2-tuple """
        assert len(span1) == 2
        assert len(span2) == 2
        return (min(span1[0], span2[0]), max(span1[1], span2[1]))

    def _check_overlap(self, span1, span2):
        """takes in two 2-tuples/lists of numbers in ascending order
            and returns true if their spans overlap"""
        if span1[0] <= span2[0]:
            if span1[1] >= span2[0]:
                return True
        elif span2[1] >= span1[0]:
            return True
        return False

    def remove_span(self, span):
        self.times.pop(span)

    def fixup_availability(self):
        index = 0
        
        while index < len(self.times) - 1:
            for span in self.times[index + 1:]:
                if self._check_overlap(self.times[index],span):
                    self.times.append(self._combine_spans(self.times[index], span))
                    self.times.pop(self.times[index])
                    self.times.pop(span)
            else:
                index += 1
        # TODO: need to test this


    def test_values(self, t1,t2):
        assert t2 > t1
        assert t1 >= 0
        assert t1 <= Availability.available_span
        assert t2 >= 0
        assert t2 <= Availability.available_span

weeknums = {"sun":0, "mon":1, "tue":2, "wed":3, "thu":4, "fri":5, "sat":6}
def parse_offset_input(string):
    # for inputting, need to turn <week #> <DayAbbr no period> <24hr time> in PT into an offset
    # later on want a way to specify time zone for natural time range inputs
        # maybe then I'll save in UTC and shift the offsets during Daylight savings
    import re
    results = re.findall("(\d) (sun|mon|tue|wed|thu|fri|sat)\.? (\d+):(\d+)", string.lower())
    assert len(results) == 1
    week = int(results[0][0]) - 1
    day = weeknums[results[0][1]]
    hour = int(results[0][2]) + float(results[0][3])/60.0
    return (week * 7 + day) * 24 + hour


__SAVEFILENAME = "base_emailer_data.json"
import json
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,Availability):
            return o._serialize()
        if isinstance(o,Person):
            temp = o.__dict__
            temp['availability'] = temp['availability']._serialize()
            temp['timezone'] =  temp['timezone'].zone
            return json.JSONEncoder.default(self, temp)
        else:
            return json.JSONEncoder.default(self, o)
    def encode(self, o):
        if isinstance(o, list) and isinstance(o.__iter__().next(), Person):
            temp = {}
            for p in o:
                temp[p.email] = {"name": p.name, "timezone": p.timezone.zone}
            return json.dumps(temp, indent=1)


def save_to_file(data, savefilename=__SAVEFILENAME):
    with open(savefilename, 'w') as outfile:
        json.dump(data, outfile, cls=MyEncoder, indent=1)


def _get_pref(name):
    temp = raw_input("%s? y/N: " % (name))
    if temp.lower() == "y":
        return True
    else:
        return False

def _get_contact(name):
    temp = raw_input("%s: " % (name))
    if temp == "" or temp.lower() == "none":
        return None
    else:
        return temp

def get_me():
    going = "y"

    people = []
    while going == "y":
        a_person = Person()
        a_person.email = raw_input("new email: ")
        a_person.name = raw_input("name: " )
        a_person.contact_preferences = {}
        a_person.contact_preferences["Skype"] = _get_pref("Skype")
        a_person.contact_preferences["Google Hangouts"] = _get_pref("Google Hangouts")
        a_person.contact_preferences["Phone Call"] = _get_pref("Phone Call")
        a_person.contact_preferences["SMS"] = _get_pref("SMS")
        a_person.contact_preferences["Emails"] = _get_pref("Emails")
        a_person.contact_preferences["Face to Face"] = _get_pref("Face to face")
        temp = raw_input('Other: ')
        if temp.lower() != "n" and temp.lower() !="":
            a_person.contact_preferences["Other"] = temp
        a_person.skype = _get_contact("skype handle")
        a_person.hangouts = _get_contact("hangouts handle")
        a_person.phone = _get_contact("phone number")
        a_person.mobile = _get_contact("mobile")
        a_person.location = _get_contact("location")
        temp = raw_input("timezone: ")
        if temp == "" or temp.lower() == "none":
            a_person.timezone = None
        else:
            a_person.timezone = temp
        a_person.other = _get_contact("Other contact")
        a_person.blurb = _get_contact("blurb")
        temp = raw_input("metadebug? N/~/y: ")
        if temp.lower() == "y":
            a_person.metadebug = True
        if temp.lower() == "~" or temp.lower() == "-":
            # TODO: go back and correct 'no's
            a_person.metadebug = "Maybe"
        else:
            a_person.metadebug = False
        a_person.notes = raw_input("other notes: ")

        going = raw_input("keep going? ")

        people.append(a_person.__dict__)
        save_to_file(people)


     
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
    return [(Person("2@3.org","fake1"), Person("3@4.com","fake2"))]

    hard_oks = hard_constraint_check(people, constraints)
    # would prefer these were sorted by number of constraints
    pool = people
    matched = []

    while len(pool) > 0:
        pass


def make_message(subject, html, text):
    """given strings with the subject, html content, and body text, give me
     a message object back"""
    message = sendgrid.Mail()
    message.set_subject(subject)
    message.set_html(html)
    message.set_text(text)
    message.set_from('Mel Heisey <mheisey.nox@gmail.com>')
    return message

def sendemail(recipient, message):
    """take a recipient email address and message, email the message.
    return a tuple of http status code and ? message"""
    sg = sendgrid.SendGridClient(Sendgrid_API_key)
    message.add_to(recipient)
    status, msg = sg.send(message)
    return (status, msg)



# or
#     message = sendgrid.Mail(to='john@email.com',
#         subject='Example',
#         html='Body',
#         text='Body',
#         from_email='doe@email.com')
#     status, msg = sg.send(message)
#     print(status, msg)
# ~*~


# ----------------------------------------------
#                    TESTS
# ----------------------------------------------

def test_parse_offset_input():
    assert parse_offset_input("2 Sun. 10:00") == 178
    assert parse_offset_input("2 wed 18:00") == 258
    assert parse_offset_input("2 sun 11:00") == 179
    assert parse_offset_input("1 Thu 11:00") == 107
    assert parse_offset_input("2 wed. 13:30") == 253.5

def test_fromJSON():
    leobjects = []
    with open('old_user_data.json', 'r') as datafile:
        leobjects = json.load(datafile)

    people = []
    for leobject in leobjects:
        people.append(person_from_json(leobject))
    assert len(json.dumps(people, cls=MyEncoder, indent=1)) > 5


def test_send_email():
    #test_msg = make_message("Testy", "<font color=\"purple\">testing html</font>", "testing text")
    templ = ""
    with open("orig_gmail_template.html", "r") as template_file:
        templ = "".join(template_file.readlines())
        templ = templ.replace("\n","")
        print templ
    test_msg = make_message("Testy Template", templ, "")
    status, msg = sendemail("mheisey.nox@gmail.com", test_msg)
    assert status == 200


def test():
    test_parse_offset_input()
    # test_send_email()
    test_fromJSON()
    assert Sendgrid_API_key != None
    person_1 = Person("paul", "werd@gmail.com")
    _person_2 = Person("me", "me@me.org")
    test_parse_offset_input()
#    __test_pairing = pair_people([_person_1, _person_2], lambda x: True)

    # these only pass by coincidence right now
    # assert len(__test_pairing) == 1
    # assert _person_1 in __test_pairing[0]
    # assert _person_2 in __test_pairing[0]
    # apparently pytz in the datetime constructor screws stuff up. ref:
    # http://stackoverflow.com/questions/24856643/unexpected-results-converting-timezones-in-python

    _availability_1 = Availability((24*1))
    _availability_2 = Availability((24*3),(24*5))
    assert _availability_1.times == [[timedelta(1), timedelta(days=1, hours=1)]]
    assert _availability_2.times == [[timedelta(3), timedelta(5)]]
    json.dumps(_availability_1, cls=MyEncoder)

    pt = timezone('America/Los_Angeles')
    __test_date = pt.localize(datetime(2016,03,21,15,30,0,0))
    assert datestring(__test_date) == "Monday, March 21. 03:30PM PDT"

    _availability_3 = person_1.make_availability([((3,2), (4,1)),((1,0),(2,0))])
    assert len(_availability_3.times) == 2
    assert _availability_3.times[0] == [timedelta(days=3, hours=2), timedelta(days=4, hours=1)]
    assert _availability_3.times[1] == [timedelta(days=1), timedelta(days=2)]



    # TODO: how on earth do I test the people pairings?
    # assert each person in given people is in there, and that no duplicates exist
    # assert each person in given people is in there, and that no duplicates exist

if __name__ == "__main__":
    print "testing..."
    test()
    print "passed!"
    # get_me()

