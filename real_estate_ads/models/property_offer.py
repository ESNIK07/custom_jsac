from odoo import models, fields, api
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Properties Offers'

    # name = fields.Char(string='Name', required=True)
    price = fields.Float(string='Price')
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status', default='pending')
    partner_id = fields.Many2one(string='Customer', comodel_name='res.partner')
    property_id = fields.Many2one(string='Property', comodel_name='estate.property')
    validity = fields.Integer(string='Validity')
    deadline = fields.Date(string='Deadline', default=fields.Date.today() , compute='_compute_deadline')
    creation_date = fields.Date(string='Creation Date')
    
    @api.depends('validity', 'creation_date')
    def _compute_deadline(self):
        for record in self:
            if record.creation_date and record.validity:
                record.deadline = record.creation_date + timedelta(days=record.validity)
            else:
                record.deadline = False
    
    

