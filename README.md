# reverse engineering erp.rajalakshmi.org

## partially got login to work with python requests and sessions

without starting a browser or headless browser got login to work using python requests

## hurdles

they are using asp.net and they are using `__VIEWSTATE` and some other mumbo jumbo in the cookies
can't understand how they are validating the user but for now able to login to a user id using the user provided login credentials

## HOW TO RUN

`requirements`

- ~~pytesseract~~
- ~~opencv~~
- requests

change the `USER` and `PASS` in the **main.py** to your erp.rajalakshmi.org login
`python3 main.py`
for now we can login into a user session and get data. When they add more features I will
try to implement them and let's see if i have enough time on my hand to port them over to
comp.devsrec.club
