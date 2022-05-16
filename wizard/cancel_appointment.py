# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalDoctor(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "management"

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')

    def cancel_appointment(self):
        return
