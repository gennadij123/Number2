
s=int(input( " Введите количество повторений " ))
for i in range(s):
    speed = int(input( " ВВедите скорость " )) # вводим скорость
    if ( speed>60 and speed <250):
        print(" превышаешь,гад" )
    elif ( speed <1): print (" стоим ")
    elif ( speed >= 250 ): print ( " охуел так гнать ")
    else :
        print (" езда по правилам ")
    

            
