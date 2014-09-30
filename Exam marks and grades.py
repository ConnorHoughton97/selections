#Connor Houghton
#30.09.14
#Exam marks and grades.
score = int(input("Please input your exam mark: "))

if 81 < score <= 100:
    print("You get an A grade.")
elif 71 < score <= 80:
    print("You get an B grade.")
elif 61 < score <= 70:
    print("You get an C grade.")
elif 51 < score <= 60:
    print("You get an D grade.")
elif 41 < score <= 60:
    print("You get an E grade.")
elif 0 < score <= 40:
    print("You get a U grade.")
else:
    print("invalid score")
