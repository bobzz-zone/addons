# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bobzz Zone and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import frappe.model.docfield
from frappe.utils import  flt, cint

class POSShiftDailyReports(Document):
	def on_cancel(self):
		frappe.db.set_value("POS Groups",self.territory,"cash",self.amount_left)
		frappe.db.set_value("POS Groups",self.territory,"deposit",flt(self.cash_left))
	def on_submit(self):
		#pos_group=frappe.db.get("POS Group",{"territory":self.territory})
		#frappe.throw(pos_group)
		frappe.db.set_value("POS Groups",self.territory,"cash",self.at_chasier)
		frappe.db.set_value("POS Groups",self.territory,"deposit",flt(self.cash_left)+flt(self.deposit))
		pass
#		pos_group=frappe.db.get("POS Group",{"territory":self.territory})

	def validate(self):
#		user=frappe.get_user()
		pos_profile=frappe.db.get("POS Profile",{"user":frappe.session.user})
		if not pos_profile:
			frappe.throw("Cant be saved by user that doesnt have POS Profile")
		if not self.from_user:
			isfound=frappe.db.get("POS Shift Daily Reports",{"docstatus":0,"from_user":frappe.session.user})
			if isfound:
				frappe.throw("You have pending shift document. Please finish it..")
			self.from_user=frappe.session.user
		if self.from_user != frappe.session.user:
			frappe.throw("This Document must be updated or submited by {}".format(self.from_user))
		#if not self.territory:
#			pos_profile=frappe.db.get("POS Profile",{"user":frappe.session.user})
		self.territory=pos_profile.territory
		pos_group=frappe.db.get("POS Groups",{"territory":self.territory})
		if pos_group and pos_group!=None:
#			frappe.throw(pos_group)
			self.cash_left=pos_group.deposit
			self.amount_left=pos_group.cash
		else:
			self.cash_left=0
			self.amount_left=0
			row=frappe.get_doc({"doctype":"POS Groups","territory":self.territory})
			row.insert(ignore_permissions=True)
#		last_data = frappe.db.sql("""select name,at_chasier,amount_left,total_sales,deposit,cash_left,counter from `tabPOS Shift Daily Reports` where territory="{}" order by counter desc  """.format(self.territory),as_dict=1)
#		if not last_data:
#			self.counter=0
#			self.cash_left=0
#			self.amount_left=0
#		else:
#			self.counter=cint(last_data[0]['counter'])+1
#			self.link=last_data[0]['name']
			
		self.at_chasier=flt(self.amount_left)+flt(self.total_sales)-flt(self.deposit)
#	        frappe.throw(frappe.session.user)
	pass

@frappe.whitelist()
def on_validate_data(doc,method):
	user=frappe.get_user()
	frappe.throw(user)
	#cash = frappe.db.get("POS Group",{"territory":})
	pass
