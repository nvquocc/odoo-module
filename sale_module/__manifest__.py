{
    'name': 'Sale Module',
    'version': '15.0',
    'summary': 'Sale Module ',
    'description': 'Phê duyệt phương án bán hàng',
    'category': 'Category',
    'author': 'Nguyen Van Quoc',
    'website': 'google.com.vn',
    'depends': [
        'sale', 'base', 'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/group.xml',
        'views/plan_sale_order_views.xml',
        'views/approved_sale_order.xml',
        'views/inherit_view.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False
}
