# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
# from datetime import date, timedelta, datetime
# from odoo.exceptions import UserError

class InstitutoAsignatura(models.Model):
    _name = "instituto.asignatura"
    _description = "Tabla de las asignaturas"

    # Para ver las tablas:
    # sudo su postgres
    # psql
    # \c dm2
    # \d instituto_practicas

    name = fields.Char(string='Nombre', required=True)


    