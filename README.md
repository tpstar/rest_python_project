# rest_python_project

To use this app

1. type "pip install -r requirements.txt" in your CLI
2. run "python manage.py runserver" in your CLI
3. copy the server address in the CLI (e.g. http://127.0.0.1:8000/) plus the following request form into the address bar of your browser to see the result:


•	Respond to requests of the form “/hello?firstname={first name}&lastname={last name}&gender={m/f}” and respond with “Hello Mr {First Name} {Last Name}” or “Hello Ms {First Name} {Last Name}” depending on the gender

o	Example: the request “/hello?firstname=tien&lastname=nguyen&gender=m” returns “Hello Mr Tien Nguyen”

•	Respond to requests of the form “/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}” and respond with the result

o	Example: the request “/compute?num1=5&num2=3&operation=subtract” returns “2” (5-3=2)

•	Respond to requests of the form “/date” with the current date in the form “yyyy-mm-dd”

o	Example: “/date” returns “2017-09-20”
