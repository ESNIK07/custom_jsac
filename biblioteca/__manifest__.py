# -*- coding: utf-8 -*-
{
    'name': 'Biblioteca',
    'version': '1.0',
    'summary': 'Gestión de libros en biblioteca',
    'category': 'Tools',
    'author': 'Tu Nombre',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/libro_views.xml',
        'views/libro_menu.xml',
    ],
    'installable': True,
    'application': True,
}
