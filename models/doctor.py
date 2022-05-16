# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "management"

    name = fields.Char(string='Name:', required=True)
    age = fields.Integer(string='Age:')
    specialised = fields.Char(string='Specialised:')
    zipcode = fields.Char(string='Zipcode:')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ], required=True,
                              default='male')
    address = fields.Text(string='Full Address:')
