# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalPatient(models.Model):
    _name = "hospital.appointment"
    _description = "appointment model"

    patient_id = fields.Many2one('hospital.patient', string="patient")
    date_appointment = fields.Date(string="Appointment Date:",default=fields.Date.context_today)
    appointment_time = fields.Datetime(string='Appointment Time:', default=fields.Datetime.now)
    gender = fields.Selection(related='patient_id.gender', readonly=False)
