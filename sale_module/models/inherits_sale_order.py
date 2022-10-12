from odoo import fields, models, _
from odoo.exceptions import ValidationError


class InheritsSaleOrder(models.Model):
    _inherit = 'sale.order'
    plan_sale_order_id = fields.One2many("plan.sale.order", 'price_id', "Plan Sale Order ID", store=True)
    display_plan = fields.Many2one('plan.sale.order', string="Display Plant Order", compute='_coupute_display_plan',
                                   readonly=True)

    def action_confirm(self):
        res = super(InheritsSaleOrder, self).action_confirm()
        if not self.display_plan.state:
            raise ValidationError("Không có kế hoạch ")
        if self.display_plan.state == 'refused':
            raise ValidationError("Kế hoạch kinh doanh chưa được phê duyệt")
        return res

    def _coupute_display_plan(self):
        for rec in self:
            display_plan = False
            if rec.plan_sale_order_id:
                display_plan = rec.plan_sale_order_id[0].id
            rec.display_plan = display_plan

    def create_business_plan(self):
        for rec in self:
            if self.env['plan.sale.order'].search([('price_id', '=', self.id)]).price_id.name == rec.name:
                raise ValidationError(f"Đã tồn tại bản ghi {rec.name}")
            else:
                return {
                    'name': _('Business Plan Form'),
                    'view_mode': 'form',
                    'view_id': False,
                    'view_type': 'form',
                    'res_model': 'plan.sale.order',
                    'type': 'ir.actions.act_window',
                    'target': 'self',
                    'context': {'default_price_id': self.id}
                }
