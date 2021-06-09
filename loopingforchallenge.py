farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#Function 1
def function1():
    for farm in farms:
        name = farm["name"].lower()
        if name == "ne farm":
            for animal in farm["agriculture"]:
                print(animal)
                
function1()  
print("end of function 1\n")
#Function 2
def function2():
    farm_num = 0
    while not farm_num:
        farm_num = int(input("Please enter a number to choose a farm\n1) NE Farm\n2) W Farm\n3) SE Farm\n>"))
        num = farm_num - 1
        farm = farms[num]
        for thing in farm["agriculture"]:
            print(thing)

function2()
print("end of function 2\n")

#Function 3
def function3():
    farm_num = 0
    while not farm_num:
        farm_num = int(input("Please enter a number to choose a farm\n1) NE Farm\n2) W Farm\n3) SE Farm\n>"))
        num = farm_num - 1
        farm = farms[num]
        for thing in farm["agriculture"]:
            if thing == "carrots" or thing == "celery":
                continue
            else:
                print(thing)

function3()
print("end of function 3\n")

farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

def functionBonus():
    farm_num = 0
    while not farm_num:
        count = 0
        farm_num = int(input("Please enter a number to choose a farm\n1) SE Farm\n2) NE Farm\n3) E Farm\n4) W Farm\n>"))
        num = farm_num - 1
        farm = farms[num]
        for thing in farm["agriculture"]:
            if thing == "carrots" or thing == "celery" or thing == "bananas" or thing == "apples" or thing == "oranges":
                continue
            else:
                print(thing)
                count += 1
        if count == 0:
          print("No Animals on this farm")

functionBonus()
print("end of function bonus")

