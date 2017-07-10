from __future__ import unicode_literals
import frappe

def asset():
	asset =frappe.db.sql("select name from tabAsset where docstatus=1",as_list=1)
	for a in asset:
		frappe.get_doc("Asset",a[0]).cancel()
