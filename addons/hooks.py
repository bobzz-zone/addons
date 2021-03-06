# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "addons"
app_title = "Addons"
app_publisher = "Bobzz Zone"
app_description = "App for Trimatari"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------
fixtures = ["Custom Field","Custom Script","Print Format"]

# include js, css files in header of desk.html
# app_include_css = "/assets/addons/css/addons.css"
# app_include_js = "/assets/addons/js/addons.js"

# include js, css files in header of web template
# web_include_css = "/assets/addons/css/addons.css"
# web_include_js = "/assets/addons/js/addons.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "addons.install.before_install"
# after_install = "addons.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "addons.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
#	"POS Shift Daily Reports" : {
#		"on_validate":"addons.addons.doctype.pos_shift_daily_reports.pos_shift_daily_reports.on_validate_data"
#	}
#	"Sales Invoice": {
#		"on_update": "addons.addons.doctype.on_total_pricing_rule.on_total_pricing_rule.calculate_discount"
#	}
#        "Sales Order": {
#		"on_update": "addons.addons.doctype.on_total_pricing_rule.on_total_pricing_rule.calculate_discount"
#	},
#        "Delivery Note": {
#		"on_update": "addons.addons.doctype.on_total_pricing_rule.on_total_pricing_rule.calculate_discount"
#	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"addons.tasks.all"
# 	],
# 	"daily": [
# 		"addons.tasks.daily"
# 	],
# 	"hourly": [
# 		"addons.tasks.hourly"
# 	],
# 	"weekly": [
# 		"addons.tasks.weekly"
# 	]
# 	"monthly": [
# 		"addons.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "addons.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "addons.event.get_events"
# }

