from ez_settings import EZSettings
from different_file import ClassThatNeedsSettings


from pathlib import Path

# set up the path to save the settings. Since this is of metaclass Singleton, we can now just always call
# EZSettings from anywhere in our program to get the object that's set up in this line.
EZSettings(Path.home() / "deleteme" / "settings.json")

class Settings:
    NAME = "name"
    POSITION = "position"
    SUPERBOWL_WINS = "superbowl_wins"
    TEAMS = "teams"
    ACTIVE = "active"

if __name__ == "__main__":
    # set some string values
    EZSettings().set(Settings.POSITION, "Quarterback")
    EZSettings().set(Settings.NAME, "Tom Brady")

    # set an int value
    EZSettings().set(Settings.SUPERBOWL_WINS, 5)

    # set a list value
    EZSettings().set(Settings.TEAMS, ["New England"])
    print(EZSettings().get(Settings.TEAMS))

    # add to the list value
    EZSettings().append(Settings.TEAMS, "Tampa Bay")
    print(EZSettings().get(Settings.TEAMS))

    # remove from the list values
    EZSettings().pop(Settings.TEAMS, "New England")
    print(EZSettings().get(Settings.TEAMS))

    # set a bool value
    EZSettings().set(Settings.ACTIVE, True)
    print(EZSettings().get(Settings.ACTIVE))

    # check to see if there's a setting called TOUCHDOWNS
    exists = EZSettings().exists("TOUCHDOWNS")
    print(exists)

    # get all the settings which have the value "True"
    print(EZSettings().get_setting_with_value(True))

    # check if there is a setting called "Sacks"
    print(EZSettings().exists("Sacks"))

    # set and get a dictionary value
    dict_value = {
                  "apple": 5,
                  "other_dict":
                      {
                          "playstation": 5,
                          "xbox": 360
                      }
                  }

    EZSettings().set("dict", dict_value)
    print(EZSettings().get_setting_with_value(5))

    # get an object that's defined in a different file
    another_class_in_another_file = ClassThatNeedsSettings()

    # since our EZSettings is define as a Singleton, we can use the same EZSettings().get() call in this other file
    # to still get any value we set in this file, without having to have passed a reference to an object to the other
    # class
    another_class_in_another_file.get_a_setting()
