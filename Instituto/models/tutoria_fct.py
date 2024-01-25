from odoo import models, fields


class TutoriaFCT:
    _name = 'instituto.tutoria_fct'
    _description = 'Modelo para almacenar las informacion de las tutorias FCT'

    tutor = fields.Char(string='Tutor', required=True)
    email = fields.Char(string='Email', required=True)
    telefono = fields.Char(string='Telefono', required=True)
    alumnos = fields.One2many('instituto.alumno', 'tutor', string='Alumnos')

