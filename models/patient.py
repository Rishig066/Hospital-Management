# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "management"

    name = fields.Char(string='Name:', required=True)
    age = fields.Integer(string='Age:')
    contact_No = fields.Char(string='Contact No:')
    zipcode = fields.Char(string='Zipcode:')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    address = fields.Text(string='Full Address:')



