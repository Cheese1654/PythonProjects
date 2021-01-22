from pakuri import Pakuri
from hashlib import md5


def main():
    print("Welcome to Pakudex: Let's Go!\n")
    Pakudex = []
    while True:

        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Remove Pakuri")
        print("5. Change Pakuri Level")
        print("6. Exit")

        choice = input("\nWhat would you like to do? ")
        if choice == '1':
            if len(Pakudex) == 0:
                print("\nNo Pakuri in Pakudex yet!\n")
            else:
                print("\nPakuri in Pakudex:")
                Pakudex.sort(key=lambda x: x.get_name())
                count = 1
                for i in Pakudex:
                    print(str(count) + ". " + i.get_name() + " (" + i.get_species() + ", level " + str(i.get_level()) + ")")
                    count += 1
                print("")
        elif choice == '2':
            there = False
            name = input("\nEnter the name of the Pakuri to display: ")
            if len(Pakudex) == 0:
                print("Error: No such Pakuri!\n")
            else:
                for i in Pakudex:
                    if i.get_name() == name:
                        print("\nName: " + i.get_name())
                        print("Species: " + i.get_species())
                        print("Level: " + str(i.get_level()))
                        print("CP: " + str(i.get_cp()))
                        print("HP: " + str(i.get_hp()) + "\n")
                        there = True
                if not there:
                    print("Error: No such Pakuri!\n")

        elif choice == '3':
            print("\nPakuri Information\n-----------------")
            check = True
            name = input("Name: ")
            for i in Pakudex:
                if i.get_name() == name:
                    print("Error: Pakudex already contains this Pakuri!\n")
                    check = False
            if check is True:
                species = input("Species: ")
                while True:
                    level = input("Level: ")
                    try:
                        level = int(level)
                        if int(level) < 0:
                            print("Level cannot be negative.")
                        elif int(level) > 50:
                            print("Maximum level for Pakuri is 50")
                        elif 0 < int(level) <= 50:
                            pakuri = Pakuri(name, species, level)
                            Pakudex.append(pakuri)
                            print("\nPakuri " + name + " (" + species + ", level " + str(level) + ") added!\n")
                            break
                    except ValueError:
                        print("Invalid level!")

        elif choice == '4':
            name = input("\nEnter the name of the Pakuri to remove: ")
            there = False
            for i in Pakudex:
                if i.get_name() == name:
                    print("Pakuri " + i.get_name() + " removed.\n")
                    Pakudex.remove(i)
                    there = True
            if there is False:
                print("Error: No such Pakuri!\n")

        elif choice == '5':
            name = input("Enter the name of the Pakuri to change: ")
            there = False
            index = 0
            for i in Pakudex:
                if i.get_name() == name:
                    there = True
                    break
                index += 1
            if not there:
                print("Error: No such Pakuri!\n")
            else:
                while True:
                    level = input("Enter the new level for the Pakuri: ")
                    try:
                        level = int(level)
                        if int(level) < 0:
                            print("Level cannot be negative.")
                        elif int(level) > 50:
                            print("Maximum level for Pakuri is 50")
                        elif 0 < int(level) <= 50:
                            Pakudex[index].set_level(level)
                            print("")
                            break
                    except ValueError:
                        print("Invalid level!")

        elif choice == '6':
            print("\nThanks for using Pakudex: Let's Go! Bye!")
            return 0
        else:
            print("\nUnrecognized Menu Selection!\n")


if __name__ == '__main__':
    main()
