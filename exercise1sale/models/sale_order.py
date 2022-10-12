import re

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    customer_discount_code = fields.Char(string="Customer Discount Code", store=True)
    sale_order_discount_estimated = fields.Float('Calculated discount total', store=True, readonly=True)
    total_after_discount = fields.Float(string="Total after discount", readonly=True, compute="_compute_after_discount")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for rec in self:
            rec.customer_discount_code = rec.partner_id.valid_coupon

    @api.constrains("customer_discount_code")
    def show_discount_code(self):
        for record in self:
            get_text_from_list = re.findall(r'\d', str(record.customer_discount_code))
            get_number_from_text = "".join(get_text_from_list)
            if get_number_from_text:
                self.sale_order_discount_estimated = int(get_number_from_text) / 100
            if record.customer_discount_code:

                if str(record.customer_discount_code) == str(record.partner_id.valid_coupon):
                    record.partner_id.has_coupon = True
                    record.partner_id.valid_coupon = record.customer_discount_code
                    return str(str(record.customer_discount_code) + str(get_number_from_text))
                else:
                    raise ValidationError("Mã code không hợp lệ")

    @api.depends("total_after_discount")
    def _compute_after_discount(self):
        for rec in self:
            rec.total_after_discount = rec.amount_total * (1 - (self.sale_order_discount_estimated or 0.0))
            if rec.sale_order_discount_estimated == 1:
                rec.total_after_discount = rec.amount_total * (1 - (self.sale_order_discount_estimated or 0.0))

    @api.depends("amount_total", 'customer_discount_code')
    def _show_number_precent(self):
        for record in self:
            get_text_from_list = re.findall(r'\d', str(record.customer_discount_code))
            get_number_from_text = "".join(get_text_from_list)
            if get_number_from_text:
                self.test = int(get_number_from_text) / 100
            else:
                self.test = False
