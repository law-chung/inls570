# Exercise 7-1: Reading into a dictionary

courses = open("courses1.txt")

def BuildDict(courses):
    course_dict = {}
    for line in courses:
        cline = line.split()
        course_dict[cline[0]] = cline[1]
    return course_dict

def courses_info(cdict):
    print(cdict.keys())
    print(cdict.values())
    capra_courses = []
    for c in cdict:
        if cdict[c] == 'Capra':
            capra_courses.append(c)
    print(capra_courses)

courses_info(BuildDict(courses))