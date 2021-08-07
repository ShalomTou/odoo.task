# -*- coding: utf-8 -*-
from odoo import fields, models


class Product(models.Model):
    _name = 'supermarket.pruduct'
    _description = 'Product'

    name = fields.Char(string='Name',required=True)
    product_category = fields.Many2one("res.product_category", string="Product Category") 
    unit_price = fields.Float(string='Unit Price',required=True)
    

  