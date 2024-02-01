# Importamos los módulos necesarios de Odoo
from odoo import models, fields


# Definimos la clase Empresa que hereda de models.Model
class Empresa(models.Model):
    """Clase que representa el modelo Empresa"""

    # Nombre técnico del modelo
    _name = 'instituto.empresa'
    # Descripción del modelo
    _description = 'Modelo para almacenar las informacion de las empresas'

    # Campo para el nombre de la empresa. Es obligatorio.
    nombre = fields.Char(string='Nombre', required=True)
    # Campo para la dirección de la empresa.
    direccion = fields.Char(string='Dirección')
    # Campo para el teléfono de la empresa.
    telefono = fields.Char(string='Telefono')
    # Campo para el departamento de la empresa. Es una selección entre 'Informática', 'Comercio', 'Marketing' y
    # 'Administración'. Por defecto es 'Informática'.
    departamento = fields.Selection([('informatica', 'Informática'), ('comercio', 'Comercio'),
                                     ('marketing', 'Marketing'), ('administracion', 'Administración')],
                                    default='informatica', string='Departamento', tracking=True)
    # Campo para los alumnos de la empresa. Es una relación One2many con el modelo 'instituto.alumno'.
    lst_alumnos = fields.One2many('instituto.alumno', 'empresa', string='Alumnos')
