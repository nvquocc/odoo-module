from odoo import models, fields


class HrDepartment(models.Model):
    _inherit = "hr.department"
    limit_money = fields.Integer('Hạn mức chi tiêu theo tháng')
