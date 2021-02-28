def ausgabe(n):
    for x in range(n):
        print(x)

def temp_c_into_k (c):
    return c+273.15

def get_temperatur ():
    while True:
        temp_x = input("Gib bitte eine Temperatur ein ")
        try:
            temp_x = float(temp_x)
            return temp_x
        except ValueError:
            print("Das ist keine gültige Eingabe für eine Temperatur !")

def menue ():
    while True:
        auswahl = input("Was wollen Sie tun ? \n1. °C -> °K\n2. °K -> °C\n3. °C -> °F\n4. °F -> °C\n5. °K -> °F\n6. °F -> °K\n")
        for i in range(1,7):
            print("i =",i)
            if auswahl == str(i) or auswahl == str(i)+".":
                return i
            else:
                print("Nope")
        print("Das wahr keine gültige Eingabe !")

def temp_calculator(mode,temp):
    if mode == 1:   #C in K
        return temp + 273.15
    elif mode == 2: #K in C
        return temp - 273.15
    elif mode == 3: #C in F
        return (temp*1.8)+32
    elif mode == 4: #F in C
        return (temp-32)/1.8
    elif mode == 5: #K in F
        return temp
    elif mode == 6: #F in K
        return (temp-273.15)*1.8+32

class myclass():
    classvalue=10
    def myclassadd(self,a,b):
        return a+b+self.classvalue


if __name__ == "__main__":
    print("aaaaaa")