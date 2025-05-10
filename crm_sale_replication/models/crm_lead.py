#-*- coding: utf-8 -*-

from odoo import models, api, exceptions

class Lead(models.Model):

    _inherit = 'crm.lead'

    def write(self, values):
        res = super(Lead, self).write(values)
        for r in self:
            sale_orders = self.env['sale.order'].search([('opportunity_id', '=', r.id)])
            for order in sale_orders:
                if order.state in ['draft', 'sent']:  # Check if the sale order is in draft or sent state
                    # Avoid recursion by using the context flag
                    if not self._context.get('no_recursion'):
                        order.with_context(no_recursion=True).write({
                            'partner_id': r.partner_id.id,
                            'user_id': r.user_id.id,
                            'team_id': r.team_id.id,
                            'campaign_id': r.campaign_id.id,
                            'medium_id': r.medium_id.id,
                            'source_id': r.source_id.id,
                        })
        return res
