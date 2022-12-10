"""
This is a story based game of a tiger with a player who has multiple choices to pick items and play.
Python Assignment 13 - Professor Aditya
BTA-1016 ConnectedData
"""
# Python imports
import json
import random
import time
import os
from datetime import datetime

# Local imports
import view
import api


_WRITE_TO_FILE = {}

# Player's GAIN HEALTH Parameters
RECHARGE_HEALTH = 50
RECHARGE_COFFEE = 5
_WRITE_TO_FILE.update({
    'RECHARGE_HEALTH': RECHARGE_HEALTH,
    'RECHARGE_COFFEE': RECHARGE_COFFEE
})

# Tiger DAMAGES Parameters
FIRE_WEAPON_DAMAGE = 80
MAP_OF_VALLEY_DAMAGE = 30
KNIFE_DAMAGE = 5
_WRITE_TO_FILE.update({
    'FIRE_WEAPON_DAMAGE': FIRE_WEAPON_DAMAGE,
    'MAP_OF_VALLEY_DAMAGE': MAP_OF_VALLEY_DAMAGE,
    'KNIFE_DAMAGE': KNIFE_DAMAGE
})

# THESE ARE THE SHORT CONSTANTS THAT WE USED SO FAR.
HILLTOP = "ht"
FOREST = "fo"
RIVER_SIDE = "rs"
VALLEY = "va"

PLAYER_HEALTH = 100
PLAYER_TOOLS = ["Knife", "Coffee"]
TIGER_HEALTH = 100
_WRITE_TO_FILE.update({
    'INITIAL_PLAYER_HEALTH': PLAYER_HEALTH,
    'INITIAL_TIGER_HEALTH': TIGER_HEALTH
})


def greeting_message(subject, _object) -> None:
    """
    This function will greet the player.
    :param subject:
    :param _object:
    :return:
    """
    if subject == "Valley area":
        msg = f"\nCongratulations! You have reached {subject}, ready to fight with tiger"
    else:
        PLAYER_TOOLS.append(_object)
        msg = f"\nCongratulations! You have reached {subject}. {_object} is available here."

    print(msg)
    _WRITE_TO_FILE.update({
        subject: msg,
    })


def items_message():
    """
    This function is used to display player tools that what he got behind him to fight with tiger.
    :return:
    """
    for item in PLAYER_TOOLS:
        print(f"You got {item}")


def fight_message():
    """
    This function will only display the fight message
    :return:
    """
    print("\n\t\t\tFight will begin in 5 seconds\t\t\t")
    time.sleep(1)
    print("\t\t\tFight will begin in 4 seconds\t\t\t")
    time.sleep(1)
    print("\t\t\tFight will begin in 3 seconds\t\t\t")
    time.sleep(1)
    print("\t\t\tFight will begin in 2 seconds\t\t\t")
    time.sleep(1)
    print("\t\t\tFight will begin in 1 second\t\t\t")
    time.sleep(1)
    print("\nFight begin. Player will attack first.")
    print("\nPlayer can choose from following options:\n\n"
          "Press HK to use Health Kit. (Can use only one time)\n"
          "Press FW to use Fire Weapon. (Can use only one time)\n"
          "Press KN to use Knife (Can use multiple times)\n"
          "Press DC to Drink Coffee (Can use multiple times)")


def fight_health_decision(user_choice):
    """
    This function will be used to deduct health of player and tiger
    :param user_choice:
    :return:
    """

    global PLAYER_HEALTH, TIGER_HEALTH
    if user_choice == "HK":
        if "Health kit" not in PLAYER_TOOLS:
            print("You're out of Health Kit.")
            return
        PLAYER_TOOLS.remove("Health kit")
        if PLAYER_HEALTH > 50:
            PLAYER_HEALTH = 100
        else:
            PLAYER_HEALTH += RECHARGE_HEALTH
    elif user_choice == "FW":
        if "Fire weapon" not in PLAYER_TOOLS:
            print("You're out of Fire Weapon.")
            return
        PLAYER_TOOLS.remove("Fire weapon")
        TIGER_HEALTH -= FIRE_WEAPON_DAMAGE
    elif user_choice == "KN":
        TIGER_HEALTH -= KNIFE_DAMAGE
    elif user_choice == "DC":
        # Whenever the user drinks the coffee we will call the Coffee API.
        api.get_coffee()
        print(f"Player just drank Coffee and boosted by {RECHARGE_COFFEE} points")
        PLAYER_HEALTH += RECHARGE_COFFEE


def update_player_health():
    """
    If the user doesn't select map of valley, then his points will be deducted by 30
    :return:
    """
    global PLAYER_HEALTH
    if "Water and map of valley" not in PLAYER_TOOLS:
        print(f"\nDeducting {MAP_OF_VALLEY_DAMAGE} points because player didn't carry Map of Valley with himself.")
        PLAYER_HEALTH -= MAP_OF_VALLEY_DAMAGE


def fight_measures():
    """
    Things to do and measure before the start of fight
    :return:
    """
    fight_message()
    update_player_health()


def fight_with_tiger():
    """
    This function is responsible to take input from player and reduce health vice versa.
    :return:
    """
    global PLAYER_HEALTH
    player_hit = str(input("\nEnter your choice: ")).upper()
    while player_hit not in ["HK", "FW", "KN", "DC"]:
        print("\nInvalid Choice. Please try again!")
        player_hit = str(input("\nEnter your choice: ")).upper()

    fight_health_decision(user_choice=player_hit)

    # Now its tiger turn to hit back
    if TIGER_HEALTH > 0:
        tiger_damage = random.choice([15, 20, 25])
        PLAYER_HEALTH -= tiger_damage


def check_holiday(date):
    """
    This function will return a boolean value that if it is a holiday or not.
    :param date:
    :return:
    """
    holidays = api.get_holidays(country="CA", year="2022")
    for holiday in holidays:
        if holiday['date'] != date:
            continue
        return True, holiday
    return False, None


def display_weather():
    """
    This function will display the timings according to the region.
    :return:
    """
    weather = api.weather_city()
    print(f"\nToday, the temperature is {round(weather['C'], 2)}°C / {round(weather['F'], 2)}°F / "
          f"{round(weather['K'], 2)}K as per the weather API.")


def display_sunrise_sunset_timings():
    """
    This function will display the timings according to the region.
    :return: 
    """
    _time = api.sunset_and_sunrise_time()
    print(f"\nThe sunrise timing is: {_time['sunrise']}")
    print(f"The sunset timing is: {_time['sunset']}")


def display_met_museum_departments():
    """
    This function will display the departments
    :return:
    """
    _WRITE_TO_FILE.update({
        'MET_MUSEUM_DEPARTMENTS_CHECKED': True,
    })
    departments, count = api.metmuseum_api()
    for d in departments:
        print(f"\nDepartment Id: {d['departmentId']}")
        print(f"Department Name: {d['displayName']}")
        time.sleep(0.035)


if __name__ == "__main__":

    username = str(input("\nEnter username: ")).lower()
    password = str(input("Enter password: ")).lower()

    if view.validate_user(username=username, password=password):
        print("Login Successful!")
        _WRITE_TO_FILE.update({
            'LOGIN_STATUS': "SUCCESSFUL",
            'LOGIN_USER': username,
            'LOGIN_DATETIME': str(datetime.today()),
            'MET_MUSEUM_DEPARTMENTS_CHECKED': False,
        })
    else:
        print("Invalid Credentials. GAME QUIT")
        os.abort()

    currentDateAndTime = datetime.now()
    print("\nDo you want to play the game? Press any key to continue and 'q' to quit ")
    user_consent = str(input("Enter your choice: ")).upper()

    while user_consent not in ['QUIT', 'Q']:

        view.story_opinion_message()
        time.sleep(2)

        print("\nLets check for a holiday..")
        _, data = check_holiday(date=str(currentDateAndTime.date()))
        if _:
            print(f"\nOhh!! Today is {data['name']}.")
            print("\nDo you want to hunt on a holiday? Press any key to continue and q to Quit")
            holiday_consent = str(input("Enter your choice: ")).upper()
            if holiday_consent in ["Q", "QUIT"]:
                print("\nGame QUIT because of holiday!\n")
                os.abort()
        else:
            print("\nNo Holiday Today!")

        print("\nYou're in a village.")
        print("\n1- Check the weather of the village.")
        print("2- Check the sunrise / sunset timings of the village.")
        print("3- Check the MetMuseum Departments.")
        print("4- Continue to play game.")

        user_preference = input("Enter your choice: ")
        while not user_preference.isdigit():
            print("\nInvalid choice. Try again.")
            user_preference = input("\nEnter your choice: ")

        user_preference = int(user_preference)
        while user_preference in [1, 2, 3]:
            if user_preference == 1:
                display_weather()
            elif user_preference == 2:
                display_sunrise_sunset_timings()
            elif user_preference == 3:
                display_met_museum_departments()
            print("\n1- Check the weather of the village.")
            print("2- Check the sunrise / sunset timings of the village.")
            print("3- Check the MetMuseum Departments.")
            print("4- Continue to play game.")
            user_preference = int(input("Enter your choice: "))

        time.sleep(2)
        print("\n\nHurray!! Lets continue the game..\n")
        view.start_of_story()
        time.sleep(3)
        view.instructions_of_story()
        time.sleep(4)
        view.pickup_options()
        time.sleep(5)
        view.location_choice()

        for i in range(2):
            items_message()
            userInput = str(input("\nEnter your choice: ")).lower()
            while userInput not in [HILLTOP, FOREST, RIVER_SIDE, VALLEY]:
                print("\nInvalid Choice. Please try again!")
                userInput = str(input("\nEnter your choice: ")).lower()

            if userInput == HILLTOP:
                greeting_message(subject="Hill Top", _object="Fire weapon")
            elif userInput == FOREST:
                greeting_message(subject="Forest", _object="Health kit")
            elif userInput == RIVER_SIDE:
                greeting_message(subject="River side", _object="Water and map of valley")
                view.map_view()
            elif userInput == VALLEY:
                greeting_message(subject="Valley area", _object="")
                break

        items_message()
        fight_measures()
        while PLAYER_HEALTH > 0 and TIGER_HEALTH > 0:
            print(f"\nPlayer health: {PLAYER_HEALTH}")
            print(f"Tiger health: {TIGER_HEALTH}")
            fight_with_tiger()

        print("\nResults: ")
        print(f"Player health: {PLAYER_HEALTH if PLAYER_HEALTH > 0 else 0}")
        print(f"Tiger health: {TIGER_HEALTH if TIGER_HEALTH > 0 else 0}")

        if PLAYER_HEALTH > TIGER_HEALTH or (PLAYER_HEALTH == 0 and PLAYER_HEALTH == TIGER_HEALTH):
            if 6 < currentDateAndTime.hour < 18:
                print("\nHurray!! Player wins (Get 1000 coins in wallet).")
                coins = 1000
            else:
                print("\nHurray!! Player wins (Get 1500 coins in wallet).")
                coins = 1500

            print("\nDo you want to convert your coins into CAD? Press any key to continue  and 'q' to quit ")
            respond = str(input("Enter your choice: ")).upper()
            if respond not in ["Q", "QUIT"]:
                print(f"\nThe approximate value {coins} coins is around ${api.currency_convert(coins=coins)[0]}.")
        else:
            print("\nPlayer loose.")

        _WRITE_TO_FILE.update({
            'FINAL_PLAYER_HEALTH': PLAYER_HEALTH,
            'FINAL_TIGER_HEALTH': TIGER_HEALTH
        })
        json_string = json.dumps(_WRITE_TO_FILE)
        with open('user/user-activity.json', 'w') as outfile:
            outfile.write(json_string)

        view.story_end_message()
        time.sleep(2)

        print("\nDo you want to play the game again? Press any key to continue and 'q' to quit")
        PLAYER_HEALTH = 100
        TIGER_HEALTH = 100
        user_consent = str(input("Enter your choice: ")).upper()

    print("\nGame QUIT. Please come back again and earn points!\n")
    os.abort()
