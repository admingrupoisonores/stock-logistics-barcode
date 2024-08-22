# Copyright (C) 2022 Akretion
# Copyright (C) 2024 Grupo Isonor
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Delivery Input Barcode",
    "version": "15.0.1.0.0",
    "category": "Tools",
    "website": "https://github.com/OCA/stock-logistics-barcode",
    "author": "Grupo Isonor, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "summary": "Add Move line with barcode",
    "maintainers": ["neitherkx"],
    "depends": [
        "stock",
        "barcode_action",
    ],
    "data": [
        "views/stock.xml",
    ],
    "demo": [],
}
