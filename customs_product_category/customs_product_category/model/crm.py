from odoo import models, api, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _order = "priority desc, id desc"
    _primary_email = 'email_from'

    name = fields.Char(
        'Opportunity', index=True, required=True,
        compute='_compute_name', readonly=False, store=True)
    partner_id = fields.Many2one(
        'res.partner', string='Customer', check_company=True, required=True, index=True, tracking=10,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="Linked partner (optional). Usually created when converting the lead. You can find a partner by its Name, TIN, Email or Internal Reference.")
    expected_revenue = fields.Monetary('Expected Revenue', currency_field='company_currency', required=True,
                                       tracking=True)
    probability = fields.Float(
        'Probability', group_operator="avg", copy=False, required=True,
        compute='_compute_probabilities', readonly=False, store=True)
    partner_id = fields.Many2one(
        'res.partner', string='Customer', check_company=True, required=True, index=True, tracking=10,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="Linked partner (optional). Usually created when converting the lead. You can find a partner by its Name, TIN, Email or Internal Reference.")
    email_from = fields.Char(
        'Email', tracking=40, index=True, required=True,
        compute='_compute_email_from', inverse='_inverse_email_from', readonly=False, store=True)
    phone = fields.Char(
        'Phone', tracking=50, required=True,
        compute='_compute_phone', inverse='_inverse_phone', readonly=False, store=True)
    user_id = fields.Many2one(
        'res.users', string='Salesperson', required=True, default=lambda self: self.env.user,
        domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]",
        check_company=True, index=True, tracking=True)
    team_id = fields.Many2one(
        'crm.team', string='Sales Team', check_company=True, index=True, tracking=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        compute='_compute_team_id', ondelete="set null", readonly=False, store=True)
    date_deadline = fields.Date('Expected Closing', required=True,
                                help="Estimate of the date on which the opportunity will be won.")

    # priority = fields.Selection(
    #     crm_stage.AVAILABLE_PRIORITIES, string='Priority', index=True,
    #     default=crm_stage.AVAILABLE_PRIORITIES[0][0])

    tag_ids = fields.Many2many(
        'crm.tag', 'crm_tag_rel', 'lead_id', 'tag_id', string='Tags', required=True,
        help="Classify and analyze your lead/opportunity categories like: Training, Service")
    opportunity_type = fields.Many2one('opportunity.type', string="Opportunity Type")
