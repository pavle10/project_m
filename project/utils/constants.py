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

EXPORT_DEFAULT_PATH = "D:\\"

# ===== SIZES =====
LOGIN_WIN_WIDTH = 600
LOGIN_WIN_HEIGHT = 500
PRINT_PREVIEW_DIALOG_WIDTH = 1000
PRINT_PREVIEW_DIALOG_HEIGHT = 400

MIN_TAB_WIDTH = 1900
MIN_TAB_HEIGHT = 980
LIST_AREA_WIDTH = 295
LIST_AREA_HEIGHT = 900
SCROLL_AREA_WIDTH = 300
SCROLL_AREA_HEIGHT = 900
TABLE_WIDTH = 1111
TABLE_HEIGHT = 451
DIALOGS_WIDTH = 300
DIALOGS_HEIGHT = 150
LABELS_WIDTH = 150
LABELS_HEIGHT = 35
SHORT_LABELS_WIDTH = 50
SHORT_LABELS_HEIGHT = 35
LINES_WIDTH = 300
LINES_HEIGHT = 35
BUTTONS_WIDTH = 150
BUTTONS_HEIGHT = 30

# ===== STYLE =====
TABS_FONT = QFont("Times", pointSize=13, weight=QFont.Normal)
LIST_FONT = QFont("Times", pointSize=13, weight=QFont.Normal)
LABELS_FONT = QFont("Times", pointSize=12, weight=QFont.Bold)
SHORT_LABELS_FONT = QFont("Times", pointSize=12, weight=QFont.Medium)
LINES_FONT = QFont("Times", pointSize=12, weight=QFont.Medium)
BUTTONS_FONT = QFont("Times", pointSize=12, weight=QFont.Medium)
STATUS_BAR_FONT = QFont("Times", pointSize=10, weight=QFont.Medium)

DATE_FORMAT_PYTHON = "%d.%m.%y."
DATE_FORMAT_PYQT = "dd.MM.yyyy."
LABEL_REQ_FLD_STYLE = "color: red"

# ===== MISC =====
DEFAULT_START_DATE = (datetime.datetime.now() - relativedelta(years=1)).date()
DEFAULT_END_DATE = datetime.datetime.now().date()

