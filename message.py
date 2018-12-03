
INVITATION = """
Subject: Invitation to participate in KU Secret Santa

Merry Christmas! Too soon? Get excited now!

Congratulations! You are invited to participate in KU-wide Secret Santa event!

Rules are simple:
\t- Sign up for the event
\t- You will have a weekend (or more) to obtain a gift for the lucky/unlucky one
\t- On December 2nd, I will send you the email address of your special person
\t- Track your recipient down and have a good time!

Please note that it will be your responsibility to deliver the gift. Secret Santa organizers will not be held responsible for any undelivered presents, shattered dreams or bitter tears! More details on rules will come in the beginning of December.

If you wish to participate in the Secret Santa, please reply to this message. Your reply will count as a sign-up.
If not, no hard feelings. It doesn't sound like you wanted to have fun anyway. :<
You can also invite your friends! Tell them to send a message to go.secretsanta.ku@gmail.com and they are good to go!

Deadline for Secret Santa registration is November 29, 11:59pm

XOXOXO,
KU Secret Santa

------------------
ORGANIZERS
------------------
 - Sagindyk Urazayev: Core Developer, HEAD ORGANIZER
 - Andrew Moore: Assistant Core Developer, FRESHMAN SENATOR
 - Jacob McNamee: Assistant to the Core Developer, BEET FARMER

-------------------
PRIVACY NOTICE
-------------------
By agreeing to participate in this event, your email address will be revealed to one and only one person - your Secret Santa. Your email address can be found in the KU Open Directory: https://directory.ku.edu/. Under the Family Educational Rights and Privacy Act (FERPA), email addresses are classified as "directory information," which means they are considered public: https://www2.ed.gov/policy/gen/guid/fpco/ferpa/students.html

We know that be revealing your recipient's email address is not a pure secret santa but we are not allowed to share your residence address as it is a private information.
"""

def modify_message(message, toaddr):
    """
    This adds headers to strings
    """
    return "\n".join([
        "From: KU Secret Santa",
        f"To: {toaddr}"
    ]) + message

CONFIRMATION = """
Subject: Your KU Secret Santa confirmation!

HO HO HO!

Thank you for choosing to participate in KU Secret Santa! Please know that you are a cool guy/gal!

This message serves as a confirmation of your participation and there is no way back. (Though you can easily just bail out and I will add you on my naughty list for this year and all of the years to come until you will start believing in magic again)

Start looking for a gift that you will give to a total stranger that might become your friend! It might be a christmas hat, a toilet seat, brussel sprouts wrapped as chocolates! Let your imagination go wild!

Giving gifts is one of the best ways to start a relationship! I will reach back to you on December 2nd. At the end of the weekend, the email address of your special person will be revealed and let the magic of Christmas do the rest!

Thank you for participating in this wonderful event and have a great rest of the week! One week to go and you are done with your Fall semester!

XOXOXO,
KU Secret Santa

P.S. I am really sorry about the duplicate! My reindeer kicked my typewriter and it sent the message without a subject!
"""

SECRET_REVEAL = """
Subject: Your KU Secret Santa reveal!

HO HO HO!

Hey there! Hope you all had an amazing weekend because it is time to reveal your KU Secret Santa reveal! Hope you have a gift for them!

Your lucky recipient is: %EMAIL_ADDRESS%

The procedure should be simple:
 - Message them
 - Make a meeting
 - Give your present
 - Have an amazing time together!

Please share your presents using the #kusecretsanta hashtag and/or email your picture to me! A fine addition to my collection.

I really hope you enjoyed the first KU Secret Santa! This is the last message from me. See you next year!

With love,
KU Secret Santa

------------------
ORGANIZERS
------------------
 - Sagindyk Urazayev: Core Developer, HEAD ORGANIZER
 - Andrew Moore: Assistant Core Developer, FRESHMAN SENATOR
 - Jacob McNamee: Assistant to the Core Developer, BEET FARMER

"""

def modify_reveal(email):
    """
    Puts an email
    """
    return SECRET_REVEAL.\
        replace("%EMAIL_ADDRESS%", email)
