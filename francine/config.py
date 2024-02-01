import os

import platformdirs


def get_db_path():
    appname = "francine"
    appauthor = "gfabrizio"
    data_dir = platformdirs.user_data_dir(appname, appauthor)
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, "francine.json")


db_path = get_db_path()
