# -*- coding: utf-8 -*-

from odoo import models, api, exceptions

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def write(self, values):
        res = super(SaleOrder, self).write(values)
        for r in self:
            if r.opportunity_id:
                opportunity = self.env['crm.lead'].browse(r.opportunity_id.id)
                # Prevent recursion with the no_recursion flag
                if not self._context.get('no_recursion'):
                    opportunity.write({
                        'partner_id': r.partner_id.id,
                        'user_id': r.user_id.id,
                        'team_id': r.team_id.id,
                        'campaign_id': r.campaign_id.id,
                        'medium_id': r.medium_id.id,
                        'source_id': r.source_id.id,
                    })
        return res
