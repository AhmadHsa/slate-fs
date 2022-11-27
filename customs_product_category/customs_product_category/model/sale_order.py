from odoo import api, fields, models, _, Command
from odoo.exceptions import AccessError, UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains('price_unit')
    def constraint_unit_price(self):
        if self.price_unit <= 0:
            raise UserError(_('Sale Price must be grater than 0'))

    @api.constrains('purchase_price')
    def constraint_cost(self):
        if self.purchase_price <= 0:
            raise UserError(_('Cost must be grater than 0'))

    @api.onchange('amount_untaxed', )
    def _onchange_amount_untaxed(self):
        crm_lead_id = self.env['crm.lead'].search([('id', '=', self.opportunity_id.id)])
        sale_order_id = self.env['sale.order'].search([('opportunity_id', '=', self.opportunity_id.id)])

        sum = 0
        for record in sale_order_id:
            sum += record.amount_untaxed
        print(sum)
        crm_lead_id.expected_revenue = sum


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.constrains('purchase_price')
    def constraint_purchase_price(self):
        if self.product_id.categ_id.name != 'accs':
            if self.purchase_price <= 0:
                raise ValidationError(_("Cost Can not be (0) When Product Category is not accs !"))
