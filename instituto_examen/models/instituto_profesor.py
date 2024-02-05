# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class InstitutoProfesor(models.Model):
    _name = "instituto.profesor"
    _description = "Tabla de las diferentes profesores"

    # Para ver las tablas:
    # sudo su postgres
    # psql
    # \c dm2
    # \d instituto_empresa

    # Tiene que tener si o si un atributo name porque sino coge el id
    name = fields.Char(required=True, string='Nombre')
    apellidos = fields.Char(required=True, string='Apellidos')
    email = fields.Char(string='Email')
    depar = fields.Selection(
        string='Departamento',
        selection=[('informática', 'Informática'), ('comercio', 'Comercio'), ('marketing', 'Marketing'),
                   ('administración', 'Administración')], default="informática", help="Departamento")

    # Si en el xml ponemos: <button name="accion_servidor" type="object" string="Ayuda"/>
    # Nos aparece un botón con un hipervínculo si descomentamos además la función:

    # def accion_servidor(self):
    #     return {
    #         "type": "ir.actions.act_url",
    #         "url": "https://odoo.com",
    #         "target": "self",
    #     }
