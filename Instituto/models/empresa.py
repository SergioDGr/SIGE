from odoo import models, fields


class Empresa(models.Model):
    _name = 'instituto.empresa'
    _description = 'Modelo para almacenar las informacion de las empresas'

    nombre = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Telefono')
    departamento = fields.Selection([('informatica', 'Informática'), ('comercio', 'Comercio'),
                                     ('marketing', 'Marketing'), ('administracion', 'Administración')],
                                    default='informatica', string='Departamento', tracking=True)
    lst_alumnos = fields.One2many('instituto.alumno', 'empresa', string='Alumnos')
