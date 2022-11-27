from collections import defaultdict
from datetime import timedelta

from odoo import api, fields, models, _, Command
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_is_zero, float_compare


class CrmLead(models.Model):
    _inherit = 'product.category'
    is_accs_category = fields.Boolean(string="Is Accs Category")
