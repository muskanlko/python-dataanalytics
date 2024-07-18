kahani =" "
while True:
    data=input("enter a story=>")
    if len(data)==0:
        print("The End!")
        break
    kahani +=data +"\n"

with open('story.txt','w')as file:
    file.write(kahani)
