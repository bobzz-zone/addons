# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = ["Customer:Link/Customer:200","POS:Data:100","Invoice:Link/Sales Invoice:150","Qty:Int:50","Gross Sales:Currency:150","Rate Commision:Data:50","Commission:Currency:100"]
	data = frappe.db.sql("""select
s.customer ,s.letter_head,
s.name ,
sum(si.qty) ,
sum(si.net_amount) ,
c.default_commission_rate  ,
(s.grand_total*c.default_commission_rate/100)  
from `tabSales Invoice Item` si 
join `tabSales Invoice` s on si.parent = s.name 
join `tabCustomer` c on s.customer=c.name
where s.docstatus=1 and c.default_sales_partner = "{}" and s.posting_date between "{}" and "{}" group by si.parent """.format(filters.get("partner"),filters.get("from"),filters.get("to")),as_list=1)
	return columns, data

