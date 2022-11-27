from collections import defaultdict
from datetime import timedelta

from odoo import api, fields, models, _, Command
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_is_zero, float_compare


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.constrains('standard_price')
    def constrains_cost_cat(self):
        if self.categ_id.name != 'accs':
            if self.standard_price <= 0:
                raise ValidationError(_("Cost Can not be (0) When Product Category is not accs !"))
