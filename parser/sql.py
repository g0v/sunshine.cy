# -*- coding: utf-8 -*-
import re


def get_portion(value):
    match = re.search(u'(?P<divider>\d+)\D+(?P<divide>\d+)', value)
    if match:
        return float(match.group('divide')) / float(match.group('divider'))
    if re.search(u'全部', value):
        return 1.0
    print value
    return 0.5

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
        return r[0], False
    c.execute('''
        INSERT INTO reports_reports(journal_id, category, name, department, title, report_at, report_type, spouse)
        SELECT %(journal_id)s, %(category)s, %(name)s, %(department)s, %(title)s, %(report_at)s, %(report_type)s, %(spouse)s
        WHERE NOT EXISTS (SELECT 1 FROM reports_reports WHERE journal_id = %(journal_id)s AND category = %(category)s AND name = %(name)s AND report_at = %(report_at)s AND report_type = %(report_type)s) RETURNING id
    ''', dataset)
    r = c.fetchone()
    if r:
        return r[0], True
    raise

def upsert_property_land(c, dataset):
    for data in dataset:
        for key in ['trust', 'register_reason', 'acquire_value']:
            data.update({key: data.get(key, '')})
        for key in ['area']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
        data['portion'] = get_portion(data['share_portion'])
        data['total'] = data['area'] * data['portion']
    c.executemany('''
        INSERT INTO property_land(report_id, name, area, share_portion, portion, owner, register_date, register_reason, acquire_value, total, trust)
        VALUES ( %(report_id)s, %(name)s, %(area)s, %(share_portion)s, %(portion)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s, %(total)s, %(trust)s)
    ''', dataset)

def upsert_property_building(c, dataset):
    for data in dataset:
        for key in ['trust', 'register_reason', 'acquire_value']:
            data.update({key: data.get(key, '')})
        for key in ['area']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
        data['portion'] = get_portion(data['share_portion'])
        data['total'] = data['area'] * data['portion']
    c.executemany('''
        INSERT INTO property_building(report_id, name, area, share_portion, portion, owner, register_date, register_reason, acquire_value, total, trust)
        VALUES ( %(report_id)s, %(name)s, %(area)s, %(share_portion)s, %(portion)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s, %(total)s, %(trust)s)
    ''', dataset)

def upsert_property_boat(c, dataset):
    for data in dataset:
        for key in ['tonnage']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_boat(report_id, name, tonnage, homeport, owner, register_date, register_reason, acquire_value)
        VALUES ( %(report_id)s, %(name)s, %(tonnage)s, %(homeport)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s)
    ''', dataset)

def upsert_property_car(c, dataset):
    for data in dataset:
        for key in ['capacity']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_car(report_id, name, capacity, owner, register_date, register_reason, acquire_value)
        VALUES ( %(report_id)s, %(name)s, %(capacity)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s)
    ''', dataset)

def upsert_property_aircraft(c, dataset):
    c.executemany('''
        INSERT INTO property_aircraft(report_id, name, maker, number, owner, register_date, register_reason, acquire_value)
        VALUES ( %(report_id)s, %(name)s, %(maker)s, %(number)s, %(owner)s, %(register_date)s, %(register_reason)s, %(acquire_value)s)
    ''', dataset)

def upsert_property_cash(c, dataset):
    for data in dataset:
        for key in ['total']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_cash(report_id, currency, owner, currency_total, total)
        VALUES ( %(report_id)s, %(currency)s, %(owner)s, %(currency_total)s, %(total)s)
    ''', dataset)

def upsert_property_deposit(c, dataset):
    for data in dataset:
        for key in ['total']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_deposit(report_id, bank, deposit_type, currency, owner, currency_total, total)
        VALUES ( %(report_id)s, %(bank)s, %(deposit_type)s, %(currency)s, %(owner)s, %(currency_total)s, %(total)s)
    ''', dataset)

def upsert_property_stock(c, dataset):
    for data in dataset:
        for key in ['trust', 'trust_at', 'currency']:
            data.update({key: data.get(key, '')})
        for key in ['quantity', 'face_value', 'total']:
            data[key] = re.sub('[^\d.]', '', data[key])
    c.executemany('''
        INSERT INTO property_stock(report_id, name, owner, quantity, face_value, currency, total, trust, trust_at)
        VALUES ( %(report_id)s, %(name)s, %(owner)s, %(quantity)s, %(face_value)s, %(currency)s, %(total)s, %(trust)s, %(trust_at)s)
    ''', dataset)

def upsert_property_bonds(c, dataset):
    for data in dataset:
        for key in ['total']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_bonds(report_id, name, symbol, owner, dealer, quantity, face_value, currency, total)
        VALUES ( %(report_id)s, %(name)s, %(symbol)s, %(owner)s, %(dealer)s, %(quantity)s, %(face_value)s, %(currency)s, %(total)s)
    ''', dataset)

def upsert_property_fund(c, dataset):
    for data in dataset:
        for key in ['total']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_fund(report_id, name, owner, dealer, quantity, face_value, currency, total)
        VALUES ( %(report_id)s, %(name)s, %(owner)s, %(dealer)s, %(quantity)s, %(face_value)s, %(currency)s, %(total)s)
    ''', dataset)

def upsert_property_otherbonds(c, dataset):
    for data in dataset:
        for key in ['total']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_otherbonds(report_id, name, owner, quantity, face_value, currency, total)
        VALUES ( %(report_id)s, %(name)s, %(owner)s, %(quantity)s, %(face_value)s, %(currency)s, %(total)s)
    ''', dataset)

def upsert_property_antique(c, dataset):
    c.executemany('''
        INSERT INTO property_antique(report_id, name, owner, quantity, total)
        VALUES ( %(report_id)s, %(name)s, %(owner)s, %(quantity)s, %(total)s)
    ''', dataset)

def upsert_property_insurance(c, dataset):
    c.executemany('''
        INSERT INTO property_insurance(report_id, company, name, owner)
        VALUES ( %(report_id)s, %(company)s, %(name)s, %(owner)s)
    ''', dataset)

def upsert_property_claim(c, dataset):
    for data in dataset:
        for key in ['total']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_claim(report_id, species, debtor, owner, register_date, register_reason, total)
        VALUES ( %(report_id)s, %(species)s, %(debtor)s, %(owner)s, %(register_date)s, %(register_reason)s, %(total)s)
    ''', dataset)

def upsert_property_debt(c, dataset):
    for data in dataset:
        for key in ['total']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_debt(report_id, species, debtor, owner, register_date, register_reason, total)
        VALUES ( %(report_id)s, %(species)s, %(debtor)s, %(owner)s, %(register_date)s, %(register_reason)s, %(total)s)
    ''', dataset)

def upsert_property_investment(c, dataset):
    for data in dataset:
        for key in ['total']:
            data[key] = float(re.sub('[^\d.]', '', data[key])) if data[key] else 0.0
    c.executemany('''
        INSERT INTO property_investment(report_id, owner, company, address, register_date, register_reason, total)
        VALUES ( %(report_id)s, %(owner)s, %(company)s, %(address)s, %(register_date)s, %(register_reason)s, %(total)s)
    ''', dataset)
