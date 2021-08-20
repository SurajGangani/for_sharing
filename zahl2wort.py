############# define func #############

def zahl2wort():
    
    # define initial data as dictionary -------------------------------------------
    d = {0: "null", 1: "eins", 2: "zwei", 3: "drei", 4: "vier", 5: "fünf", 6: "sechs", 7: "seben", 8: "acht", 9: "neun", 10: "zehn", 
    11: "elf", 12: "zwölf", 13: "dreizehn", 14: "vierzehn", 15: "fünfzehn", 16: "sechzehn", 17: "siebzehn", 18: "achtzehn", 19: "neunzehn",
    20: "zwanzig", 30: "dreißig", 40: "vierzig", 50: "fünfzig", 60: "sechzig", 70: "siebzig", 80: "achtzig", 90: "neunzig",
    100: "einhundert"}
    
    ############# get user input and call func #############

    # get user input -------------------------------------------
    num = int(input("Bitte geben Sie eine Zahl zwischen 0 und 100 ein : "))
    
    # main loop -------------------------------------------------
    for i in d:
        if num == i:
            to_return = d[i]
            is_valid = True
            break
        elif (num < i) and (num != 0):   
            y = num % 10
            x = num - y
            to_return = d[y] + "und" + d[x]
            is_valid = True
            break
        else:
            is_valid = False
    
    # to output ------------------------------------------------
    if is_valid:
        return print(str(num) + " = " + to_return[0].upper() + to_return[1:]) 
    else:
        print("Die eingegebene Zahl liegt nicht im Bereich 0 bis 100.")
        return zahl2wort()
        
        
        
############# call func #############
zahl2wort()