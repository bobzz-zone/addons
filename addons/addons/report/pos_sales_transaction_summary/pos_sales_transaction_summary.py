# Copyright (c) 2013, Bobzz Zone and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Customer:Data:300","POS:Data:150","Total:Currency:300"], []
	territory,mop,user="","",""
	if filters.get("mode") and filters.get("mode")!="":
		mop=""" and sit.mode_of_payment="{}" """.format(filters.get("mode"))
	if filters.get("user") and filters.get("user")!="":
		user=""" and si.owner="{}" """.format(filters.get("user"))
	if filters.get("territory") and filters.get("territory")!="":
		t = frappe.db.sql("""select lft,rgt from tabTerritory where name="{}" """.format(filters.get("territory")),as_dict=1)
		lft,rgt=0,0
		#frappe.throw(t)
		for d in t:
			lft =d["lft"]
			rgt=d["rgt"]
		t = frappe.db.sql("""select name from tabTerritory where lft>= {} and rgt<= {} """.format(lft,rgt),as_list=1)
		temp=""
		for d in t:
			if temp=="":
				temp=""" "{}" """.format(d[0])
			else:
				temp="""{},"{}" """.format(temp,d[0])
		territory=""" and si.territory IN ({}) """.format(temp)
		#frappe.throw(territory)
	data = frappe.db.sql("""select si.customer,si.letter_head,sum(sit.amount-si.change_amount) from `tabSales Invoice Payment` sit 
		join `tabSales Invoice` si on sit.parent=si.name
		where si.is_pos=1 and si.docstatus=1 and si.posting_date ="{}" {} {} {} group by si.customer,si.letter_head
		""".format(filters.get("date"),user,territory,mop) ,as_list=1)
	#data = frappe.db.sql("""select si.customer,si.letter_head,sum(sit.qty),sum(sit.net_amount) 
	#	from `tabSales Invoice Item` sit join `tabSales Invoice` si on sit.parent=si.name 
	#	where si.is_pos=1 and si.docstatus=1 and si.posting_date ="{}" {} {} {} group by si.customer,si.letter_head 
	#	""".format(filters.get("date"),user,territory,mop),as_list=1)
	#frappe.throw("""select si.customer,si.letter_head,sum(sit.qty),sum(sit.net_amount)
        #        from `tabSales Invoice Item` sit join `tabSales Invoice` si on sit.parent=si.name
        #        where si.is_pos=1 and si.docstatus=1 and si.posting_date ="{}" {} {} {} group by si.customer,si.letter_head
        #        """.format(filters.get("date"),user,territory,mop))
	return columns, data
