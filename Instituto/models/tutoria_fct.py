# Importamos los módulos necesarios de Odoo
from odoo import models, fields


# Definimos la clase TutoriaFCT que hereda de models.Model
class TutoriaFCT(models.Model):
    """Clase que representa el modelo Tutoria FCT"""

    # Nombre técnico del modelo
    _name = 'instituto.tutoria_fct'
    # Descripción del modelo
    _description = 'Modelo para almacenar las informacion de las tutorias FCT'

    # Campo para el nombre del tutor. Es obligatorio.
    tutor = fields.Char(string='Tutor', required=True)
    # Campo para el correo electrónico del tutor. Es obligatorio.
    email = fields.Char(string='Email', required=True)
    # Campo para el número de teléfono del tutor. Es obligatorio.
    telefono = fields.Char(string='Telefono', required=True)

    # Campo para los alumnos del tutor. Es una relación One2many con el modelo 'instituto.alumno'.
    alumnos = fields.One2many('instituto.alumno', 'tutor', string='Alumnos')
