from ez_settings.ez_settings import EZSettings
from pathlib import Path

# Get a reference to our settings object
settings_obj = EZSettings(Path.home() / "deleteme" / "settings.json")

class Settings:
    NAME = "name"
    POSITION = "position"
    SUPERBOWL_WINS = "superbowl_wins"
    TEAMS = "teams"
    ACTIVE = "active"

if __name__ == "__main__":
    # set some string values
    settings_obj.set(Settings.POSITION, "Quarterback")
    settings_obj.set(Settings.NAME, "Tom Brady")

    # set an int value
    settings_obj.set(Settings.SUPERBOWL_WINS, 5)

    # set a list value
    settings_obj.set(Settings.TEAMS, ["New England"])
    print(settings_obj.get(Settings.TEAMS))

    # add to the list value
    settings_obj.append(Settings.TEAMS, "Tampa Bay")
    print(settings_obj.get(Settings.TEAMS))

    # remove from the list values
    settings_obj.pop(Settings.TEAMS, "New England")
    print(settings_obj.get(Settings.TEAMS))

    # set a bool value
    settings_obj.set(Settings.ACTIVE, True)
    print(settings_obj.get(Settings.ACTIVE))

    # check to see if there's a setting called TOUCHDOWNS
    exists = settings_obj.exists("TOUCHDOWNS")
    print(exists)

    print(settings_obj.get_setting_with_value(True))

    print(settings_obj.exists("Tom Brady"))

    dict_value = {
                  "apple": 5,
                  "other_dict":
                      {
                          "playstation": 5,
                          "xbox": 360
                      }
                  }

    settings_obj.set("dict", dict_value)
    print(settings_obj.get_setting_with_value(5))
