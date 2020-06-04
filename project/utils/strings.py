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
FROM_DATE_LBL = "Od datuma"
TO_DATE_LBL = "Do datuma"
YEARS = "Godine"
MONTHS = "Meseci"
DAYS = "Dani"

# ===== BUTTONS =====
LOGIN_BTN = "Uloguj se"
ADD_BTN = "Dodaj"
UPDATE_BTN = "Promeni"
DELETE_BTN = "Obriši"
PRINT_BTN = "Štampaj"
EXPORT_BTN = "Sačuvaj"

# ===== HEADERS =====
PRESENT_EMPLOYEE_HDR = ["Ime", "Prezime", "Ime oca", "JMBG", "Lična karta", "Stručna sprema", "Radno mesto", "Slava",
                        "Adresa", "Tekući račun", "Staž pre M", "Staž u M", "Kućni telefon", "Mobilni telefon", "Prijava"]
PRESENT_POSITION_HDR = ["Naziv", "Radna subota"]
PRESENT_CHILD_HDR = ["Ime", "Prezime", "JMBG", "Datum rodjenja", "Majka", "Otac"]
PRESENT_UNIFORM_HDR = ["Naziv"]
PRESENT_UNIFORM_PIECE_HDR = ["Zaposleni", "Naziv", "Veličina", "Količina", "Dodatno", "Datum"]
PRESENT_FREE_DAYS_HDR = ["Zaposleni", "Početak", "Završetak", "Ukupno dana", "Razlog"]
PRESENT_WAGE_HDR = ["Zaposleni", "Dan", "Sat", "Obrok"]
PRESENT_SALARY_1_HDR = ["Datum", "Zaposleni", "Neto", "Bruto"]
PRESENT_SALARY_2_HDR = ["Datum", "Zaposleni", "Radnih dana", "Vrednost radnog dana", "Radnih sati",
                        "Vrednost radnog sata", "Obroka", "Vrednost obroka", "Rate", "Dana odmora",
                        "Vrednost dana odmora", "Fiksno"]

# ===== MESSAGES =====

# Login
LOGIN_MSG_TITLE = "Logovanje poruka"
SUCCESSFUL_LOGIN_MSG = "Ulogovani ste kao korisnik {username}"
MISSING_CREDENTIALS_MSG = "Oba polja moraju biti popunjena!"
WRONG_CREDENTIALS_MSG = "Pogrešno korisničko ime i/ili lozinka!"

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

UNIFORM_ADD_SUCC_MSG = "Novo odelo je uspešno dodato!"
UNIFORM_ADD_FAIL_MSG = "Novo odelo nije uspešno dodato! Probajte opet."
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
UNIFORM_PIECE_EMP_SUCC_MSG = "Pronadjena zadužena odeća za zadate parametre!"

FREE_DAYS_ADD_SUCC_MSG = "Slobodni dani su uspešno dodati!"
FREE_DAYS_ADD_FAIL_MSG = "Slobodni dani nisu uspešno dodati! Probajte opet."
FREE_DAYS_UPD_SUCC_MSG = "Uspešno su promenjeni slobodni dani!"
FREE_DAYS_UPD_FAIL_MSG = "Nisu uspešno promenjeni slobodni dani! Probajte ponovo."
FREE_DAYS_DEL_SUCC_MSG = "Uspešno su izbrisani slobodni dani!"
FREE_DAYS_DEL_FAIL_MSG = "Nisu uspešno izbrisani slobodni dani! Probajte ponovo."
FREE_DAYS_EMP_SUCC_MSG = "Pronadjeni slobodni dani zaposlenog!"
FREE_DAYS_EMP_FAIL_MSG = "Nisu pronadjeni slobodni dani zaposlenog!"

WAGE_ADD_SUCC_MSG = "Nova dnevnica je uspešno dodata!"
WAGE_ADD_FAIL_MSG = "Nova dnevnica nije uspešno dodata! Probajte opet."
WAGE_UPD_SUCC_MSG = "Uspešno je promenjena dnevnica!"
WAGE_UPD_FAIL_MSG = "Nije uspešno promenjena dnevnica! Probajte ponovo."
WAGE_DEL_SUCC_MSG = "Uspešno je izbrisana dnevnica!"
WAGE_DEL_FAIL_MSG = "Nije uspešno izbrisana dnevnica! Probajte ponovo."
WAGE_EMP_SUCC_MSG = "Pronadjene su dnevnice zaposlenog!"
WAGE_EMP_FAIL_MSG = "Nisu pronadjene dnevnice zaposlenog!"

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

# Data validation
REQUIRED_FIELDS_NOT_FILLED_MSG = "Sva obavezna polja (crvene boje) moraju biti popunjena!"
NOT_INTEGER_MSG = "Slovni karakteri uneti u polje gde se traže cifre!"
INVALID_DATES_MSG = "Početni datum mora biti pre krajnjeg datuma!"
INVALID_DATE_FORMAT_MSG = "Vrednosti za godine, mesece i dane moraju biti u odgovarajućim okvirima!"
INVALID_MEASURE_MSG = "Brojevne vrednosti moraju biti pozitivne!"
NOT_ALLOWED_FIX_AND_OTHER_MSG = "Plata mora biti uneta ili kao fiksna ili po danima!"
INVALID_NET_GROSS_RATIO_MSG = "Bruto ne sme biti manji od neto!"
CHILD_ONE_PARENT_REQUIRED_MSG = "Bar jedan roditelj mora biti izabran!"
WAGE_FOR_EMPLOYEE_MISSING_MSG = "Dnevnice za zaposlenog {employee} nisu unete!"

# Other
NOT_IMPLEMENTED_MSG = "Nije implementirano!"
INTERNAL_ERROR_MSG = "Interna greška! Pitaj Pavla."

# ===== REPORTS =====

EXPORT_CAPTION = "Sačuvaj kao PDF"
SAVE_FILE_FILTER = "PDF files (*.pdf);;All Files()"

# Employees
EMPLOYEE_LIST_TITLE = "Spisak zaposlenih"
POSITIONS_LIST_TITLE = "Spisak radnih pozicija"
CHILDREN_LIST_TITLE = "Spisak dece zaposlenih"
UNIFORMS_LIST_TITLE = "Spisak radne odeće"
UNIFORM_PIECES_LIST_TITLE = "Spisak zadužene radne odeće"
