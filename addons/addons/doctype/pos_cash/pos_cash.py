# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bobzz Zone and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import  flt, cint
class POSCash(Document):
	def on_cancel(self):
		frappe.db.set_value("POS Groups",self.territory,"deposit",self.cash_amount)
	def on_submit(self):
		frappe.db.set_value("POS Groups",self.territory,"deposit",flt(self.cash_amount)-flt(self.cash_stored))
	def validate(self):
		pos_group=frappe.db.get("POS Groups",{"territory":self.territory})
		self.cash_amount=pos_group.deposit
		if self.cash_amount<self.cash_stored:
			frappe.throw("Nilai kas tidak mencukupi untuk di setorkan")
	pass
