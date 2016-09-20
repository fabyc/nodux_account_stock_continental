#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from decimal import Decimal
from functools import partial

from trytond.model import ModelView, fields
from trytond.wizard import Wizard, StateView, StateTransition, Button
from trytond.pyson import Eval, Get
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Category', 'Template']
__metaclass__ = PoolMeta

class Category:
    __name__ = 'product.category'

    @classmethod
    def __setup__(cls):
        super(Category, cls).__setup__()
        if cls.account_stock.domain:
            del cls.account_stock.domain[0]
            del cls.account_stock_supplier.domain[0]
            del cls.account_stock_customer.domain[0]
            del cls.account_stock_production.domain[0]
            del cls.account_stock_lost_found.domain[0]

class Template:
    __name__ = 'product.template'

    @classmethod
    def __setup__(cls):
        super(Template, cls).__setup__()
        if cls.account_stock.domain:
            del cls.account_stock.domain[0]
            del cls.account_stock_supplier.domain[0]
            del cls.account_stock_customer.domain[0]
            del cls.account_stock_production.domain[0]
            del cls.account_stock_lost_found.domain[0]
