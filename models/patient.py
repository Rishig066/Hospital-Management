# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "management"

    name = fields.Char(string='Name:', required=True)
    age = fields.Integer(string='Age:', required=True)
    contact_No = fields.Intiger(string='Contact No:', required=True)
    Address = fields.Text(string='Full Address:')



