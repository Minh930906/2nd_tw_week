num=100
a=0
o_door = ["close"]*num
for a in range(num):
    for b in range(a,num,a+1):
        if o_door[b] == "open":
            o_door[b] = "close"
        elif o_door[b] == "close":
            o_door[b] = "open"

doors = []
for a in range(num):
    if o_door[a]=="open":
        doors.append(a+1)

print("The following doors are open: ",doors)
   
    
    