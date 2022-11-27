# -*- coding: utf-8 -*-
{
    'name': "Customs-product-category""",
    'summary': """ Customs-product-category""",
    'description': """Customs-product-category""",
    'website': "",
    'category': 'INVENTORY',
    'depends': ['stock', 'sale', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        "security/security.xml",
        'views/product_category.xml',
        'views/crm.xml',
        'views/contact.xml',
        'views/crm_opportunity.xml',
        'data/data.xml',

    ],
}
