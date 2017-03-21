# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bobzz Zone and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class OnTotalPricingRule(Document):
	pass

def calculate_discount(args):
	if isinstance(args, basestring):
		args = json.loads(args)

	args = frappe._dict(args)
	if args.get("discount_amount")==0:
		data = frappe.db.sql("""select 
				priority,applicable_for,customer,customer_group,
				territory,sales_partner,min_value,company,
				price_or_discount,discount,discount_percentage 
				from `tabOn Total Pricing Rule` 
				where (ifnull(valid_from,"")="" or valid_from>="{0}") and (ifnull(valid_upto,"")="" or valid_upto<="{0}") and 
				(customer = "{1}" or customer_group = "{2)" or 
				territory="{3}" or sales_partner="{4}") 
				order by min_value asc,priority asc """.format(args.get("posting_date"),args.get("customer"),args.get("customer_group"),args.get("territory"),args.get("sales_partner")),as_list=1)
		prior=0
		disc=0
		last_policy=0
		found=0
		for rule in data:
			if args.get("grand_total")>= rule[5] and rule[0]>=prior:
				prior=rule[0]
				policy=0
				if rule[1]=="Customer":
					policy=4
				elif rule[1]=="Sales Partner":
					policy=3
				elif rule[1]=="Customer Group":
					policy=2
				elif rule[1]=="Territory":
					policy=1
				if last_policy<policy:
					last_policy=policy
					if rule[7]=="Discount Percentage":
						disc=args.get("grand_total")*rule[9]/100
					else:
						disc=rule[8]
		return disc
					
