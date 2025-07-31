// Copyright (c) 2025, Ashish and contributors
// For license information, please see license.txt

frappe.query_reports["Service Booking"] = {
	"filters": [
	     {
			"fieldname": "service_type",
			"label": __("Service Type"),
			"fieldtype": "Select",
			"options": "\nTherapy\nSpa\nOther",			
	    },
	    {
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nRequested\nApproved\nCompleted",
        },
	]
}
