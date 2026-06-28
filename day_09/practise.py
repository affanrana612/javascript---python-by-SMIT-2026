name = input("Enter your name: ")
print("hello", name)
health = input("How are you ",name="? 1.fine  2.notfine")

if health == "1":
    print("congratulations you are fine")
elif health == "2":
    print("you need health checkup")
else:
    print("enjoy")
    
