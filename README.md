# Swag Labs Tests
This project is intended to test the following website: https://www.saucedemo.com
## Prerequisites
- Python and pip installed
- For Chrome include the ChromeDriver location in your PATH environment variable
- For Firefox include Geckodriver location in your PATH envrionment variable
## Setup
- pip install -r requirements.txt
## Run tests
- See pytest.ini to customize test configuration
## CLI options
- **--browser** for choose browser, available options are: chrome | firefox
- **--env** for choose tested environment, available options are: standard | visual | error | problem | perf | timeout