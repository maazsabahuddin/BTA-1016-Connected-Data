# Local imports

# Python imports
import time
import json


LINE_BY_LINE = False


def map_view():
    print("===============\t\t\t=====================\t\t\t=================")
    print("=\t\t\t  = = = = = =\t  Hill Top\t\t= = = = = = =\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=\t(Fire Weapon)\t=\t\t\t=\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=====================\t\t\t=\t\t\t\t=")
    print("=\t\t\t  =\t\t\t\t\t\t\t\t\t\t\t=\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=====================\t\t\t=\t\t\t\t=")
    print("=\t\t\t  = = = = = =\t  Forest\t\t= = = = = = =\t\t\t\t=")
    print("=\tVillage\t  =\t\t\t=\t(Health Kit)\t=\t\t\t=\tValley\t\t=")
    print("=\t\t\t  =\t\t\t=====================\t\t\t=\t(Tiger)\t\t=")
    print("=\t\t\t  =\t\t\t\t\t\t\t\t\t\t\t=\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=====================\t\t\t=\t\t\t\t=")
    print("=\t\t\t  = = = = = =\t  River Side\t= = = = = = =\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=\t(Water & Map)\t=\t\t\t=\t\t\t\t=")
    print("===============\t\t\t=====================\t\t\t=================")


def story_opinion_message():
    print("="*73)
    print(f"{'='}\t\t\t\t\t\tTHIS IS A STORY BASED GAME\t\t\t\t\t\t{'='}")
    print("=" * 73)


def story_end_message():
    print("\n")
    print("="*65)
    print(f"{'='}\t\t\t\t\t\t\t GAME ENDS \t\t\t\t\t\t\t{'='}")
    print("=" * 65)


def start_of_story():
    import config
    if LINE_BY_LINE:
        for key in config.INITIAL_ROOM_MESSAGE:
            print(key, end='')
            time.sleep(0.035)
    else:
        print(config.INITIAL_ROOM_MESSAGE)


def instructions_of_story():
    import config
    if LINE_BY_LINE:
        for key in config.ROOMS_INSTRUCTION_MESSAGE:
            print(key, end='')
            time.sleep(0.035)
    else:
        print(config.ROOMS_INSTRUCTION_MESSAGE)


def pickup_options():
    import config
    if LINE_BY_LINE:
        for key in config.OPTIONS_INSTRUCTION_MESSAGE:
            print(key, end='')
            time.sleep(0.035)
    else:
        print(config.OPTIONS_INSTRUCTION_MESSAGE)


def location_choice():
    import config
    if LINE_BY_LINE:
        for key in config.PLAYING_INSTRUCTION_MESSAGE:
            print(key, end='')
            time.sleep(0.035)
    else:
        print(config.PLAYING_INSTRUCTION_MESSAGE)


def validate_user(username, password):
    """
    This function will validate the username and password.
    :param username:
    :param password:
    :return:
    """
    f = open("user/login-credentials.json", "r")
    users = json.load(f)
    for u in users:
        if username == u['username'] and password == u['password']:
            return True
    return False
