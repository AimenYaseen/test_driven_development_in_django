# Test Driven Development in Django
This project will contain functional tests and unit tests. Its main focus will be unit tests. I will practice 'how to write unit tests and then write functions to pass that tests'.

## Steps to follow:
- clone the repository
- create a virtual environment
- install requirements using command 'pip install -r requirements.txt'
- To run functional tests, you need selenium. To run selenium, you need a web driver. It can be geckodriver(firefox) or chromedriver(google chrome).
- Download them using these links
- geckodriver - https://github.com/mozilla/geckodriver/releases
- chromedriver - https://chromedriver.chromium.org/downloads
- use the latest or the one that matches your browser versions.
- extract and then move the executable file to your projects virtual environments bin directory.
- follow this tutorial to set up in ubuntu 'https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/'
- move to the project folder
- run server 'python manage.py runserver:8000'
- run this command 'python manage.py test' to run all the tests in this project.