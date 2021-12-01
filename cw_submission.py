from datetime import timedelta

from main import parse_date, module_deadline
import mc_submit

class CW_submission:
    def __init__(self, student_id,fullname, module_name, submission_date):
        self.student_id = student_id
        self.fullname = fullname
        self.module_name = module_name
        self.submission_date = submission_date

def submit():
    student_id_str = input("Enter Student ID: ")

    if not student_id_str.isnumeric():
        return None
    student_id = int(student_id_str)
    #get full name
    fullname = input("Enter Full Name: ")
    #get module name and validate
    module_name = input("Enter Module Name (CSF, IMOB, WT, ISDS): ")
    if not module_name.upper() in module_deadline.keys():
        return None
    #get submission date and validate
    str_date = input("Enter the date you are submitting the coursework."
                     "\n(dd.mm.YYYY): ")
    if str_date == "" or str_date.isalpha():
        return None
    try:
        sub_date = parse_date(str_date)
    except:
        print("Enter in this format ===> (dd.mm.YYYY)")
        return None
    #append to the list of submissions
    new_submission = CW_submission(student_id, fullname, module_name, sub_date)
    return new_submission


def check(cw_submission):
    deadline = module_deadline.get(cw_submission.module_name.upper())
    submission_date = cw_submission.submission_date
    if deadline < submission_date:
        #On time -> No
        if submission_date - deadline <= timedelta(days=1):
            #Within 24 hours?
            within_24hours(cw_submission)

        #Within 5days -> Yes
        elif submission_date - deadline <= timedelta(days=5):
            within_5days(cw_submission)

        else:
            #Within 5 days -> No
            after_5days(cw_submission)
    elif deadline >= submission_date:
        #On time -> Yes
        full_mark()

#function for printing full mark
def full_mark():
    print("Your score is full mark of your assignment. No penalty")

#function to handle submissions within one day
def within_24hours(cw_submission):
    if check_valid_reason():
        mc_submit.check(cw_submission)
    else:
        print("Minus 10 marks from overall mark but not below 40")

#function to handle cases within 5 days
def within_5days(cw_submission):
    if check_valid_reason():
        mc_submit.check(cw_submission)
    else:
        print("Mark: 0")

#function to handle submissions after 5 days
def after_5days(cw_submission):
    if check_valid_reason():
        mc_submit.check(cw_submission)
    else:
        print("Mark: 0")

def check_valid_reason():
    while True:
        print("Is there a valid reason?")
        answer = input("Yes/No\n")
        if answer.upper() == "YES":
            return True
        elif answer.upper() == "NO":
            return False
        else:
            print("Wrong Input. Type Yes or No!")