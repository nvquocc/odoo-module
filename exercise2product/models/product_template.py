from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    product_warranty = fields.Char(string="Product Warranty", readonly=True,
                                   store=True)
    date_from = fields.Date(string="Ngày bắt đầu", store=True)
    date_to = fields.Date(string="Ngày kết thúc", store=True)
    price_discount = fields.Float(string="Giá còn lại ", compute='_compute_price_discount', store=True, readonly=True)

    @api.constrains("date_from", "date_to")
    def _format_date(self):
        for rec in self:
            format_day = '%d/%m/%y'
            if rec.date_from and rec.date_to:
                df = str(rec.date_from.strftime(format_day)).replace("/", "")
                dt = str(rec.date_to.strftime(format_day)).replace("/", "")
                if rec.date_from > rec.date_to and rec.date_to < rec.date_from:
                    raise ValidationError("Error")
                if not rec.date_from:
                    self.product_warranty = str("PWR/{}".format(df))
                    print(self.product_warranty)
                if rec.date_to:
                    self.product_warranty = str("PWR/{}".format(dt))
                self.product_warranty = str("PWR/{}/{}".format(df, dt))

    @api.depends("price_discount", "product_warranty", "date_from", "date_to")
    def _compute_price_discount(self):
        for rec in self:
            format_date = "%d/%m/%Y"
            if not rec.date_from and not rec.date_to:
                break
            if self.date_from and self.date_to:
                date_now = datetime.now()
                df = str(datetime.strftime(self.date_from,format_date))
                dt = str(datetime.strftime(self.date_to,format_date))
                dn = str(datetime.strftime(date_now,format_date))
                if dt < dn:
                    raise ValidationError(f"Mã {self.product_warranty} chưa hết hạn nên không có mã giảm giá nào cả")
                else:
                    rec.price_discount = rec.list_price - (rec.list_price * 0.1)

            if not rec.product_warranty:
                self.price_discount = rec.list_price - (rec.list_price * 0.1)

# @api.depends("product_warranty", "list_price", "date_from", "date_to")
# def _compute_test(self):
#     for rec in self:
#         format_day = '%d/%m/%y'
#         date_today = str(datetime.datetime.now().strftime(format_day))
#         if rec.date_to:
#             date_to1 = datetime.datetime.strftime(rec.date_to, format_day)
#             if date_to1 > date_today:
#                 self.price_discount = rec.list_price - (rec.list_price * 0.1)
#             else:
#                 rec.price_discount = rec.list_price

# self.price_discount = rec.list_price - (rec.list_price * 0.1)
# if str(rec.product_warranty):
# if

# if str(rec.product_warranty):

# else:
#     dt = (rec.date_to.strftime(format_day))
#     dn = date_tody.strftime(format_day)
#     if dt > dn:
#         self.price_discount = rec.list_price - (rec.list_price * 0.1)

# print(type(rec.date_from))
# if rec.date_to < date.today():
#     if str(rec.product_warranty):
#         self.price_discount = rec.list_price
# # if rec.date_to > date.today() and not str(rec.product_warranty):
# #     self.price_discount = rec.list_price - (rec.list_price * 0.1)
# # if not rec.product_warranty:
# #     self.price_discount = rec.list_price - (rec.list_price * 0.1)
# #     # print(self.price_discount)
