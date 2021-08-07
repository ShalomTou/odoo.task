# -*- coding: utf-8 -*-
from odoo import fields, models
from datetime import datetime


class Cart(models.Model):
    _name = 'supermarket.cart'
    _description = 'Cart'

    customer = fields.Many2one("res.customer", string="Customer")
    date_of_creation = fields.Date(
        string='Date of Creation', default=datetime.today())
    total_amount = fields.Float(
        compute=compute_total, store=True, string="Total Amount")

    def compute_total(self):
        return fields.One2many('res.cart_item', 'product') * fields.One2many('res.cart_item', 'quantity')

