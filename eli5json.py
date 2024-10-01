# Exercise: reddit ELI5 JSON 
import json

fp = open("eli5_sm.json", "r")
s = fp.read()
j = json.loads(s)

i = 0
while i < len(j):
    print('------- Title -------')
    if 'title' in j[i][1]:
        print(j[i][1]['title'])
    print('------ Comments --------')
    if 'comments' in j[i][1]:
        x = 0
        while x < len(j[i][1]['comments']):
            print(j[i][1]['comments'][x]['body'][0][:30])
            x += 1
    i += 1