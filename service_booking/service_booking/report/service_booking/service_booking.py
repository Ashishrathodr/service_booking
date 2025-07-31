# Copyright (c) 2025, Ashish and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):    
	columns=get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
    columns = [
        {
            "label": ("Customer Name"),
            "fieldname": "customer_name",
            "fieldtype": "Data",
            "width":180
        },
        {
            "label": ("Service Type"),
            "fieldname": "service_type",
            "fieldtype": "Data",
            "width":80
        },        
        {
            "label": ("Preferred Date"),
            "fieldname": "preferred_date",
            "fieldtype": "Datetime",
            "width":200
        },             
        {
            "label": ("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width":120
        },                        
	]
    return columns

def get_data(filters):
	data=[]    
	filters_data = []
	if filters.get("service_type"):
		filters_data.append(["service_type", "=", filters.get("service_type")])
	if filters.get("status"):
		filters_data.append(["status", "=", filters.get("status")])  
  
	booking_data = frappe.get_all(
		"Service Booking",
		filters=filters_data,		
		fields=["customer_name", "service_type", "preferred_date", "status"],
		order_by="name",
	)  
 
	if not booking_data:
		return data
	else:
		return booking_data