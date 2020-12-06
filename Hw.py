def name_check():
    student_list = ["barine eviren"]
    count_fail=0
    while count_fail != 3 :
        name = input("Please enter your name and surname:")
        if name in student_list :
            print("Welcome", name)
            return 0
        elif count_fail ==2 :
            count_fail +=1
            print("Please try again later")
        else :
            count_fail +=1
            print("Try again")
def courses_choices_grades() :
    c = input("Please enter your lessons with a space:")
    clist= c.split()
    if 3<= len(clist) <= 5 :
        x=input("Which course did you take exams?:")
    else :
        return ("You failed in class")
    keys= ["Midterm","Final","Project"]
    d = dict.fromkeys(keys)
    c=1
    last_grade = 0
    for key,val in d.items():
        val=input("Enter your "+str(key)+"'s grade")
        if c ==1 :
            d[key] = float(val)*0.3
            last_grade += d[key]
            c+=1
        elif c==2 :
            d[key] = float(val)*0.5
            last_grade += d[key]
            c+=1
        else :
            d[key] = float(val)*0.2
            last_grade += d[key]
    if last_grade >= 90 :
        return ("You get AA")
    elif 70<=last_grade<90:
        return ("You get BB")
    elif 50<=last_grade<70 :
        return ("You get CC")
    elif 30<=last_grade<50 :
        return ("You get DD")
    else :
        return ("You get FF and you failed in this course")

if name_check() == 0 :
    courses=[]
    for i in range(1,6):
        x = input("Enter your "+str(i)+". courses")
    courses.append(x)
    print(courses_choices_grades())
