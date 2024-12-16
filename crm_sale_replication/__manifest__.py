# -*- coding: utf-8 -*-
{
    'name': "crm_sale_replication",

    'summary': """
        Creates a replication of modifications made to Opportunities and Quotations""",

    'description': """
        This module creates a link between Opportunities and Quotes.
        Any modifications made to one will be reflected in the other,
        in the fields where it is possible, obviously.

        opportunity
        sales
        CRM
        Lead
        Duplicate
        Opportunities
        sale
        link
        opportunity sale
        sale order
        sale order Opportunity


    """,
    'author': "Pingo Tecnologia",
    'support': 'contato@pingotecnologia.com.br',
    'images': ['static/description/capa.png'],
    'licence': 'LGPL',
    'author': "Éder Brito - Pingo Tecnologia",
    'website': "https://pingotecnologia.com.br",

    'category': 'sale',
    'version': '1.0',

    'depends': [
      'sale_crm',
      'sale_management',
    ],
}
