# Exercise 7-2: Dictionary of lists

courses = open("courses2.txt") # open courses2.txt file 

def BuildDict(courses): # BuildDict function
    course_dict = {} # create empty dict with int as key and list as value
    capra_courses = []
    for line in courses:
        course_parts = line.split()
        if course_parts[0] in course_dict.keys(): # if key in dict
            course_dict[course_parts[0]].append(course_parts[1]) # add new value to existing value list
        else: 
            course_dict[course_parts[0]] = [course_parts[1]] # add key value pair from line
    inls523_instructors = []
    for key, value in course_dict.items(): # for pairings in items
        if key == "523": # if key is 523
            inls523_instructors.append(value) # add value to 523 instructors list 
        if 'Capra' in value: # if Capra in value
            capra_courses.append(key) # append key to courses list 
    return course_dict.keys(), course_dict.values(), inls523_instructors, capra_courses

print(BuildDict(courses))
