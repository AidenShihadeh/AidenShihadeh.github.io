from random import*
import time
import sys
n=0 #this is less than > and this is more than < and is not means if it isnt in there
health=200
backpack  = []
level=0
done = 0
alive = 1
xp=0
magic=100
def sleep():
    time.sleep(0.3)
def diceRoll():
    num=randint(1,10)
def rolls(): 
    aws = randint(1,10)
def shop():
    global gold
    global choice
    try:
        print ("Would You Like To Buy Anything From My Shop")
        choice = int(input("1.Yes\n2.No"))
    except ValueError:
        print("Lets Try Something Else")
        shop()
    try: #Check To see if there is error,if error go to except
        while choice == 1:
            print ("What Would You Like To Buy?")
            choice2 = int(input("1.A Burger 10G\n2.A Orange Juice Carton 10g\n3.A Super Potion 30G\n4.A Super Mana Potion 30G\n5.A Revivial Potion 100G\n6.Leave\n"))
            if choice2 == 1 and "Burger" not in backpack and gold > 10:
                 print("Here You Go")
                 sleep()
                 print("BURGER GET")
                 sleep()
                 backpack.append("Burger")
                 gold-=10
            if choice2 == 2 and "Orange Juice" not in backpack and gold > 10:
                 print("Here You Go")
                 sleep()
                 print("Orange Juice GET")
                 sleep()
                 backpack.append("Orange Juice")
                 gold-=10
            if choice2 == 3 and "Super Potion" not in backpack and gold > 30:
                 print("Here You Go")
                 sleep()
                 print("Super Potion GET")
                 sleep()
                 backpack.append("Super Potion")
                 gold-=30
            if choice2 == 4 and "Super Mana Potion" not in backpack and gold > 30:
                 print("Here You Go")
                 sleep()
                 print("Super Mana Potion GET")
                 sleep()
                 backpack.append("Super Mana Potion")
                 gold-=30
            if choice2 == 5 and "Revival Potion" not in backpack and gold == 100:
                 print("Here You Go")
                 sleep()
                 print("Revival Potion GET")
                 sleep()
                 backpack.append("Revival Potion Potion")
                 gold-=100
            if choice2 == 6:
                break
                print("Goodbye")
            elif gold < 10:
               print ("You Cannot Afford That Item")
               sleep()
    except ValueError: #Error Handler
         print("Please Enter A Valid Number")
         shop()
print("Hello Adventurer")
sleep()
print("This Will Be Your Adventure Full Of Action")
name = input("Enter Your Name Adventurer ")
sleep()
if name == "Aiden":
    gold = 100
    shop()
if name == "Robbie Rotten":
    print("We Are Number One")
if name == ("Rodrigo"):
    print ("According To All Known Laws Of aviation a bee should not be able to fly")
if name == "Aiden2":
    backpack = ["Gun","Clock","Health Potion","Water Bottle","Wand","Magic Potion"]
print(name,"That is a mighty name")
luck = randint(1,10)
dexterity = randint(1,10)
strength = randint(1,10)
print ("Your Luck Is",luck,"Your Dexterity is",dexterity,"And finally your stength is",strength,)
print ("What 3 items do you want to take with you")
predefined = ["1.Gun","2.Clock","3.HPotion","4.Water Bottle","5.Wand","6.MPotion"]
for items in predefined:
    print("Item:",items)
picked = int(input("Pick You Item "))
picked2 = int(input("Pick Your Second Item "))
picked3 = int(input("Pick Your Third Item "))
if picked == 1 or picked2 == 1 or picked3 == 1:
    backpack.append("Gun")
if picked == 2 or picked2 == 2 or picked3 == 2:
    backpack.append("Clock")
if picked == 3 or picked2 == 3 or picked3 == 3:
    backpack.append("HealthPotion")
if picked == 4 or picked2 == 4 or picked3 == 4:
    backpack.append("WaterBottle")
if picked == 5 or picked2 == 5 or picked3 == 5:
    backpack.append("Wand")
if picked == 6 or picked2 == 6 or picked3 == 6:
    backpack.append("MagicPotion")
print ("Let Us Begin Your Adventure Young Adventutrer")
sleep()
print ("You Awake In A Forest")
sleep()
print ("You See a Goblin")
sleep()
print ("What Do You Do")
print ("1. Attempt To Sneak Round")
print ("2. Prepeare To Fight")
choice = int(input(""))
if "Wand" and "Gun" not in backpack:
    choice = 1
if choice == 2:
    print ("You Sneak Towards The Goblin And Attack It From Behind")
    if "Gun" in backpack and alive == 1:
        choice = input("Do You Want Combo With Your Gun? y/n ")
        if choice == ("y"):
            aim = randint (1,100)
            if aim < 90:
                print ("You Kill The Goblin")
                xp = randint(1,20)
                print ("You Got",xp,"Xp")
                alive = 0
            if aim > 90:
                print ("You Miss")
                print ("The Goblin Notices You And Attacks")
                damage = randint(1,50)
                health-=damage
                print ("He Did",damage,"Damage To you, You Are Now At",health,"hp")
                
    
    if "Wand" in backpack and alive == 1:
        choice = input("Do You Want To Combo With your Wand y/n ")
        if choice == ("y") or choice == ("Y"):
            print ("You Kill The Goblin")
            xp += randint(1,20)
            magic -= 10
            print ("You Got",xp,"Xp")

if choice == 1:
    print ("You Attempt to sneak round")
    if luck > 5:
        chance = randint(75,100)
    else:
        chance = randint(1,100)
    if chance > 60:
        print ("You Succsefully Sneak By The Goblin")
    else:
        print ("You Got Caught")
        damage = randint(30,100)
        health -= damage
        print ("The Goblin Hit You Over The Head With A Mace He Did",damage,('Damage to You \nYou now have'),health,("Health Remaining"))
        print ("You RUUUUN AWAY")
        
if xp > 10:
    lvlup = int(input("You Leveled Up What Would You Like To Level \n1.Luck \n2.Dexterity \n3.Strength\n"))
    if lvlup == 1:
        luck+=1
        print (("Your Luck Is Now"),luck,)
        xp = 0
        level += 1
    if lvlup == 2:
        dexterity+=1
        print (("Your Dexterity Is Now"),dexterity,)
        xp = 0
        level += 1
    if lvlup == 3:
        strength+=1
        print (("Your Strength Is Now"),strength,)
        xp = 0
        level += 1
    
print ("You Continue On Your Journey")
print ("You See A Huge Temple")
active = 1
while active == 1:
    try:
        choice = int(input("What Would You Like To Do\n1.Check Around\n2.Items\n3.Continue on your journey\n"))
        if choice == 1:
            print("You See Nothing Of Intrest")
        if choice == 2:
           print (*backpack)
        sleep()
        if "Clock" in backpack:
                cchoice = input("Do You Want To look at the clock? y/n")
                if cchoice == "y" or choice == "Y":
                    print ("The Time in seconds since 1960 is",time.time(),("Or 46.9039959567985747 Years"))
          
        if "HealthPotion" in backpack:
            bchoice = input("Do You Want To Restore Your Mana By Drinking The HealthPotion? y/n")
            if bchoice == "y" or bchoice == "Y":
                health = 200
                print ("Your Health Is Now At 100")
                backpack.remove("HealthPotion")
                done = 1
        if "HealthPotion" and "Clock" not in backpack and choice == 2:
            print ("You Have No Items Of Intrest")
        
        if choice == 3:
            choice = 0
            active = 0
    except ValueError:
        print("Lets Try Something Else")
print ("You Walk Into The Temple")
print ("You See A Snake Pit")
print ("You Attempt To jump over")
chance = "Hi"
rollc = randint(1,10)
print ("Guess The Number From One To Ten")
chances = input("Is The Number Lower Or Higher Than 5 \nLower Or Higher Only ")
if chances == "lower" and rollc < 5:
        print ("You Are Correct")
        print ("You Jumped Over And Bairly Got To The Other Side")
        rolling = 0

if chances == "higher" and rollc > 5:
       print ("You Are Correct")
       print ("You Jumped Over And Bairly Got To The Other Side")
       rolling = 0
       
if chances == "higher" and rollc < 5:
       print ("You Fell Into Snake Pit And Died")
       time.sleep(1)
       exit()

if chances == "lower" and rollc > 5:
       print ("You Fell Into Snake Pit And Died")
       time.sleep(1)
       exit()
if chances == "cheat":
    print ("You Cheat")
print ("You See A Shop")
print ("What Would You Like To buy?")
print ("The Items Are")
sleep()
print (" 1.HealthPotion \n 2.MagicPotion \n 3.A Gun")
choice = int(input(""))
if choice == 1:
    backpack.append("HealthPotion")
if choice == 2:
    backpack.append("MagicPotion")
if choice == 3:
    backpack.append ("Gun")
print ("Goodbye")
print ("You Encounter a split Path")
print ("What Do You Do")
pick = 0
sleep()
pick = int(input("1.Take The Left Path \n2.Take The Right Path\n"))
if pick == 1:
    print ("A Boulder Comes And Hits You")
    print ("You Died")
    exit()
if pick == 2:
    print ("You Get By Safely")
if pick == 3:
    print ("No")
print ("You See A Room With A Big Diamond In The Middle")
sleep()
choice = input("Do you want to grab the diamond (Yes/No)")
if choice == "yes":
             print("You Grab The Diamond")
             sleep()
             backpack.append("Diamond")#Adds Diamond To Backpack
             print("Diamond GET")
             print ("You See A boulder Coming For you")
             sleep()
             print("You Bairly Got Out")
             health-=100
             print("You Cut Your Arm On A Spike Trap -100 health")
if choice == "no":
             print ("You Walked Out Of The Cave")
             print ("You Found A Health Potion")
             backpack.append("HealthPotion")

if "Diamond" in backpack:
    sleep()
    print("You Look At The Diamond More Closely")
    time.sleep(1)
    print("Its a FAKE diamond!")
    time.sleep(0.4)
    print("You Throw Away The Phony Diamond!")
    backpack.remove("Diamond")
print("You see a village in the distance")
sleep()
print("You Walk Towards The Village")
sleep()
print("You Find a Golden Nugget On The Way")
backpack.append("Golden Nugget")
print (backpack)
print("You See A Shop In The Village")
print("Hello Welcome To My Shop")
print("That Is A Quite Nice Nugget Of Gold You Have")
choice = int(input("Would You Like To Sell It To Me? \n1.Yes\n2.No\n"))
if choice == 1 or choice == 2:
    if choice == 2:
        print("Too Bad Im Taking It")
    print("Here You Are 100 Gold Coins")
    gold = 100
    backpack.remove("Golden Nugget")
shop()
