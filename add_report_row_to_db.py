import sqlite3

def add_rep_row_to_db(date_of_report, code_of_report, name_of_reporter, date_of_start_bt, date_of_end_bt, sum_total, sum_word):
    con = sqlite3.connect('db.db', detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()
    #cur.execute('CREATE TABLE IF NOT EXISTS report (date_of_report DATE, code_of_report STRING, name_of_reporter STRING, date_of_start_bt DATE, date_of_end_bt DATE, sum_total DOUBLE, sum_word TEXT)')
    cur.execute(
        'CREATE TABLE  IF NOT EXISTS report (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, date_of_report DATE, code_of_report STRING, name_of_reporter STRING, date_of_start_bt DATE, date_of_end_bt DATE, sum_total DOUBLE, sum_word TEXT)')
    data_to_db = [date_of_report, code_of_report, name_of_reporter, date_of_start_bt, date_of_end_bt, sum_total, sum_word]
    cur.execute('INSERT INTO report VALUES (null, ?, ?, ?, ?, ?, ?, ?)', data_to_db)
    con.commit()
    cur.close()
    con.close()

def add_pay_row_to_db(days_in_bt, salary_per_day, salary_per_bt, name_of_payment, sum_of_payment, date_of_payment, sum_hotel, sum_from_credit):
    con = sqlite3.connect('db.db', detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS payments (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, days_in_bt INTEGER, salary_per_day DOUBLE, salary_per_bt DOUBLE, name_of_payment STRING, sum_of_payment DOUBLE, date_of_payment DATE, sum_hotel BOOLEAN, sum_from_credit BOOLEAN)')
    data_to_db = [days_in_bt, salary_per_day, salary_per_bt, name_of_payment, sum_of_payment, date_of_payment, sum_hotel, sum_from_credit]
    cur.execute('INSERT INTO payments VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?)', data_to_db)
    con.commit()
    cur.close()
    con.close()
