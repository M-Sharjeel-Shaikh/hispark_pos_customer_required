{
    "name": "POS Customer Required | POS Customer Mandatory",
    "summary": "Require selecting a customer before validating an order in POS",
    "description":""" This module enforces customer selection in the Point of Sale. Cashiers cannot validate or confirm 
        an order without assigning a customer. It helps ensure accurate sales tracking, loyalty programs, and proper invoicing.
    """,

    "version": "16.0",
    "category": "Point Of Sale",
    "author": "Hi Spark Solutions",
    "company": "Hi Spark Solutions",
    "maintainer": "Hi Spark Solutions",
    "website": "https://www.hisparksolutions.com/",

    "depends": ["point_of_sale"],
    "demo": [],
    "data": ["views/pos_config_view.xml"],
    "assets": {
        "point_of_sale.assets": [
            "hispark_pos_customer_required/static/src/js/pos_customer_required.js",
            # "hispark_pos_customer_required/static/src/**/*.css",
        ],
    },

    "images": ["static/description/banner.gif"],
    "qweb": [],
    "live_test_url": "",

    "license": "OPL-1",
    "application": True,
    "auto_install": False,
    "installable": True,
    "price": "5",
    "currency": "USD",
}
