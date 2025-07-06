# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class LibroAPI(http.Controller):

    @http.route('/api/libros', auth='public', type='json', methods=['POST'], csrf=False)
    def crear_libro(self):
        data = request.httprequest.json
        _logger.info(">>> Datos recibidos: %s", data)

        # Validación básica
        if not data.get('titulo'):
            return {'error': 'El campo "titulo" es obligatorio.'}

        try:
            libro = request.env['biblioteca.libro'].sudo().create({
                'titulo': data.get('titulo'),
                'autor': data.get('autor'),
                'fecha_publicacion': data.get('fecha_publicacion'),
                'numero_paginas': data.get('numero_paginas'),
            })

            return {
                'id': libro.id,
                'mensaje': 'Libro creado correctamente'
            }

        except Exception as e:
            _logger.error("Error al crear el libro: %s", str(e))
            return {'error': 'No se pudo crear el libro.'}
