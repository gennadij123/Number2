#   Угадай число
import random   # Генерация случ.чисел

digit=0 # загаданное компом число
raz=0 # количество попыток
win=False  #   ugadal ?
play=True  #  Продолж игра ?
x=0  #  Число пользователя

maxball=0 # МАКС очков за сессию
startball = 100 # Стартовое кол-во очков
ballplay=0 # количество очков текущее в раунде
helpmy=0 # переменная,определяющая подсказку

# ===================================================

# Внешний цикл выполняется пока play истинно
while(play):
    
    #  ВВодим нижнюю границу с проверкой на число
    lowdigit =""
    while(not lowdigit.isdigit()): # Пока в строке не число выполняем цикл
        lowdigit =input( " нижняя граница чисел =" )
        if (not lowdigit.isdigit()):
            print( "."*27+" Сказано нижнюю границу !!!! ")
          
    lowdigit=int(lowdigit)

    #  ВВодим верхнюю границу с проверкой на число
    highdigit =""
    while(not highdigit.isdigit()):# Пока в строке не число выполняем цикл  
        highdigit=input( " верхняя граница= ")
        if (not highdigit.isdigit()):
            print( "."*27+" Сказано верхнюю границу !!!! ")
    highdigit=int(highdigit)
    
    startball=ballplay  #   очки  ставим на максимум
  
    print (startball)
    digit=random.randint(lowdigit,highdigit) #  Комп загадал число
    print (" комп загадал число,угадай !!!!!!!!!")
    print(f" Загаданное число: {digit}")
    # Внутренний цикл
    while( not win ):  #  цикл отвечает за один раунд
        x=""  # ВВодим переменную с проверкой на число 
        while (not x.isdigit()): # Пока в строке не число выполняем цикл
            x=input( f" Введите число от {lowdigit} до  {highdigit}  ")
            if (not x.isdigit()):
                print( "."*27+" ВВедите быстро число !!!! ")
        x=int(x)
    
        raz+=1
        print(" Попыток угадать уже  ",raz) #  Здесь всё понятно ))
        
        #  условия для подсказок-------------------------
        helpmy=abs(x-digit)#  модуль-всегда положительное число-разница
        if (helpmy<3): print( " жарища !!! ")
        elif (helpmy<5):print ("  горячо ! ! ")
        elif (helpmy<10) : print( "  тёпленько ")
        elif (helpmy<20): print ( " холодно " )
        else : print(  "  ДУБАК страшный " )
        #------------------------------------------------
        #  Рассчёт очков  игрока
        if (raz==7):
            ballplay-=10
            print ( " минус 10 баллов ))" )
        elif (raz==6):
            ballplay-=8
            print ( " минус 8 баллов ))" )
        elif(raz==5):
            ballplay-=4
            print ( " минус 4 балла ))" )
        elif(raz>2 and raz<5):
            ballplay-=2
            print ( " минус 2 балла ))" )
        print ( " У  ВАс осталось баллов : ", ballplay )
            
            
                             
        
        
        if (x>digit and x<=highdigit):
            print( " попробуй поменьше ")
        if (x<digit and x>=lowdigit ):
            print( " попробуй побольше ")

            
        if(x<lowdigit or x>highdigit):
            print(f" ДЯТЕЛ,ЧИСЛО должно быть больше{lowdigit} но меньше {highdigit}") 
        if (x==digit):
            print( " Угадал паршивец ")
            #  Сбрасываем win
            win = True
    if (input("ENTER- сыграть ещё,  0 - ВЫХОД")=="0" ):
        play=False
    else :
        win=False
        
   






