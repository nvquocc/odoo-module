from odoo import fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release, name'
    _rec_name = 'short_name'
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    short_name = fields.Char('Short Title', translate=True,
                             index=True)
    notes = fields.Text('Internal Notes')
    state = fields.Selection([('draft', 'Not Available'), ('available', 'Available'), ('lost', 'Lost')], 'State',
                             default="draft")
    description = fields.Html('Description', sanitize=True, strip_style=False)
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out Of Print?')
    date_updated = fields.Date('Last Updated')
    pages = fields.Integer('Number of Pages',
                           groups='base.group_user',
                           states={'lost': [('readonly', True)]},
                           help='Total book page count', company_dependent=False)
    active = fields.Boolean('Active', default=True)
    reader_rating = fields.Float(
        'Reader Average Rating',
        digits=(14, 4),  # Optional precision decimals,
    )
    author_ids = fields.Many2many('res.partner', string="Authors")
    cost_price = fields.Float(
        'Book Cost', digits='Book Price')
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    retail_price = fields.Monetary(
        'Retail Price',
        # optional: currency_field='currency_id',
    )
    publisher_id = fields.Many2one(
        'res.partner', string='Publisher',
        # optional:
        ondelete='set null',
        context={},
        domain=[],
    )


def name_get(self):
    for record in self:
        result = []

        rec_name = "%s (%s)" % (record.name, record.date_release)
        result.append((record.id, rec_name))
    return result
