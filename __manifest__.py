# -*- coding: utf-8 -*-
{
    'name': "prueba",
    'summary': """Prueba odoo""",
    'description': """Odoo module to buy 2nd hand laptops:""",
    'author': "Jon",
    'website': "https://github.com/SalesianosZaragoza/recuperacion-odoo-jonfeddan",
    'sequence': -100,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Prueba',
    'version': '0.1',
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/usuarios.xml',
        'views/portatiles.xml',
        'views/transacciones.xml',
        'views/menu.xml'
    ]
}