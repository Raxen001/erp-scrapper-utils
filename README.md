# reverse engineering erp.rajalakshmi.org

## partially got login to work with python requests and sessions

without starting a browser or headless browser got login to work using python requests

## hurdles

they are using asp.net and they are using `__VIEWSTATE` and some other mumbo jumbo in the cookies
can't understand how they are validating the user but for now able to login to a user id using the user provided login credentials

