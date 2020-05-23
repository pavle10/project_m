import os
import datetime
from dateutil.relativedelta import relativedelta

# Paths
ROOT_PATH = os.path.dirname(os.path.abspath(__file__ + "/../../"))
RESOURCES_PATH = os.path.join(ROOT_PATH, "resources")

ICONS_PATH = os.path.join(RESOURCES_PATH, "icons")
APP_ICON_PATH = os.path.join(ICONS_PATH, "app_icon.png")

DATABASE_CONFIG_PATH = os.path.join(RESOURCES_PATH, "database.ini")
DEFAULT_SECTION = "postgresql"

# Sizes
LOGIN_WIN_WIDTH = 600
LOGIN_WIN_HEIGHT = 500
MAIN_WIN_WIDTH = 1400
MAIN_WIN_HEIGHT = 1000
MIN_TAB_WIDTH = 700
MIN_TAB_HEIGHT = 850
DIALOG_WIDTH = 300
DIALOG_HEIGHT = 150

# Style
DATE_FORMAT_PYTHON = "%d.%m.%y."
DATE_FORMAT_PYQT = "dd.MM.yyyy."

# Misc
DEFAULT_START_DATE = (datetime.datetime.now() - relativedelta(years=1)).date()
DEFAULT_END_DATE = datetime.datetime.now().date()

