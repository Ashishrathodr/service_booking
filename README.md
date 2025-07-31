### Service Booking

Service Booking

### Installation

### Local

To setup the repository locally follow the steps mentioned below:

1. Setup bench by following the [Installation Steps](https://frappeframework.com/docs/user/en/installation) and start the server

```
bench start
```

2. In a separate terminal window, cd into `frappe-bench` directory and run the following commands:

```
# get app
$ bench get-app https://github.com/Ashishrathodr/service_booking.git

# install on site
$ bench --site sitename install-app service_booking
$ bench --site sitename migrate

```
🖥 System Info
```
•	OS: Ubuntu 22.04
•	Python: 3.10
•	Frappe: 15.69.2
•	ERPNext: 15.63.0
•	Tools: VS Code
```

📘 Features
```
•	Doctype: Service Booking
•	Server Script: Sends confirmation email on approval
•	Print Format: Jinja-based confirmation receipt
•	Report: Filtered view of service booking
•	Webhook integration
```

### License

mit
