# 🌴 EZ Settings

EZ Settings is a very simple, lightweight settings module that makes it easy to get and set settings for your application. It's all stored in a JSON file, so any value you want to store has to be able to be serialized in a JSON file.

It works in "base" mode, where you make an object of the `EZSettingsBase` class and use that throughout your program. Or you can use it as a singleton by defining `EZSettings` once in the beginen of you program, and then calling it anywhere else. 




## EZSettingsBase
Let's look at the `Base` way first:

### Initializing

You can provide a path where you want the settings file to be
```python
from ez_settings import EZSettings

settings = EZSettings("/home/applications/my_app/settings.json")
```

### Setting values

I like to make simple classes to store setting names, just because it makes it easier to autocomplete when writing code. You can also just pass in a normal string in the `set` and `get` functions.

```python
from ez_settings.ez_settings_base import EZSettingsBase


class Settings:
    NAME = "name"
    POSITION = "position"
    SUPERBOWL_WINS = "superbowl_wins"
    TEAMS = "teams"
    ACTIVE = "active"


settings = EZSettingsBase("/home/applications/my_app/settings.json")

settings.set(Settings.NAME, "Tom Brady")
settings.set(Settings.SUPERBOWL_WINS, 5)

```

### Getting values

```python
from ez_settings.ez_settings_base import EZSettingsBase


class Settings:
    NAME = "name"
    POSITION = "position"
    SUPERBOWL_WINS = "superbowl_wins"
    TEAMS = "teams"
    ACTIVE = "active"


settings = EZSettingsBase("/home/applications/my_app/settings.json")

championships = settings.get(Settings.SUPERBOWL_WINS)

```

### List values

You can append or pop items if the value of your setting is a list

```python
from ez_settings.ez_settings_base import EZSettingsBase


class Settings:
    NAME = "name"
    POSITION = "position"
    SUPERBOWL_WINS = "superbowl_wins"
    TEAMS = "teams"
    ACTIVE = "active"


settings = EZSettingsBase("/home/applications/my_app/settings.json")

# set a list value
settings.set(Settings.TEAMS, ["New England"])

# add to the list value
settings.append(Settings.TEAMS, "Tampa Bay")

# remove from the list values
settings.pop(Settings.TEAMS, "New England")

```

### Deleting a single setting

```python
from ez_settings.ez_settings_base import EZSettingsBase


class Settings:
    NAME = "name"
    POSITION = "position"
    SUPERBOWL_WINS = "superbowl_wins"
    TEAMS = "teams"
    ACTIVE = "active"


settings = EZSettingsBase("/home/applications/my_app/settings.json")
settings.remove(Settings.POSITION)
```

### Wiping all settings

```python
from ez_settings.ez_settings_base import EZSettingsBase

settings = EZSettingsBase("/home/applications/my_app/settings.json")
settings.reset()
```
### Checking if a setting exists

```python
from ez_settings.ez_settings_base import EZSettingsBase

settings = EZSettingsBase("/home/applications/my_app/settings.json")
settings.exists("Injuries")
```


## Singleton

Now let's do the exact same thing, just using the Singleton method

```python
from ez_settings.ez_settings_base import EZSettings
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

```

Let's add another file to our program, with a class and a function that gets the `name` setting from our settings

_> different_file.py_

```python
from ez_settings.ez_settings_base import EZSettings


class ClassThatNeedsSettings(object):
    def __init__(self):
        super().__init__()

    def get_a_setting(self):
        # there can only always ever be one instance of our EZSettings, so we can just get a value from it
        # without ever having to know where it came from or where in our program it was set
        print(EZSettings().get("name"))


```

In our main program, we can make an object of `ClassThatNeedsSettings`, call the `get_a_setting` method and it will print out the value of `name`

```python
    # get an object that's defined in a different file
    another_class_in_another_file = ClassThatNeedsSettings()

    # since our EZSettings is defined as a Singleton, we can use the same EZSettings().get() call in this other file
    # to still get any value we set in this file, without having to have passed a reference to an object to the other
    # class
    another_class_in_another_file.get_a_setting()

```
