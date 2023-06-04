import os
import glob

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ENVIRONMENTS_PATH = os.path.join(BASE_PATH, "environment")

if not os.path.isfile(os.path.join(ENVIRONMENTS_PATH, "__init__.py")):
    """
    We now know the _settings file is not yet linked, so create the symlink
    """
    settings_files = glob.glob1(ENVIRONMENTS_PATH, "[a-z]*.py")

    print("Available environment settings files:")
    for idx, file in enumerate(settings_files):
        print("{0}.".format(idx + 1), file)

    while True:
        try:
            selected_settings = settings_files[
                int(
                    input(
                        "Select one of the above settings files [1-{0}]: ".format(
                            len(settings_files)
                        )
                    )
                )
                - 1
            ]
            print("You picked: ", selected_settings)
            os.symlink(
                os.path.join(".", selected_settings),
                os.path.join(ENVIRONMENTS_PATH, "__init__.py"),
            )
        except IndexError:
            print(
                "Error, please select a settings file by entering a corresponding number!"
            )
            continue
        else:
            break

# Now that we know the _settings file exists we can import it
from .environment import *
