# Python imports
import json


# INITIAL_ROOM_MESSAGE = "\nThe player is a hunter who hunts animals for the safety of people. This time, he was in a \n" \
#                   "mountain village where a wild tiger caused trouble for the local community. The tiger is \n" \
#                  "threatening the lives of villagers and has already attacked some livestock. Now, villager Head \n" \
#                  "wants the player to kill the tiger for them, and in return, villagers will reward the player. \n" \
#                  "The hunter (player) will receive 1000 coins if he kills the tiger between 6 AM to 6 PM. On the \n" \
#                   "other hand, he will receive 1500 coins if he kills the tiger at night which is from 6 PM till " \
#                   "the morning."


# ROOMS_INSTRUCTION_MESSAGE = "\n\nThe player can choose different items for the mission and these items will help the " \
#                       "player to kill the tiger.\n" \
#                       "Following are the items: \n\n" \
#                       "Health kit- It will recharge player health by 50 points / 50%\n\n" \
#                       "Fire Weapon- Damages tiger health by 80 points / 80%\n\n" \
#                       "Map of valley- This will help player to reach destination without any health decrease.\n\n" \
#                       "Without a “map of the valley”, it will take longer time to find tiger and health will be " \
#                       "reduce by 30 points/ 30%).\n\n" \
#                       "Knife- Damages tiger health by 5 points / 5%.\n\n" \
#                       "Coffee- Increases health by 5 points / 5%\n"


# OPTIONS_INSTRUCTION_MESSAGE = "\nHowever, the player can pick up only 2 items. As his backpack can hold a maximum " \
#                               "of 4 items and he has already a bottle of coffee and a knife with him. \n\n"


# PLAYING_INSTRUCTION_MESSAGE = "Villager’s Head has also given locations to find different items:\n\n" \
#                    "(Press [HT] to enter) Fire weapon is in Hill Top.\n\n" \
#                    "(Press [FO] to enter) The Health kit is in the Forest.\n\n" \
#                    "(Press [RS] to enter) Coffee and the map of the valley are on the RiverSide.\n\n" \
#                    "(Press [VA] to enter Valley) To fight the tiger, the player should reach the valley area:\n"

jsonRoomObject = open("./rooms.json")
roomDb = json.load(jsonRoomObject)

INITIAL_ROOM_MESSAGE = roomDb["INITIAL_ROOM_MESSAGE"]

ROOMS_INSTRUCTION_MESSAGE = roomDb["ROOMS_INSTRUCTION_MESSAGE"]

OPTIONS_INSTRUCTION_MESSAGE = roomDb["OPTIONS_INSTRUCTION_MESSAGE"]

PLAYING_INSTRUCTION_MESSAGE = roomDb["PLAYING_INSTRUCTION_MESSAGE"]
