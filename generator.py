#Windows Installation info
#Ensure python is installed and added to path
#Create a shortcut at "C:\Windows\System32\cmd.exe /k python ./generator.py"
#Double click the shortcut to run the program

#Mac installation info 
#Ensure python is installed properly
#Create a shortcut and add the action of running generator.py
#Open the shortcut to run the program

#Gather citation info
#Case name
case_name = input("Case name:")
case_name = f"\033[4m{case_name}\033[0m"
case_name = case_name + ","

#Shortened case name
short_name = input("Shortened case name:")
short_name = f"\033[4m{short_name}\033[0m"
short_name = short_name + ","

#Reporter name and issue
reporter_name = input("Reporter name:")
reporter_issue = input("Reporter volume:")

#Case and pincite pages
case_page = input("Case page:")
case_page = case_page + ","
pincite_page = input("Pincite page (Leave blank if citing whole case):")

#Court name
court_name = input("Court name:")
if court_name:
    court_name = "(" + court_name

#Case date
case_date = input("Case date:")
case_date = case_date + ")"

# Print full case citation
print("\nFull citation:")
if pincite_page:
    if not court_name:
        case_date = "(" + case_date
        print(case_name, reporter_issue, reporter_name, case_page, pincite_page, case_date)
    print(case_name, reporter_issue, reporter_name, case_page, pincite_page, court_name, case_date)
else:
    print(case_name, reporter_issue, reporter_name, case_page, court_name, case_date)
print()

# Print shortened citation
print("Shortened citation:")
if pincite_page:
    print(short_name, reporter_issue, reporter_name, "at", pincite_page)
else:
    print(short_name, reporter_issue, reporter_name, case_page)
print()

# Print no name shortened citation
print("No-name shortened citation:")
if pincite_page:
    print(reporter_issue, reporter_name, "at", pincite_page)
else:
    print(reporter_issue, reporter_name, case_page)
print()

# Print Id. citation
print(f"\033[4m{'Id.'}\033[0m citation:")
if pincite_page:
    print(f"\033[4m{'Id.'}\033[0m at", pincite_page)
else:
    print(f"\033[4m{'Id.'}\033[0m at", case_page)
print()
#Farewell to user
print("Good luck with your legal work! Keep an eye on the punctuation!")
print()
