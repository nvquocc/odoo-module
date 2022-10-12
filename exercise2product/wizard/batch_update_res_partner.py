from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

import logging

_logger = logging.getLogger(__name__)


class BatchUpdateWizard(models.TransientModel):
    _name = "res.partner.batchupdate.wizard"
    valid_coupon = fields.Char(string="Valid coupon")

    def multi_update(self):
        ids = self.env.context['active_ids']  # selected record ids
        my_sale_order = self.env["res.partner"].browse(ids)
        new_data = {}

        if self.valid_coupon:
            new_data["valid_coupon"] = self.valid_coupon
        my_sale_order.write(new_data)
