#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


# see also: https://github.com/sendgrid/sendgrid-python
# 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

 
# http://naelshiab.com/tutorial-send-email-python/

fromaddr = "mheisey.nox@gmail.com"
toaddr = "THE EMAIL ADDRESS TO SEND TO" # TODO: Swapping out

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "0bs1d14n4 n0x")
 
text = email_generator(fromaddr, toaddr)

server.sendmail("mheisey.nox@gmail.com", toaddr, msg)
server.quit()




def email_generator(from_email, to_email):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "SUBJECT OF THE MAIL"
    body = "YOUR MESSAGE HERE"
    msg.attach(MIMEText(body, 'plain'))
    return msg.as_string()

"""new components:
    availability: ok'd times. hard no times. soft ok times.
        for now just keep 
        import as spans, import as singleOK
        last_offset, last_partner.

    Person: EMAIL key
        active
        availability
        name
        preferred methods of contact
        Skype
        Hangouts
        Phone Number
        Mobile
        Location
        Other Contact method
        Timezone
        Blurb
        Meta-debugger
        Notes: [(date, string)...]
    constraints:
        [PREFER: [(p1, p2),...], UNMATCH:[(p1, p2),...]]
        eventually I may want this as part of the person

    given two availabilities, which may match or may be 
    previous_matchups:
        save as json obviously, can be separable


    PERSON_FROM_JSON
    PERSON_TO_JSON



# components:
    # format dates to readable
    # pair up candidate email addresses
        # hard constraint checker
        # importing/storing constraint information
        # optional: soft constraint checker
    # generate next dates from constraints
    # make batch of emails
    # send emails loop

    # test dates
        # time zones
        # do they match
    # test emails
        # formats correctly
        # pairs correspond
    # test sender
        # server responds
        # emails send


