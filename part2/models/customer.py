# -*- coding: utf-8 -*-
from odoo import fields, models
from datetime import datetime
import dateutil.parser


class Customer(models.Model):
    _name = 'supermarket.customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    city = fields.Char(string='City', required=True)
    street = fields.Char(string='Street', required=True)
    email = fields.Char(string='Email')
    premium = fields.Boolean(compute=compute_premium, string="Vip")
    carts = fields.Many2many('res.cart', string="Carts")

    def compute_premium(self, carts):
        if (carts >= 2):
            time = carts.date_of_creation
            insertion_date = dateutil.parser.parse(
                time.strftime("%Y-%m-%d %H:%M:%S"))
            time_between_insertion = datetime.now() - insertion_date
            if time_between_insertion.days > 7:
                return False
            else:
                return True
