#Nicolas Franchi
#Dictionary Project
#9/24/18
import random
import sys
import time

storage = ["---Tomahawk---", "---Scav Vest---", "   ---PACA Soft Armor---", "---T-Bag---"]

def start_eft():
    start = True
    while start:
        escape = input('Do you want to play Escape From Tarkov? Yes or No ')
        if escape == 'yes':
            time.sleep(1)
            print("You have started escape from Tarkov ")
        if escape == 'no':
            print("Shutting down program")
            sys.exit()

def menu_eft():
    menu = input("----------Start a raid or look into your inventory?---------- ")
    if menu == 'inventory':
        print("---Please wait while we load your inventory---")
        time.sleep(1)
        print(" ... ")
        time.sleep(1)
        print(" ... ")
        time.sleep(1)
        print("Your inventory has been loaded")
        print("These are the items in your inventory %s" % storage)
    elif menu == 'start raid':
        raid = input("Would you like to start a raid as a --Scav-- or --P.M.C-- ")
        if raid == 'pmc':
            print("You have chossen P.M.C, you will spawn with the gear in your inventory that is  equiped, if you die during the raid you will lose the gear you brought to the   raid")
        elif raid == 'scav':
            print("You have chossen Scav, you will spawn with  a Scav vest and a AKS-74U with PS ammo")

def raid_eft():
    raid = input("Where will you like to loot -Doorms-Warehouses-Private Storage Area-
                 if raid == 'doorms':
                     doorms_choice = input("You make your way to the enterance, but you hear gunshots in the doorms, will you engage or run away?"
                           if doorms_choice == 'engage':
                                print("You run in you see a PMC looting a body you empty 10 bullets into him and he looks at you and takes you down with one shot... he was a hacker!!!")
