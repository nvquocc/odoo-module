from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import re


class ResPartner(models.Model):
    _inherit = "res.partner"
    has_coupon = fields.Boolean(string="Has a coupon", default=False)
    valid_coupon = fields.Char(string="Valid coupon")

    @api.constrains("valid_coupon")
    def show_discount_code(self):
        for record in self:
            get_text_from_list = re.findall(r'\d', str(record.valid_coupon))
            get_number_from_text = "".join(get_text_from_list)
            if str(record.valid_coupon)[0:4] == 'VIP_' and int(get_number_from_text) <= 100:
                return str(str(record.valid_coupon) + str(get_number_from_text))
            else:
                raise ValidationError("Mã code không hợp lệ")
