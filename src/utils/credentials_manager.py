"""Utils for helping with credentials management.

This module contains functions for managing credentials for
further use in script.

This file can also be imported as a module and contains the following functions:
    * initial_configuration() - manages initial configuration of .ini file
"""


import configparser


def initial_configuration() -> dict:
    """Manage initial configuration of .ini file.

    This function handles getting CLIENT_ID and CLIENT_SECRET and
    writing this to .ini file for futher access and use.

    Returns:
        dict: Dictionary of CLIENT_ID and CLIENT_SECRET.
    """
    print("It looks like you are here for the first time, "
          "let's set everything up!")
    print("Enter your CLIENT_ID:")
    while True:
        client_id = input("> ")
        if client_id == "":
            print("You entered nothing. Try again.")
            continue
        break
    print("Great. Now, let's enter your CLIENT_SECRET:")
    while True:
        client_secret = input("> ")
        if client_secret == "":
            print("You entered nothing. Try again.")
            continue
        break
    credentials_data = {
        "CLIENT_ID": client_id,
        "CLIENT_SECRET": client_secret
    }
    config = configparser.ConfigParser()
    config["CREDENTIALS"] = credentials_data
    with open("spotichecker.ini", "w") as configfile:
        config.write(configfile)
    print("Great. 'spotichecker.ini' was successfully created!\n")
    return credentials_data
