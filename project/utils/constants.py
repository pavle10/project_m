import os
import datetime
from dateutil.relativedelta import relativedelta
from PyQt5.QtGui import QFont

# ===== PATHS =====
ROOT_PATH = os.path.dirname(os.path.abspath(__file__ + "/../../"))
RESOURCES_PATH = os.path.join(ROOT_PATH, "resources")

ICONS_PATH = os.path.join(RESOURCES_PATH, "icons")
APP_ICON_PATH = os.path.join(ICONS_PATH, "app_icon_32.png")

DATABASE_CONFIG_PATH = os.path.join(RESOURCES_PATH, "database.ini")
DEFAULT_SECTION = "postgresql"

# ===== SIZES =====
LOGIN_WIN_WIDTH = 600
LOGIN_WIN_HEIGHT = 500
MAIN_WIN_WIDTH = 1400
MAIN_WIN_HEIGHT = 600
MIN_TAB_WIDTH = 1390
MIN_TAB_HEIGHT = 570
LIST_AREA_WIDTH = 200
LIST_AREA_HEIGHT = 500
SCROLL_AREA_WIDTH = 220
SCROLL_AREA_HEIGHT = 500
DIALOGS_WIDTH = 300
DIALOGS_HEIGHT = 150
LABELS_WIDTH = 150
LABELS_HEIGHT = 25
LINES_WIDTH = 250
LINES_HEIGHT = 25
BUTTONS_WIDTH = 250
BUTTONS_HEIGHT = 28

# ===== STYLE =====
TABS_FONT = QFont("Times", pointSize=11, weight=QFont.Normal)
LIST_FONT = QFont("Times", pointSize=11, weight=QFont.Normal)
LABELS_FONT = QFont("Times", pointSize=10, weight=QFont.Bold)
LINES_FONT = QFont("Times", pointSize=10, weight=QFont.Medium)
BUTTONS_FONT = QFont("Times", pointSize=10, weight=QFont.Medium)

DATE_FORMAT_PYTHON = "%d.%m.%y."
DATE_FORMAT_PYQT = "dd.MM.yyyy."
LABEL_REQ_FLD_STYLE = "color: red"

# ===== MISC =====
DEFAULT_START_DATE = (datetime.datetime.now() - relativedelta(years=1)).date()
DEFAULT_END_DATE = datetime.datetime.now().date()

