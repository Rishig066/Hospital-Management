# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital management',
    'version': '1.1',
    'summary': '',
    'sequence': 10,
    'description': """hospital management software""",
    'category': '',
    'website': '',
    'images': [],
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_appointment.xml',
        'views/patient.xml',
        'views/menu.xml',
        'views/appointment.xml',
        'views/doctor.xml',



    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}