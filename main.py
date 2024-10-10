print("Welcome to Voter Eligibility Checker.")
print("Lets see fi you are eligable to vote")

age = int(input("Please enter your age: "))
citizen = input("Are you a legal citizen of the US? (y/n): ")
registered = input("Are you registered to vote? (y/n): ")
jail = input("Are you currently in jail? (y/n): ")

if age >= 18 and citizen == "y" and registered == "y" and jail == "n": 
  eligable = True
  print("You are eligable to vote.")
else:
  eligable = False
  print("You are ineligable to vote.")
