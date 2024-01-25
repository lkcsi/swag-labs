# Swag Labs Tests
This project is intended to test the following website: https://www.saucedemo.com

## Note
> With every user provided in main page, the application behaves differently, just like they were different environments 
or versions, so I treated them as different environments. The only exception is locked_out_user it behaves like a user.

> Although I've treated users as different environments, there are tests (login tests and logout tests) where it makes sense 
to use them as actual users.

## Prerequisites
- Python (3.10 or above) and pip installed
- Create a .env file in project root folder with **PASSWORD** field, password value can be found here: https://www.saucedemo.com
- For Chrome include the ChromeDriver location in your PATH environment variable
- For Firefox include Geckodriver location in your PATH environment variable

## Setup
- pip install -r requirements.txt

## Run tests
- Should be in project root folder 
- Use **pytest** to run tests
- Examples:
```
pytest --env=problem --browser=firefox
pytest --env=visual --html=reports/visual.html
pytest -k "logout_test" --browser=chrome
```

## CLI options
- **--browser** for choose browser, available options are: chrome | firefox
- **--env** for choose tested environment, available options are: standard | visual | error | problem | perf
- **--html** for choose report name, please use **reports/<report_name>** format, to make sure it is placed to reports folder, otherwise screenshots won't work

## Config
- Use config.ini file to configure different environments
- **CorrectEnvBaseUrl** and **CorrectEnvUsername** is used for visual regression tests, where they used as a correct environment which can be used to compare the tested environment to
- **BaseUrl** and **Username** are to choose the tested environment
- **WaitTime** is the threshold in seconds, within web elements should be presented

## Pytest config file
Contains common cli options to fine tune pytest behavior

## Environment file
**.env** file stores login password. **PASSWORD**=password, password value can be found here: https://www.saucedemo.com

## Report
Reports can be found in ./reports folder, the provided screenshots are relative to this path, so relocating reports will 
screw up screenshot 

## Todo
- [ ] reports should be self-contained
- [ ] cleanup screenshot folder
- [ ] try selenium page factory