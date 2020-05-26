# Strings for application


# Application level
WINDOWS_TITLE = "Zaposleni i plate"
EMPTY = "Prazno"
ALL = "Svi"
YES = "Da"
NO = "Ne"

# Main window
ADD_TAB_NAME = "Dodaj"
PRESENT_TAB_NAME = "Prikazi"
REPORTS_TAB_NAME = "Izveštaji"

EMPLOYEE = "Zaposleni"
POSITION = "Radno mesto"
CHILD = "Dete"
UNIFORM = "Radno odelo"
UNIFORM_PIECE = "Zaduženje radnog odela"
FREE_DAY = "Slobodni dani"
WAGE = "Dnevnice"
SALARY_1 = "Plata 1"
SALARY_2 = "Plata 2"

# ===== LABELS  =====
MAIN_LBL = "Logovanje"
USERNAME_LBL = "Korisničko ime:"
PASSWORD_LBL = "Lozinka:"
EMPLOYEE_LBL = "Zaposleni:"
FROM_DATE_LBL = "Od datuma:"
TO_DATE_LBL = "Do datuma:"

# ===== BUTTONS =====
LOGIN_BTN = "Uloguj se"
ADD_BTN = "Dodaj"
UPDATE_BTN = "Promeni"
DELETE_BTN = "Obriši"
PRINT_BTN = "Štampaj"

# ===== HEADERS =====
PRESENT_EMPLOYEE_HDR = ["Ime", "Prezime", "Ime oca", "JMBG", "Lična karta", "Stručna sprema", "Radno mesto", "Slava",
                        "Adresa", "Tekući račun", "Staž pre M", "Staž u M", "Kućni telefon", "Mobilni telefon", "Prijava"]
PRESENT_POSITION_HDR = ["Naziv", "Radna subota"]
PRESENT_CHILD_HDR = ["JMBG", "Godina rodjenja", "Majka", "Otac"]
PRESENT_UNIFORM_HDR = ["Naziv"]
PRESENT_UNIFORM_PIECE_HDR = ["Naziv", "Veličina", "Količina", "Dodatno", "Datum"]
PRESENT_FREE_DAYS_HDR = ["Početak", "Završetak", "Ukupno dana", "Razlog"]
PRESENT_WAGE_HDR = ["Dan", "Sat", "Obrok"]
PRESENT_SALARY_1_HDR = ["Neto", "Bruto", "Datum"]
PRESENT_SALARY_2_HDR = ["Datum", "Radnih dana", "Vrednost radnog dana", "Radnih sati", "Vrednost radnog sata", "Obroka",
                        "Vrednost obroka", "Rate", "Dana odmora", "Vrednost dana odmora", "Fiksno"]

# ===== MESSAGES =====

# Login
SUCCESSFUL_LOGIN_TITLE = "Uspešno logovanje"
SUCCESSFUL_LOGIN_MSG = "Ulogovani ste kao korisnik "
FAILED_LOGIN_TITLE = "Neuspešno logovanje"
FAILED_LOGIN_MSG = "Pogrešno korisničko ime i/ili lozinka!"

# Database
SECTION_NOT_FOUND_MSG = "Section {section} not found!"
DATABASE_ERROR_MSG = "DB error: {error}"

# Views

# Add tab views
ADD_VIEW_MSG = "Dodavanje poruka"

# Present tab views
PRESENT_VIEW_MSG = "Prikaz poruka"
MUST_SELECT_ONE_ROW_MSG = "Mora biti obeležen tačno jedan red!"
DELETE_DIALOG_MSG = "Da li si sigurna da želiš da izbrišeš ovaj red?"

# Messages about results from database interaction
EMPLOYEE_ADD_SUCC_MSG = "Novi zaposleni je uspešno dodat!"
EMPLOYEE_ADD_FAIL_MSG = "Novi zaposleni nije uspešno dodat! Probajte opet."
EMPLOYEE_UPD_SUCC_MSG = "Uspešno su promenjeni podaci o zaposlenom!"
EMPLOYEE_UPD_FAIL_MSG = "Nisu uspešno promenjeni podaci o zaposlenom! Probajte ponovo."
EMPLOYEE_DEL_SUCC_MSG = "Uspešno je izbrisan zaposleni!"
EMPLOYEE_DEL_FAIL_MSG = "Nije uspešno izbrisan zaposleni! Probajte ponovo."

POSITION_ADD_SUCC_MSG = "Nova pozicija je uspešno dodata!"
POSITION_ADD_FAIL_MSG = "Nova pozicija nije uspešno dodata! Probajte opet."
POSITION_UPD_SUCC_MSG = "Uspešno su promenjeni podaci o poziciji!"
POSITION_UPD_FAIL_MSG = "Nisu uspešno promenjeni podaci o poziciji! Probajte ponovo."
POSITION_DEL_SUCC_MSG = "Uspešno je izbrisana pozicija!"
POSITION_DEL_FAIL_MSG = "Nije uspešno izbrisana pozicija! Probajte ponovo."

CHILD_ADD_SUCC_MSG = "Novo dete je uspešno dodato!"
CHILD_ADD_FAIL_MSG = "Novo dete nije uspešno dodato! Probajte opet."
CHILD_UPD_SUCC_MSG = "Uspešno su promenjeni podaci o detetu!"
CHILD_UPD_FAIL_MSG = "Nisu uspešno promenjeni podaci o detetu! Probajte ponovo."
CHILD_DEL_SUCC_MSG = "Uspešno su izbrisani podaci o detetu!"
CHILD_DEL_FAIL_MSG = "Nisu uspešno izbrisani podaci o detetu! Probajte ponovo."

UNIFORM_UPD_SUCC_MSG = "Uspešno je promenjen odevni komad!"
UNIFORM_UPD_FAIL_MSG = "Nije uspešno promenjen odevni komad! Probajte ponovo."
UNIFORM_DEL_SUCC_MSG = "Uspešno je izbrisan odevni komad!"
UNIFORM_DEL_FAIL_MSG = "Nije uspešno izbrisan odevni komad! Probajte ponovo."

UNIFORM_PIECE_ADD_SUCC_MSG = "Novo zaduženje odeće je uspešno dodato!"
UNIFORM_PIECE_ADD_FAIL_MSG = "Novo zaduženje odeće nije uspešno dodato! Probajte opet."
UNIFORM_PIECE_UPD_SUCC_MSG = "Uspešno je promenjeno zaduženje odeće!"
UNIFORM_PIECE_UPD_FAIL_MSG = "Nije uspešno promenjeno zaduženje odeće! Probajte ponovo."
UNIFORM_PIECE_DEL_SUCC_MSG = "Uspešno je izbrisano zaduženje odeće!"
UNIFORM_PIECE_DEL_FAIL_MSG = "Nije uspešno izbrisano zaduženje odeće! Probajte ponovo."

FREE_DAYS_ADD_SUCC_MSG = "Slobodni dani su uspešno dodati!"
FREE_DAYS_ADD_FAIL_MSG = "Slobodni dani nisu uspešno dodati! Probajte opet."
FREE_DAYS_UPD_SUCC_MSG = "Uspešno su promenjeni slobodni dani!"
FREE_DAYS_UPD_FAIL_MSG = "Nisu uspešno promenjeni slobodni dani! Probajte ponovo."
FREE_DAYS_DEL_SUCC_MSG = "Uspešno su izbrisani slobodni dani!"
FREE_DAYS_DEL_FAIL_MSG = "Nisu uspešno izbrisani slobodni dani! Probajte ponovo."

WAGE_UPD_SUCC_MSG = "Uspešno je promenjena dnevnica!"
WAGE_UPD_FAIL_MSG = "Nije uspešno promenjena dnevnica! Probajte ponovo."
WAGE_DEL_SUCC_MSG = "Uspešno je izbrisana dnevnica!"
WAGE_DEL_FAIL_MSG = "Nije uspešno izbrisana dnevnica! Probajte ponovo."

SALARY_1_ADD_SUCC_MSG = "Nova plata 1 je uspešno dodata!"
SALARY_1_ADD_FAIL_MSG = "Nova plata 1 nije uspešno dodata! Probajte opet."
SALARY_1_UPD_SUCC_MSG = "Uspešno je promenjena plata 1!"
SALARY_1_UPD_FAIL_MSG = "Nije uspešno promenjena plata 1! Probajte ponovo."
SALARY_1_DEL_SUCC_MSG = "Uspešno je izbrisana plata 1!"
SALARY_1_DEL_FAIL_MSG = "Nije uspešno izbrisana plata 1! Probajte ponovo."

SALARY_2_ADD_SUCC_MSG = "Nova plata 2 je uspešno dodata!"
SALARY_2_ADD_FAIL_MSG = "Nova plata 2 nije uspešno dodata! Probajte opet."
SALARY_2_UPD_SUCC_MSG = "Uspešno je promenjena plata 2!"
SALARY_2_UPD_FAIL_MSG = "Nije uspešno promenjena plata 2! Probajte ponovo."
SALARY_2_DEL_SUCC_MSG = "Uspešno je izbrisana plata 2!"
SALARY_2_DEL_FAIL_MSG = "Nije uspešno izbrisana plata 2! Probajte ponovo."

# Messages about data validation
CHILD_ONE_PARENT_REQUIRED = "Bar jedan roditelj mora biti izabran!"

# Other
NOT_IMPLEMENTED_MSG = "Nije implementirano!"
