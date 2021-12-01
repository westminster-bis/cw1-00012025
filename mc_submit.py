import main

class MC_submission:
    def __init__(self, student_id, module_name, reason, start_date, end_date):
        self.student_id = student_id
        self.module_name = module_name
        self.reason = reason
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return "Student ID: " + str(self.student_id) + "\nModule Name: " + str(self.module_name) + "\nReason: " + str(
            self.reason) + "\nStart Date: " + str(self.start_date) + "\nEnd Date: " + str(self.end_date)

#submitting mc case
def submit(cw_submission):
    global start_date, end_date
    main.new_two_lines()
    print("====== MC Submission ======")
    #this part for menu item #3. To submit new MC
    if cw_submission is None:
        while True:
            try:
                student_id = int(input("Enter Student ID: "))
                module_name = input("Enter Module Name (CSF, IMOB, WT, ISDS): ")
                if module_name.upper() in main.module_deadline.keys():
                    break
                else:
                    raise Exception("Module not found")
            except:
                print("Invalid Input")
    else:
        student_id = cw_submission.student_id
        module_name = cw_submission.module_name

    print("Enter Reason of MC \nP.S. You should provide real hard copy of proof of your reason to Registrar's Office")
    reason = input("Write details here: ")

    while True:
        start_date_str = input("Enter start date of MC (dd.mm.YYYY): ")
        try:
            start_date = main.parse_date(start_date_str)
        except:
            print("Enter in this format ===> (dd.mm.YYYY)")
        end_date_str = input("Enter end date of MC (dd.mm.YYYY): ")
        try:
            end_date = main.parse_date(end_date_str)
            break
        except:
            print("Enter in this format ===> (dd.mm.YYYY)")

    new_mc = MC_submission(student_id, module_name.upper(), reason, start_date, end_date)
    print("MC Successfully Submitted")

    main.mc_submissions.append(new_mc)
    return new_mc

#check if mc dates match the deadline
def check(cw_submission):
    global mc_submission
    mc_submitted = False

    # checking if mc submitted before
    if len(main.mc_submissions) != 0:
        for mc in main.mc_submissions:
            if mc.module_name.upper() == cw_submission.module_name.upper() and mc.student_id == cw_submission.student_id:
                mc_submission = mc
                mc_submitted = True
                break
    if not mc_submitted:
        mc_submission = submit(cw_submission)

    deadline = main.module_deadline.get(cw_submission.module_name.upper())
    if mc_submission.start_date <= deadline <= mc_submission.end_date:
        print("MC Accepted")
        return True
    else:
        print("MC Not Accepted")
        return False