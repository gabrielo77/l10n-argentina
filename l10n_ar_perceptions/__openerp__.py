# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2007-2018 E-MIPS (http://www.e-mips.com.ar)
#    All Rights Reserved. Contact: info@e-mips.com.ar
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
{
    "name": "Extended configuration for Perceptions for ARGENTINA",
    "version": "1.0",
    "depends": [
        "base",
        "sale_stock",
        "l10n_ar_point_of_sale",
        "l10n_ar_perceptions_basic",
    ],
    "author": "E-MIPS",
    "website": "http://e-mips.com.ar",
    "license": "GPL-3",
    "category": "Own Modules",
    "description": """
    This module provide :
    A complete and complex configuration of Perceptions.
    """,
    "data": [
        'data/perception_data.xml',
        'views/perception_view.xml',
        'views/partner_view.xml',
        'views/account_invoice_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'active': False,
}
