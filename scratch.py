# ********************************************** PYTHON PRACTICE *******************************************************

"""
PLAN: build a fun simulation of Howl's Moving Castle

1. Game entails exploring the castle and talking to characters
2. You can move between rooms

"""
# ============== Helper Functions ==============

# @@@@@@@@@@@@@@@@@@@ Room Class @@@@@@@@@@@@@@@@@@@
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def setDescription(self, newDescript):
        self.description = newDescript

    def printDescription(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("ENTERED: " + self.name)
        print("\n" + self.description + "\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# @@@@@@@@@@@@@@@@@@@ Character Class @@@@@@@@@@@@@@@@@@@
class Character:
    def __init__(self, name, room):
        self.name = name
        self.location = room

    def speak(self, text):
        print("====================================================================")
        print(self.name)
        print("\n" + text + "\n")
        print("====================================================================")

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def setLocation(self, newLocation):
        self.location = newLocation

# @@@@@@@@@@@@@@@@@@@ Howl's Actual Castle Class @@@@@@@@@@@@@@@@@@@
class Castle:
    def __init__(self):
        self.name = "Howl's Moving Castle"
        self.characters = []
        self.rooms = []
        self.map = """
        -----------------------------------------------------------
        |                                                         |
        |                                                         |
        |                                                         |
        |                    FILL IN MAP                          |
        |                                                         |
        |                                                         |
        -----------------------------------------------------------
        """

    def createRooms(self):
        room1 = Room("Living Room", "A large room with wooden floors and a long, messy workbench. Books, magical ingredients, and critters are prolific.")
        room2 = Room("Kitchen", "There are pots and pans hanging from the wall, as well as food covering the table with little room to spare. There is a lovely hearth near the center.")
        room3 = Room("Bathroom", "The smell is rank -- the tub is covered in Howl's potions and the toilet probably hasn't been scrubbed... like, ever.")
        room4 = Room("Howl's Bedroom", "The grand bed is surrounded by magical trinkets, all of which twitch and glitter incessantly. A piece of paper has been hung up and stabbed.")
        self.rooms.append(room1)
        self.rooms.append(room2)
        self.rooms.append(room3)
        self.rooms.append(room4)


    def addCharacter(self, name):
        newCharacter = Character(name, "Living Room")
        self.characters.append(newCharacter)

    def printCharacters(self):
        print("The characters in the castle are:")
        for creature in self.characters:
            print(creature.getName() + ", who is currently in the " + creature.getLocation())

    def searchCharacter(self, name):
        for i in self.characters:
            if(i.getName() == name):
                return i

    def searchRoom(self, room):
        for i in self.rooms:
            if(i.getName() == room):
                return i

    def printMap(self):
        print(self.map)

    def setCharacterLocation(self, name, newLocation):
        self.searchCharacter(name).setLocation(newLocation)

    def characterSpeak(self, name, text):
        self.searchCharacter(name).speak(text)

    def introduction(self):
        print("Welcome to Howl's Moving Castle... the infamous, dynamic abode of Howl Pendragon.") # Make this fancier later -- Maybe make the player Sophie

    def enterRoom(self, character, newRoom):
        # Change the character's location
        self.setCharacterLocation(character, newRoom)
        # Read the room intro
        self.searchRoom(newRoom).printDescription()

# $$$$$$$$$$$$$$$$$$$$ Driver Section $$$$$$$$$$$$$$$$$$$$
def main():
    # Initialization
    howlsMovingCastle = Castle()
    howlsMovingCastle.createRooms()
    howlsMovingCastle.addCharacter("Markel")
    howlsMovingCastle.addCharacter("Calcifer")
    howlsMovingCastle.setCharacterLocation("Calcifer", "Kitchen")
    howlsMovingCastle.addCharacter("Sophie")

    # Game interactions
    howlsMovingCastle.introduction()
    howlsMovingCastle.enterRoom("Sophie","Living Room")
    howlsMovingCastle.characterSpeak("Calcifer", "May all your bacon burn")
    howlsMovingCastle.characterSpeak("Sophie", "It's gorgeous, Howl! It's like a dream...")
    print("\nSuccess")

if __name__ == "__main__":
    main()

# **********************************************************************************************************************
