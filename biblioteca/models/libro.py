# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro de Biblioteca'
    _rec_name = 'titulo'

    titulo = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor')
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    numero_paginas = fields.Integer(string='Número de Páginas')
    es_largo = fields.Boolean(string='¿Es un libro largo?', compute='_compute_es_largo', store=True)

    @api.depends('numero_paginas')
    def _compute_es_largo(self):
        for libro in self:
            libro.es_largo = libro.numero_paginas > 300
