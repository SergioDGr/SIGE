from odoo import api, models, fields


class Alumno(models.Model):

    _name = 'instituto.alumno'
    _description = 'Modelo para almacenar las informacion de los alumnos'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento', required=True)
    direccion = fields.Char(string='Dirección')
    codigo_postal = fields.Char(string='Código Postal')
    email = fields.Char(string='Email')
    ciclo_formativo = fields.Selection([('dam', 'DAM'), ('daw', 'DAW'), ('asir', 'ASIR')], default='dam',
                                       string='Ciclo Formativo', tracking=True)
    coche = fields.Boolean(string='Coche')
    otros = fields.Text(string='Otros')
    nota_media = fields.Float(string='Nota Media', default=5.0)
    empresa = fields.Many2one('instituto.empresa', string='Empresa')
    tutor = fields.Many2one('instituto.tutoria_fct', string='Tutor')

    @api.multi
    def abrir_formulario(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'instituto.alumno',
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
        }
