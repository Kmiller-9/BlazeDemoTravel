## Setup Instructions

# TravelTheWorld

## Project Overview
This project is a web automation script for the BlazeDemo website using Selenium.

## Prerequisites

- Python 3.13 or higher
- `pip` (Python package installer)
- Google Chrome browser
- ChromeDriver

## Setup Instructions

### Install Required Python Packages

1. Clone the repository

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 
## Install the required packages:
   pip install selenium webdriver-manager
 ```sh
    pip install -r requirements.txt
    ```

    Ensure that [requirements.txt](http://_vscodecontentref_/3) contains the following packages:

    ```
   selenium
   webdriver-manager
   pytest
   parameterized
    
## Running the Tests

You can run the tests using the `main.py` script located in the `src` directory. The script provides options to run specific test cases, all tests in a subfolder, or all tests in the project.

### Running All Tests in a Subfolder

To run all tests in a specific subfolder, use the `subfolder` parameter at the bottom of the main method:
the code looks like this:
   # Run all tests in a specific subfolder
    # run_tests(subfolder='flight_selector', append=False)  # Overwrite the report file
    # run_tests(subfolder='links', append=True)  # Append to the report file
    # run_tests(subfolder='end_to_end', append=True)  # Append to the report file
    # run_tests(subfolder='other', append=True)  # Append to the report file

```sh

## Notes
The webdriver-manager package is used to automatically download and manage the chromedriver executable, so you don't need to manually download or include it in your repository.
Ensure that your Chrome browser is up to date to avoid compatibility issues with chromedriver."# BlazeDemoTravel" 
