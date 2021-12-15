
for i in range(1, 25): 
    try:
        file = open("src/day-" + str(i) + ".py").read()
        print("\nAdvent of Code Day: " + str(i))
        exec(file)
    except: 
        break
