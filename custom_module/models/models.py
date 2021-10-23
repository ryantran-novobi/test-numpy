# -*- coding: utf-8 -*-

import numpy as np
from odoo import models, fields, api


class custom_module(models.Model):
    _name = 'custom_module.custom_module'
    _description = 'custom_module.custom_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
            a = np.arange(15).reshape(3, 5)
            print(a.shape)
