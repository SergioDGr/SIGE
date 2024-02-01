# Importamos los módulos necesarios de Odoo
from odoo import models, fields


# Definimos la clase Alumno que hereda de models.Model
class Alumno(models.Model):
    """Clase que representa el modelo Alumno"""

    # Nombre técnico del modelo
    _name = 'instituto.alumno'
    # Descripción del modelo
    _description = 'Modelo para almacenar las informacion de los alumnos'

    # Campo para el nombre del alumno. Es obligatorio.
    nombre = fields.Char(string='Nombre', required=True)
    # Campo para los apellidos del alumno. Es obligatorio.
    apellidos = fields.Char(string='Apellidos', required=True)
    # Campo para la fecha de nacimiento del alumno. Es obligatorio.
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento', required=True)
    # Campo para la dirección del alumno.
    direccion = fields.Char(string='Dirección')
    # Campo para el código postal del alumno.
    codigo_postal = fields.Char(string='Código Postal')
    # Campo para el correo electrónico del alumno.
    email = fields.Char(string='Email')
    # Campo para el ciclo formativo del alumno. Es una selección entre 'DAM', 'DAW' y 'ASIR'. Por defecto es 'dam'.
    ciclo_formativo = fields.Selection([('dam', 'DAM'), ('daw', 'DAW'), ('asir', 'ASIR')], default='dam',
                                       string='Ciclo Formativo', tracking=True)
    # Campo para indicar si el alumno tiene coche.
    coche = fields.Boolean(string='Coche')
    # Campo para otros detalles del alumno.
    otros = fields.Text(string='Otros')
    # Campo para la nota media del alumno. Por defecto es 5.0.
    nota_media = fields.Float(string='Nota Media', default=5.0)
    # Campo para la empresa del alumno. Es una relación Many2one con el modelo 'instituto.empresa'.
    empresa = fields.Many2one('instituto.empresa', string='Empresa')
    # Campo para el tutor del alumno. Es una relación Many2one con el modelo 'instituto.tutoria_fct'.
    tutor = fields.Many2one('instituto.tutoria_fct', string='Tutor')


