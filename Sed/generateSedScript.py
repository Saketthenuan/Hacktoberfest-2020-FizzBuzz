total = 100
current = 1
string = "s/fizzbuzz/"

while current <= total:
    if current % 3 == 0 and current % 5 != 0:
        string += "fizz\\n"
    elif current % 5 == 0 and current % 3 != 0:
        string += "buzz\\n"
    elif current % 15 == 0:
        string += "fizzbuzz\\n"
    else:
        string += str(current) + "\\n"
    current += 1

string = string.strip()
string += "/g"

sedScript = open("fizzbuzz.sed", "w")
sedScript.write(string)
sedScript.close()
