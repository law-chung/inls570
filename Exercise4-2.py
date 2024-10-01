# Exercise 4-2 

inv = []
while True:
    cmd = input("Enter command: ")
    if cmd == 'exit':
        break
    if cmd == 'list':
        print (" ", inv)    
    else:
        cmd_parts = cmd.split()
        cverb = cmd_parts[0]
        cnoun = cmd_parts[1]
        if cverb == 'buy':
            inv.append(cnoun)
        if cverb == 'sell':
            if cnoun not in inv: 
                print(f'You do not have {cnoun}')
            elif cnoun in inv: 
                inv.remove(cnoun)