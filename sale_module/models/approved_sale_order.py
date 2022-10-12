from odoo import fields, models, api


class ApprovedSaleOrder(models.Model):
    _name = "approved.sale.order"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    plan_sale_order_id = fields.Many2one("plan.sale.order", 'Name ID', tracking=True)
    name = fields.Many2one("res.partner", string="Tên",required=True)
    state = fields.Selection(
        [('new', 'Mới'), ('send_approve', 'Gửi duyệt'), ('approved', 'Duyệt'), ('refused', 'Từ chối duyệt')],
        'Trạng thái phê duyệt', default='new', tracking=True, readonly=True)
    is_user = fields.Boolean(default=False, compute="compute_user")
    button_invisble = fields.Boolean('Show Button', compute='_compute_button_invisible')

    def compute_user(self):
        user = self.env.user
        for rec in self:
            if user.partner_id.id == rec.name.id:
                rec.is_user = True
            else:
                rec.is_user = False

    def approved_button(self):
        partner_ids = []
        self.state = 'approved'
        for rec in self:
            if self.state == 'approved':
                partner_ids.append(self.plan_sale_order_id.create_uid.partner_id.id)
                self.plan_sale_order_id.message_post(
                    body=f"Chấp nhận gửi thông tin cho {self.plan_sale_order_id.create_uid.partner_id.name}  ",
                    message_type="notification",
                    partner_ids=[self.plan_sale_order_id.create_uid.partner_id.id])

    def refuse_button(self):
        self.state = 'refused'
        if self.state == 'refused':
            self.plan_sale_order_id.message_post(
                body=f"Từ chối gửi thông tin cho {self.plan_sale_order_id.create_uid.partner_id.name}")

    @api.depends("plan_sale_order_id.state")
    def _compute_button_invisible(self):
        for rec in self:
            rec.button_invisble = not (rec.is_user and (rec.plan_sale_order_id.state == 'send_approve'))
