age = input("What is your age? ")
with open("name.txt", "a") as f:
    f.write("\n" + age)
