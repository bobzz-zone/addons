// Copyright (c) 2013, Bobzz Zone and contributors
// For license information, please see license.txt

frappe.query_reports["POS Sales Transaction Summary"] = {
	"filters": [
		{
			"fieldname":"date",
			"label": "Date",
			"fieldtype": "Date",
			"default": get_today(),
			"reqd": 1
		},
                {
                        "fieldname":"territory",
                        "label": "Territory",
                        "fieldtype": "Link",
                        "options": "Territory"
                },
		{
			"fieldname":"user",
			"label": "User",
			"fieldtype": "Link",
			"options": "POS Profile"
		},
		{
			"fieldname":"mode",
			"label": "Payment Mode",
			"fieldtype": "Link",
			"options": "Mode of Payment",
			"default":"Cash"
		}
	]
}
