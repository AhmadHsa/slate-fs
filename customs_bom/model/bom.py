from odoo import models, api, fields
import base64
from copy import copy
from locale import currency

import xlrd

from odoo import _, api, fields, models
from odoo.exceptions import AccessError, UserError, ValidationError
from datetime import datetime


class OpportunityType(models.Model):
    _name = 'bom'

    product_template_id = fields.Many2one('product.template')
    name = fields.Char(string="name")
    partner_id = fields.Many2one('res.partner', string='Partner')
    quantity = fields.Integer(string='Quantity')
    cost = fields.Float(string='Cost')
    note = fields.Text(string='Note')
    sub_total = fields.Float(string="SubTotal", compute="_compute_sub_total")

    @api.depends('cost', 'quantity')
    def _compute_sub_total(self):
        for record in self:
            record.sub_total = record.cost * record.quantity
