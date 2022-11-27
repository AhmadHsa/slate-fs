from odoo import models, api, fields


class OpportunityType(models.Model):
    _name = 'opportunity.type'
    _inherit = ['mail.thread']

    name = fields.Char(string="name")
