
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
