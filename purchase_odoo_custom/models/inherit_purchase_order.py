from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    department_id = fields.Many2one('hr.department', 'Phòng ban', required=True)

    def show_name_of_purchase_order(self):
        for rec in self.order_line:
            print(rec.partner_id.name)