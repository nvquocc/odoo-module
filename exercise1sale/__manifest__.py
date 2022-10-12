{
    'name': "Exercise 1",
    'summary': "Bài tập 1 Odoo",
    'description': """Bài tập 1 Odoo
            
""",
    'author': "Nguyen Van Quoc",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '15.0',
    'depends': ['base', 'sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/group.xml',
        'views/odoo_sale_view.xml',
        'views/res_partner_view.xml',
        'views/template.xml',
        'wizard/batch_update.xml',

    ],
    'demo': [
        # 'demo.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'exercise1sale/static/src/js/script.js'
        ]
    }
}
