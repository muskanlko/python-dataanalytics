kahani =" "
while True:
    data=input("enter a story=>")
    if len(data)==0:
        print("The End!")
        break
    kahani +=data +"\n"

print("The real story:")
print(kahani)