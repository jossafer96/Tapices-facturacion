# -*- coding: utf-8 -*-

{
    'name': 'Tapices Recibo ',
    'summary': """Factura personalizada""",
    'version': '12.0.1.0',
    'description': """Add Company Logo , Info & Customer name to POS Tapices""",
    'author': 'FE',
    'company': 'FE Techno Solutions',
    'website': 'http://www.unah.com.hn',
    'category': 'Point of Sale',
    'depends': ['base', 'point_of_sale'],
    'license': 'AGPL-3',
    'data': [],
    'qweb': ['static/src/xml/pos.xml',
    'static/src/js/models.js',
    ],
    'demo': [
        'views/tapices.xml',
    ],
    'installable': True,
    'auto_install': False,

}
