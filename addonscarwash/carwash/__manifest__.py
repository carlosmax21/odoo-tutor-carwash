# -*- coding: utf-8 -*-
{
    'name': "carwash",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/Pegawai/pegawai_view.xml',
        'views/Pegawai/pencuci_view.xml',
        'views/Pegawai/pengelap_view.xml',
        'views/Finance/cucimobil_view.xml',
        'views/Finance/purchase_view.xml',
        'views/Storage/aksesoris_view.xml',
        'report/Pegawai/report_pencuci.xml',
        'report/Pegawai/report_pengelap.xml',
        'report/Storage/report_aksesoris.xml',
        'report/Finance/report_cucimobil.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
