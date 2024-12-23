# -*- coding: utf-8 -*-
{
    'name': "Payroll PPH 21",

    'summary': """Modul HR - PPH 21""",

    'description': """
        Module ini digunakan untuk menghitung PPH 21
    """,

    'author': "PT ApirCommerce",
    'website': "https://www.cybrosys.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_payroll_community'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/ptkp_views.xml',
        'views/rate_views.xml',
        'views/hr_employee_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
