animals = ["monke","penguin","cat","bear","panda","puma"]

animals.append("polor bear")
print(animals)
animals.remove("penguin")
print(animals)
animals.pop(1)
print(animals)
animals.insert(1,"line")
print(animals)
animals.sort()
print(animals)

search = input ("what animal do you want to search for?")
if search in animals:
    print(f"{search} is in my list!")
else:
    print(f"{search} is not in my list:(")

for a in animals:
    print(f"I have a {a} in my list")


