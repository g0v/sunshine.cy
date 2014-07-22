def upsert_journals(c, dataset):
    c.executemany('''
        UPDATE journals_journals
        SET date = %(date)s, download_url = %(download_url)s
        WHERE name = %(name)s
    ''', dataset)
    c.executemany('''
        INSERT INTO journals_journals(name, date, download_url)
        SELECT %(name)s, %(date)s, %(download_url)s
        WHERE NOT EXISTS (SELECT 1 FROM journals_journals WHERE name = %(name)s)
    ''', dataset)

def upsert_reports(c, dataset):
    c.execute('''
        SELECT id
        FROM reports_reports
        WHERE journal_id = %(journal_id)s AND category = %(category)s AND name = %(name)s AND report_at = %(report_at)s AND report_type = %(report_type)s
    ''', dataset)
    r = c.fetchone()
    if r:
        return r[0]
    c.execute('''
        INSERT INTO reports_reports(journal_id, category, name, department, title, report_at, report_type, spouse)
        SELECT %(journal_id)s, %(category)s, %(name)s, %(department)s, %(title)s, %(report_at)s, %(report_type)s, %(spouse)s
        WHERE NOT EXISTS (SELECT 1 FROM reports_reports WHERE journal_id = %(journal_id)s AND category = %(category)s AND name = %(name)s AND report_at = %(report_at)s AND report_type = %(report_type)s) RETURNING id
    ''', dataset)
    r = c.fetchone()
    if r:
        return r[0]

def upsert_property_investment(c, dataset):
    c.executemany('''
        UPDATE property_investment
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, owner = %(owner)s, company = %(company)s, address = %(address)s, register_date = %(register_date)s, register_reason = %(register_reason)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_investment(legislator_id, date, category, owner, company, address, register_date, register_reason, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(owner)s, %(company)s, %(address)s, %(register_date)s, %(register_reason)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_investment WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_debt(c, dataset):
    c.executemany('''
        UPDATE property_debt
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, species = %(species)s, debtor = %(debtor)s, owner = %(owner)s, register_date = %(register_date)s, register_reason = %(register_reason)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_debt(legislator_id, date, category, species, debtor, owner, register_date, register_reason, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(species)s, %(debtor)s, %(owner)s, %(register_date)s, %(register_reason)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_debt WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_claim(c, dataset):
    c.executemany('''
        UPDATE property_claim
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, species = %(species)s, debtor = %(debtor)s, owner = %(owner)s, register_date = %(register_date)s, register_reason = %(register_reason)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_claim(legislator_id, date, category, species, debtor, owner, register_date, register_reason, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(species)s, %(debtor)s, %(owner)s, %(register_date)s, %(register_reason)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_claim WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_insurance(c, dataset):
    c.executemany('''
        UPDATE property_insurance
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, company = %(company)s, name = %(name)s, owner = %(owner)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_insurance(legislator_id, date, category, company, name, owner, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(company)s, %(name)s, %(owner)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_insurance WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_antique(c, dataset):
    c.executemany('''
        UPDATE property_antique
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, owner = %(owner)s, quantity = %(quantity)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_antique(legislator_id, date, category, name, owner, quantity, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(owner)s, %(quantity)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_antique WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_otherbonds(c, dataset):
    c.executemany('''
        UPDATE property_otherbonds
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, owner = %(owner)s, quantity = %(quantity)s, face_value = %(face_value)s, currency = %(currency)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_otherbonds(legislator_id, date, category, name, owner, quantity, face_value, currency, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(owner)s, %(quantity)s, %(face_value)s, %(currency)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_otherbonds WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_fund(c, dataset):
    c.executemany('''
        UPDATE property_fund
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, owner = %(owner)s, dealer = %(dealer)s, quantity = %(quantity)s, face_value = %(face_value)s, currency = %(currency)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_fund(legislator_id, date, category, name, owner, dealer, quantity, face_value, currency, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(owner)s, %(dealer)s, %(quantity)s, %(face_value)s, %(currency)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_fund WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_bonds(c, dataset):
    c.executemany('''
        UPDATE property_bonds
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, symbol = %(symbol)s, owner = %(owner)s, dealer = %(dealer)s, quantity = %(quantity)s, face_value = %(face_value)s, currency = %(currency)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_bonds(legislator_id, date, category, name, symbol, owner, dealer, quantity, face_value, currency, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(symbol)s, %(owner)s, %(dealer)s, %(quantity)s, %(face_value)s, %(currency)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_bonds WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_stock(c, dataset):
    for data in dataset:
        for key in ['trust', 'trust_at', 'currency']:
            if data.get(key):
                data.update({key: ''})
    c.executemany('''
        UPDATE property_stock
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, owner = %(owner)s, quantity = %(quantity)s, face_value = %(face_value)s, currency = %(currency)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_stock(legislator_id, date, category, name, owner, quantity, face_value, currency, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(owner)s, %(quantity)s, %(face_value)s, %(currency)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_stock WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_land(c, dataset):
    for data in dataset:
        for key in ['trust', 'register_reason', 'acquire_value']:
            if data.get(key):
                data.update({key: ''})
    c.executemany('''
        UPDATE property_land
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, area = %(area)s, share_portion = %(share_portion)s, portion = %(portion)s, owner = %(owner)s, register_date = %(register_date)s, register_reason = %(register_reason)s, acquire_value = %(acquire_value)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_land(legislator_id, date, category, name, area, share_portion, portion, owner, register_date, register_reason, acquire_value, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(area)s, %(share_portion)s, %(portion)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_land WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_building(c, dataset):
    for data in dataset:
        for key in ['trust', 'register_reason', 'acquire_value']:
            if data.get(key):
                data.update({key: ''})
    c.executemany('''
        UPDATE property_building
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, area = %(area)s, share_portion = %(share_portion)s, portion = %(portion)s, owner = %(owner)s, register_date = %(register_date)s, register_reason = %(register_reason)s, acquire_value = %(acquire_value)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_building(legislator_id, date, category, name, area, share_portion, portion, owner, register_date, register_reason, acquire_value, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(area)s, %(share_portion)s, %(portion)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_building WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_boat(c, dataset):
    c.executemany('''
        UPDATE property_boat
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, tonnage = %(tonnage)s, homeport = %(homeport)s, owner = %(owner)s, register_date = %(register_date)s, register_reason = %(register_reason)s, acquire_value = %(acquire_value)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_boat(legislator_id, date, category, name, tonnage, homeport, owner, register_date, register_reason, acquire_value, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(tonnage)s, %(homeport)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_boat WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_car(c, dataset):
    c.executemany('''
        UPDATE property_car
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, capacity = %(capacity)s, owner = %(owner)s, register_date = %(register_date)s, register_reason = %(register_reason)s, acquire_value = %(acquire_value)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_car(legislator_id, date, category, name, capacity, owner, register_date, register_reason, acquire_value, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(capacity)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_car WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_aircraft(c, dataset):
    c.executemany('''
        UPDATE property_aircraft
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, name = %(name)s, maker = %(maker)s, number = %(number)s, owner = %(owner)s, register_date = %(register_date)s, register_reason = %(register_reason)s, acquire_value = %(acquire_value)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_aircraft(legislator_id, date, category, name, maker, number, owner, register_date, register_reason, acquire_value, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(name)s, %(maker)s, %(number)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_aircraft WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_cash(c, dataset):
    c.executemany('''
        UPDATE property_cash
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, currency = %(currency)s, owner = %(owner)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_cash(legislator_id, date, category, currency, owner, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(currency)s, %(owner)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_cash WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)

def upsert_property_deposit(c, dataset):
    c.executemany('''
        UPDATE property_deposit
        SET legislator_id = %(legislator_id)s, date = %(date)s, category = %(category)s, bank = %(bank)s, deposit_type = %(deposit_type)s, currency = %(currency)s, owner = %(owner)s, total = %(total)s
        WHERE index = %(index)s and source_file = %(source_file)s
    ''', dataset)
    c.executemany('''
        INSERT INTO property_deposit(legislator_id, date, category, bank, deposit_type, currency, owner, total, source_file, index)
        SELECT %(legislator_id)s, %(date)s, %(category)s, %(bank)s, %(deposit_type)s, %(currency)s, %(owner)s, %(total)s, %(source_file)s, %(index)s
        WHERE NOT EXISTS (SELECT 1 FROM property_deposit WHERE index = %(index)s and source_file = %(source_file)s)
    ''', dataset)
