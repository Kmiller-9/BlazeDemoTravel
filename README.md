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

2. Create a Virtual Environment (optional)
	First, navigate to your project directory in the terminal or command prompt. Then, run the following command to create a virtual environment named venv:

		python -m venv venv

	This command creates a directory named venv that contains a copy of the Python interpreter and a site-packages directory where your project's dependencies will be installed.

3. Activate the Virtual Environment (optional)
	The method to activate the virtual environment depends on your operating system:

	On Windows:

		venv\Scripts\activate

	On macOS and Linux:

		source venv/bin/activate

   Verify Activation
	Once activated, your terminal prompt should change to indicate that you are now working within the virtual environment. It will typically show the name of the virtual environment in parentheses, like this:

		(venv) $

   Note: if an error related to execution policies is encountered it could  be because the execution of scripts is disabled on your system. Entering the following may fix the issue (Windows)

      Set-ExecutionPolicy Unrestricted -Scope Process

4. Install Dependencies required
	With the virtual environment activated, you can now install your project's dependencies using pip. For example, to install the dependencies listed in your requirements.txt file, run:

		pip install -r requirements.txt

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
