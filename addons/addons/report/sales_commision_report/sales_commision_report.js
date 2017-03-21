frappe.query_reports["Sales Commision Report"] = {
	"filters": [
		{
			"fieldname":"from",
			"label": "From",
			"fieldtype": "Date",
			"reqd": 1
		},
		{
			"fieldname":"to",
			"label": "To",
			"fieldtype": "Date",
			"reqd": 1
		},
		{
			"fieldname":"partner",
			"label": "Sales Partner",
			"fieldtype": "Link",
			"options": "Sales Partner",
			"reqd": 1
		}
]
}
