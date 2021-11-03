"""Utils for helping with credentials management.

This module contains functions for managing credentials for
further use in script.

This file can also be imported as a module and contains the following functions:
    * initial_configuration - manages initial configuration of .ini file
    * credentials_checker - check for credentials file existance
"""


import os
import configparser


def initial_configuration() -> dict:
    """Manage initial configuration of .ini file.

    This function handles getting CLIENT_ID and CLIENT_SECRET and
    writing this to .ini file for futher access and use.

    Returns:
        dict: Dictionary of CLIENT_ID and CLIENT_SECRET.
    """
    print("It looks like you are here for the first time. Let's set everything up!")
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
    credentials_data = {"CLIENT_ID": client_id, "CLIENT_SECRET": client_secret}
    config = configparser.ConfigParser()
    config["CREDENTIALS"] = credentials_data
    with open("spotichecker.ini", "w", encoding="utf-8") as configfile:
        config.write(configfile)
    print("Great. 'spotichecker.ini' was successfully created!\n")
    return credentials_data


def credentials_checker() -> dict:
    """Check for credentials file existance.

    If credentials file doesn't exist, run initial setup to
    create a new credentials file.

    Returns:
        dict: Dictionary with CLIENT_ID and CLIENT_SECRET
    """
    if os.path.isfile("spotichecker.ini"):
        config = configparser.ConfigParser()
        config.read("spotichecker.ini")
        return {
            "CLIENT_ID": config["CREDENTIALS"]["CLIENT_ID"],
            "CLIENT_SECRET": config["CREDENTIALS"]["CLIENT_SECRET"],
        }
    credentials_data = initial_configuration()
    return credentials_data
