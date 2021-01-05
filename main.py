from ez_settings.ez_settings import EZSettings
from pathlib import Path


class Settings:
    NAME = "name"
    POSITION = "position"
    SUPERBOWL_WINS = "superbowl_wins"
    TEAMS = "teams"
    ACTIVE = "active"


if __name__ == "__main__":
    # make the settings
    settings = EZSettings(Path.home() / "deleteme" / "settings.json")

    # set some string values
    settings.set(Settings.POSITION, "Quarterback")
    settings.set(Settings.NAME, "Tom Brady")

    # set an int value
    settings.set(Settings.SUPERBOWL_WINS, 5)

    # set a list value
    settings.set(Settings.TEAMS, ["New England"])
    print(settings.get(Settings.TEAMS))

    # add to the list value
    settings.append(Settings.TEAMS, "Tampa Bay")
    print(settings.get(Settings.TEAMS))

    # remove from the list values
    settings.pop(Settings.TEAMS, "New England")
    print(settings.get(Settings.TEAMS))

    # set a bool value
    settings.set(Settings.ACTIVE, True)
    print(settings.get(Settings.ACTIVE))

    # check to see if there's a setting called TOUCHDOWNS
    exists = settings.exists("TOUCHDOWNS")
    print(exists)

    print(settings.get_setting_with_value(True))

    print(settings.exists("Tom Brady"))

    dict_value = {
                  "apple": 5,
                  "other_dict":
                      {
                          "playstation": 5,
                          "xbox": 360
                      }
                  }

    settings.set("dict", dict_value)
    print(settings.get_setting_with_value(5))

