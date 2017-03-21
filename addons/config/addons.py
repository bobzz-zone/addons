from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {
                        "label": _("Documents"),
                        "icon": "icon-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "POS Shift Daily Reports",
                                        "description": _("Cash Movement for POS User"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "POS Cash",
                                        "description": _("For Managers to take cash"),
                                }
			]
		},
                {
                        "label": _("Reports"),
                        "icon": "icon-list",
                        "items": [
                              #  {
                              #          "type": "report",
                              #          "is_query_report": True,
                              #          "name": "Cash Only POS Sales Transaction",
                              #          "doctype": "POS Shift Daily Reports",
                              #  },
                                {
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "POS Sales Transaction Summary",
                                        "doctype": "POS Shift Daily Reports",
                                },
                                {
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Cashier Cash Summary Report",
                                        "doctype": "POS Cash",
                                },
                                {
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Sales Commision Report",
                                        "doctype": "POS Cash",
                                }
                        ]
                },
	]
