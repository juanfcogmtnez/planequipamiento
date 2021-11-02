# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Espacios(models.Model):
	_name = "espacios"
	_inherit = ['image.mixin']
	name = fields.Char(string='Espacio')
	active = fields.Boolean(string = 'Activo',default=True)
	codigo = fields.Char(string="codigo")
	description = fields.Text(string='Descripción')
	superficie = fields.Float(string='Superficie')
	bloque = fields.Char(string='Bloque')
	planta = fields.Char(string='Planta')
	plan_id = fields.Many2one(comodel_name='planespacios', string = 'Plan de espacio')
