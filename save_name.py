name = input("What is your name? ")
with open("name.txt", "w") as f:
    f.write(name)
