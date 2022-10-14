from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"
    vendor_suggest_id = fields.Many2one('res.partner', 'Nhà  cung cấp đề xuất')


