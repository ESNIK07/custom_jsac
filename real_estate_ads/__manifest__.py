# -*- coding: utf-8 -*-
{
    "name": "Real Estate Ads",
    "description": """
    A module to manage real estate ads.
    """,
    "author": "JSAC",
    "version": "1.0",
    "category": "Sale",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/property_view.xml",
        "views/property_type_view.xml",
        "views/property_tag_view.xml",
        "views/menu_items.xml",

    ],
    "installable": True,
    "application": True,
}