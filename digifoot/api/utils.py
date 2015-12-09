# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from babel import dates
from django.utils.translation import to_locale, get_language
from babel.numbers import format_currency

def currency(number, currency = 'EUR'):
    locale = to_locale(get_language())
    if not number:
        return ""

    return format_currency(number, currency, locale = locale)

def format_date(date):
    locale = to_locale(get_language())
    return dates.format_date(date, format='medium', locale = locale)
