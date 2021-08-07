# -*- coding: utf-8 -*-
from odoo import fields, models


class CartItem(models.Model):
    _name = 'supermarket.cart_item'
    _description = 'Cart Item'

    product = fields.Many2one('res.product', string='Product')
    quantity = fields.Integer('Quantity', required=True)
    cart = fields.One2many('res.cart', 'customer', string="Cart")
