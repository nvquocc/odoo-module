from odoo import fields, models, api
from odoo.exceptions import ValidationError


class PlanSaleOrder(models.Model):
    _name = "plan.sale.order"
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Tên", required=True)
    price_id = fields.Many2one('sale.order', 'Báo giá', ondelete='cascade', readonly=True)
    info_business_plan = fields.Text(string="Phương án kinh doanh", required=True)
    approval_id = fields.One2many('approved.sale.order', 'plan_sale_order_id', 'Approval ID', tracking=True)
    state = fields.Selection(
        [('new', 'Mới'), ('send_approve', 'Gửi duyệt'), ('approved', 'Duyệt'), ('refused', 'Từ chối duyệt')],
        'Trạng thái phê duyệt', default='new', tracking=True, compute='_compute_state', store=True)

    @api.constrains("approval_id")
    def check_user_approval_id(self):
        for rec in self.approval_id:
            if rec.name.name == self.approval_id.create_uid.partner_id.name:
                raise ValidationError("Không được chọn chính người dùng đó")

    def send_approved_button(self):
        check = 0
        partner_ids = []
        self.state = 'send_approve'
        for rec in self.approval_id:
            if self.state == 'send_approve':
                partner_ids.append(rec.name.id)
                check = check + 1
                self.message_post(body=f"Đã gửi thông tin cho {rec.name.name} phương án kinh doanh",
                                  partner_ids=partner_ids)

            rec.state = 'send_approve'

    @api.depends("approval_id.state")
    def _compute_state(self):
        for rec in self:
            approve_list = rec.approval_id.mapped('state')
            if 'refused' in approve_list:
                rec.state = 'refused'
            approve_list = [x == 'approved' for x in approve_list]
            if all(approve_list):
                rec.state = 'approved'
