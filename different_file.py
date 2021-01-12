from ez_settings import EZSettings

class ClassThatNeedsSettings(object):
    def __init__(self):
        super().__init__()

    def get_a_setting(self):
        # there can only always ever be one instance of our EZSettings, so we can just get a value from it
        # without ever having to know where it came from or where in our program it was set
        print(EZSettings().get("name"))
