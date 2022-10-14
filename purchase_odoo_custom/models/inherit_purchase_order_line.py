from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"
    vendor_suggest_id = fields.Many2one('res.partner', 'Nhà  cung cấp đề xuất')

    @api.onchange("vendor_suggest_id")
    def show_vendor_id(self):
        for rec in self:
            # print(rec.vendor_suggest_id.name)
            # print(rec.partner_id.name)
            print(rec.vendor_suggest_id.product_id.name)
            print(rec.partner_id.name)
# self.create_uid.partner_id.name || rec.partner_id.name