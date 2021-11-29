import main


class CW_submission:
    def __init__(self, student_id,fullname, module_name, submission_date):
        self.student_id = student_id
        self.fullname = fullname
        self.module_name = module_name
        self.submission_date = submission_date

def submit():
    student_id = input("Enter Student ID: ")
    if not student_id.isnumeric():
        return False
    fullname = input("Enter Full Name: ")
    if fullname=="" or not fullname.isalpha():
        return False
    module_name = input("Enter Module Name (CSF, IMOB, WT, ISDS): ")
    if not module_name in main.module_deadline.keys():
        return False
    str_date = input("Enter the date you are submitting the coursework."
                     "\n(dd.mm.YYYY): ")
    if str_date == "" or str_date.isalpha():
        return False
    sub_date = main.parse_date(str_date)
    main.cw_submissions.append(CW_submission(student_id,fullname,module_name,sub_date))
    return True