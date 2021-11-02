# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Planequipamiento(models.Model):
	_name = "planequipamiento"
	_inherits = {'project.task':'plan'}
	plan = fields.Many2one('project.task') 	
	active = fields.Boolean(string="Activo",default=True)
