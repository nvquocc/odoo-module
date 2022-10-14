from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    department_id = fields.Many2one('hr.department', 'Phòng ban', required=True)

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        print("Da ke thua ")
        return res

    @api.onchange("order_line")
    def onchange_product(self):
        for rec in self.order_line:
            print(rec.product_id.name)
            print(rec.partner_id.name)

    # @api.onchange("order_line")
    # def _onchange_order_line(self):
    #     for rec in self:
    #         print(rec.product_id.variant_seller_ids.name.name)
    #         print(rec.partner_id.name)
    #         if rec.product_id.variant_seller_ids.name.name == rec.partner_id.name:
    #
