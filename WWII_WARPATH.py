from random import*
HomeNation = ["spain", "usa", "uk", "france"]
#HomeNation.lower()
EnemyNation = ["nazi germany", "italy", "vichy france", "japan"]
#EnemyNation.lower()
Century = ["21st century", "20th century", "1800s"]
#Century.lower()
Ability21 = ["nuke", "missile", "shotgun battalion", "hospitalize", "barricade"]
#Ability21.lower()
Ability20 = ["nuke", "aircrafts", "shotgun battalion", "hospitalize", "barricade"]
#Ability20.lower()
Ability18 = ["cannons", "naval fleet", "shotgun battalion", "hospitalize",
             "barricade"]
#Ability18.lower()
Ab21Ener = {"nuke" : 100, "missile" : 15, "shotgun battalion" : 7,
             "hospitalize" : 7, "barricade" : 6}
Ab21Dam = {"nuke" : 40, "missile" : 10, "shotgun battalion" : 15,
           "hospitalize":0, "barricade":0}
Ab21Heal = {"nuke" : 0, "missile" : 0, "shotgun battalion" : 0,
             "hospitalize" : 15, "barricade" : 0}
'''
Ab21def = {"nuke" : 0, "missile" : 0, "shotgun battalion" : 0,
             "hospitalize" : 0, "barricade" : 10}
'''
Ab20Ener = {"nuke" : 100, "aircrafts" : 15, "shotgun battalion" : 7,
            "hospitalize" : 7, "barricade" : 6}
Ab20Dam = {"nuke" : 40, "aircrafts" : 10, "shotgun battalion" : 15,
           "hospitalize" : 0, "barricade" : 0}
Ab20Heal = {"nuke" : 0, "aircrafts" : 0, "shotgun battalion" : 0,
             "hospitalize" : 15, "barricade" : 0}

Ab18Ener = {"cannons" : 100, "naval fleet" : 15, "shotgun battalion" : 7,
             "hospitalize" : 7, "barricade" : 6}
Ab18Dam = {"cannons" : 40, "naval fleet" : 10, "shotgun battalion" : 15,
           "hospitalize" : 0, "barricade" : 0}
Ab18Heal = {"cannons" : 0, "naval fleet" : 0, "shotgun battalion" : 0,
             "hospitalize" : 15, "barricade" : 0}
'''
AbRegen = {"hospitalize" : 10}
Regenerates your health
AbDefen = {"barricade" : -10}
Removes damage from the opponents attack
Barricade subtracts ten damage from the enemy's next move
'''
win = False
lose = False
yourbarri = False
Enembarri = False
YourHeal = 100
EnemHeal = 150

YourEner = 150
EnemEner = 200

EndConditions = [EnemHeal, EnemEner, YourHeal, YourEner]
ValidHome = False
ValidEnemy = False
ValidTime = False
lowenermode = False
lowenermode = False
while ValidHome == False:
    Nation = (input("Pick your Nation. You can choose between UK, USA, France, and Spain "))
    Nation.lower()
    if Nation.lower() not in HomeNation:
        print("That isn't a Valid Country")
    if Nation.lower() in HomeNation:
        ValidHome = True
while ValidEnemy == False:
    Enemy = (input("Pick your enemy. You can choose between Nazi Germany, Italy, Japan, Vichy France "))
    Enemy.lower()
    if Enemy.lower() not in EnemyNation:
        print("That isn't a valid enemy")
    else:
        ValidEnemy = True
while ValidTime == False:
    Time = (input("Choose the time between the 21st century, the 20th century, or the 1800s "))
    Time.lower()
    if Time.lower() not in Century:
        print("That isn't a valid time")
    else:
        ValidTime = True
#Select century
if Time.lower() == "21st century":
    Ablist = Ability21
    Enerlist = Ab21Ener
    Damlist = Ab21Dam
    Heallist = Ab21Heal
elif Time.lower() == "20th century":
    Ablist = Ability20
    Enerlist = Ab20Ener
    Damlist = Ab20Dam
    Heallist = Ab20Heal
elif Time.lower() == "1800s":
    Ablist = Ability18
    Enerlist = Ab18Ener
    Damlist = Ab18Dam
    Heallist = Ab18Heal
print("This is a World war simulator. To play, you will be given a set of"
      + " attacks. When you use, an offensive attack, it will reduce from"
      + " you energy and from your enemy's health. The goal is to reduce the"
      " enemy's health to zero. You cant run out of energy though. Good Luck,"
      +" and let the battle begin.\n")
#Century = ["21st Century", "20th Century", "1800s"]
#Ability21 = ["Nuke", "Missile", "Shotgun Battalion", "Hospitalize", "Barricade"]


while win == False and lose == False:
    Validturn = False
    while Validturn == False:
        if Time == "21st century":
            yourturn = input("Choose between the moves of Nuke, Missile, " +
                             "Shotgun Battalion, Hospitalize, and Barricade,"+
                             " beware however that each move casts energy depending" +
                             " on the move\n")
        elif Time == "20th century":
            yourturn = input("Choose between the moves of Nuke, Aircrafts, " +
                             "Shotgun Battalion, Hospitalize, and Barricade,"+
                             " beware however that each move casts energy depending" +
                             " on the move\n")
        elif Time == "1800s":
            yourturn = input("Choose between the moves of Cannons, Naval Fleet, " +
                             "Shotgun Battalion, Hospitalize, and Barricade,"+
                             " beware however that each move casts energy depending" +
                             " on the move\n")
        yourturn.lower()
        if yourturn.lower() in Ablist or yourturn.lower() == "w":
            Validturn = True
            #if yourturn.lower() == "w":
            # win = True
            if yourturn.lower() in Ablist:
                if yourturn.lower() == "barricade":
                    yourbarri = True
                if Enembarri == True:
                    EnemHeal -= Damlist[yourturn.lower()] - 15
                else:
                    EnemHeal -= Damlist[yourturn.lower()]
                YourEner -= Enerlist[yourturn.lower()]
                YourHeal += Heallist[yourturn.lower()]
                print("Your Health: " + str(YourHeal) + " Enemy Health: " + str(EnemHeal))
                print("Your Energy: " + str(YourEner) + " Enemy Energy: " + str(EnemEner)+ "\n")
        else:
            print("That isn't a valid move")

        
    if YourHeal <= 0:
        lose = True
        break
    if EnemHeal <= 0:
        win = True
        break
    if YourEner <= 0:
        lose = True
        break
    if EnemEner <= 0:
        win = True
        break
                
    
    if EnemEner <= 100:
        lowenermode = True
    if EnemHeal <= 40:
        lowenermode = True
    #AI picks move
    Validturn = False
    while Validturn == False:
        Move = choice(Ablist)
        if lowenermode == True and Move.lower() == "nuke":
            Validturn = False
        else:
            Validturn = True
    print(Enemy + " has played the move " + Move + "!\n")
    #AI has picked move
    if Move.lower() == "barricade":
        Enembarri = True
    if yourbarri == True:
        YourHeal -= Damlist[Move.lower()] - 15
    else:
        YourHeal -= Damlist[Move.lower()]

    EnemEner -= Enerlist[Move.lower()]
    EnemHeal += Heallist[Move.lower()]
    print("Your Health: " + str(YourHeal) + " Enemy Health: " + str(EnemHeal))
    print("Your Energy: " + str(YourEner) + " Enemy Energy: " + str(EnemEner))
    yourbarri = False
    if YourHeal <= 0:
        lose = True
    if EnemHeal <= 0:
        win = True
    if YourEner <= 0:
        lose = True
    if EnemEner <= 0:
        win = True
if win == True:
    print("You Won, Congrats!")
if lose == True:
    print("Oh no! You Lost!")
'''
YourHeal = 100
EnemHeal = 150 

YourEner = 150
EnemEner = 200
'''     
#answer = randrange(len(fortune))
#mylist[randrange(0,len(mylist))]
#Enerlist = {"Nuke" : 100, "Missile" : 5, "Shotgun Battalion" : 7,
            # "Hospitalize" : 7, "Barricade" : 6}
#Damlist = {"Nuke" : 40, "Missile" : 10, "Shotgun Battalion" : 15}
'''
After you first move, this mechanism will do an attack and be able to know that
you shouldn't be able to heal in the beginning, after that, it will pick a random
attack to use until its energy gets low enough to where it knows that certain
attacks will mean it loses all of its energy and so it will try and conserve
energy by doing attacks that take less energy. It will need to know its energy
health so that when its health is low, it knows to heal and and when energy is
low, it knows to conserve energy
'''
