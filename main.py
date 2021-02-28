import somemodules

if __name__ == "__main__":

    #temp_in_c = somemodules.get_temperatur()

    #temp_in_k = somemodules.temp_c_into_k(temp_in_c)

    #print(temp_in_c, "°C das sind", temp_in_k, "°K")

    #menue_auswahl = somemodules.menue()
    #temp_in_x = somemodules.get_temperatur()

    f = open('text.txt', 'a')
    f.write("nananana")
    f.close()
    f = open('text.txt','r')
    print(f.read())


    klassea = somemodules.myclass()
    print("klasse",klassea.myclassadd(2,5))

    a = [1,2,3,4,5,6,7]

    for i in range(len(a)):
        print('i=',a[i])

    a.append(55)
    for i in range(len(a)):
        print('i=',a[i])

    lul=[0,1]

    for i in range(len(lul)):
        print('i=',lul[i])
        lul.append(len(lul))
        if len(lul) == 10:
            break