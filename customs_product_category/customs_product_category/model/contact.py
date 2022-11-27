from odoo import models, api, fields


class CrmLead(models.Model):
    _inherit = 'res.partner'
    # _name = 'res.partner.category'

    name = fields.Char(string='Tag Name', required=True, translate=True)
    # parent_id = fields.Many2one('res.partner.category', required=True, string='Parent Category', index=True,
    #                             ondelete='cascade')
    street = fields.Char(required=True, )
    street2 = fields.Char(required=True, )
    city = fields.Char(required=True, )
    state_id = fields.Many2one("res.country.state", required=True, string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")

    zip = fields.Char(change_default=True, required=True, )
    country_id = fields.Many2one('res.country', required=True, string='Country', ondelete='restrict')
    function = fields.Char(string='Job Position', required=True, )
    phone = fields.Char(required=True, )
    mobile = fields.Char(required=True, )
    email = fields.Char(required=True, )
    website = fields.Char('Website Link', required=True, )
    title = fields.Many2one('res.partner.title', required=True, )
    # category_id = fields.Many2many('res.partner.category', column1='partner_id',
    #                                column2='category_id', string='Tags', default=_default_category)
