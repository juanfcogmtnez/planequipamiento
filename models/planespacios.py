# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Planespacios(models.Model):
	_name = "planespacios"
	_inherits = {'project.task':'plan'}
	plan = fields.Many2one('project.task')  
	active = fields.Boolean(string="Activo",default=True)
	espacios_ids = fields.One2many(
		comodel_name='espacios',
		inverse_name = 'name',
		string = "Espacios",
	)

