import unittest
import io
import sys
import os

# Custom test result class to capture test outputs
class CustomTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_outputs = []  # List to store test results

    # Override addSuccess to capture successful test results
    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_outputs.append((test, "SUCCESS"))

    # Override addFailure to capture failed test results
    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_outputs.append((test, "FAILURE", self._exc_info_to_string(err, test)))

    # Override addError to capture test errors
    def addError(self, test, err):
        super().addError(test, err)
        self.test_outputs.append((test, "ERROR", self._exc_info_to_string(err, test)))

    # Custom method to write test status
    def _write_status(self, test, status):
        self.stream.write(status + '\n')

# Function to run tests and generate a report
def run_tests(test_names=None, subfolder=None, append=False):
    """
    Run specified test cases from the tests folder and generate a text report.
    
    :param test_names: List of test case names to run. If None, all tests are run.
    :param subfolder: Subfolder within the tests folder to run tests from. If None, all tests are run.
    :param append: Whether to append to the report file or overwrite it.
    """
    # Adjust the Python path to include the parent directory
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, parent_dir)
    print(f"Python path: {sys.path}")  # Debug print

    loader = unittest.TestLoader()
    if test_names:
        # Load specified test cases
        tests = loader.loadTestsFromNames(test_names)
    elif subfolder:
        # Construct the correct path to the subfolder within the tests directory
        subfolder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', subfolder))
        print(f"Discovering tests in subfolder: {subfolder_path}")
        # Check if the subfolder path is a directory and contains an __init__.py file
        if os.path.isdir(subfolder_path):
            print(f"{subfolder_path} is a directory.")
            if os.path.isfile(os.path.join(subfolder_path, '__init__.py')):
                print(f"{subfolder_path} contains an __init__.py file.")
            else:
                print(f"{subfolder_path} does not contain an __init__.py file.")
        else:
            print(f"{subfolder_path} is not a directory.")
        tests = loader.discover(start_dir=subfolder_path, pattern='test*.py')
        print(f"Number of tests discovered: {tests.countTestCases()}")
    else:
        # Load all tests from the tests folder
        tests = loader.discover(start_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests')), pattern='test*.py')
    
    # Create a custom result object to store the output
    result = CustomTestResult(stream=sys.stdout, descriptions=True, verbosity=2)
    # Run the test cases
    tests.run(result)
    
    # Collect the output from each test case
    output = ""
    for test, status, *details in result.test_outputs:
        output += f"{test}: {status}\n"
        if details:
            output += f"Details: {details[0]}\n"
    
    # Define the report file path
    report_file_path = 'test_report.txt'
    
    # Write the collected output to a report
    mode = 'a' if append else 'w'
    with open(report_file_path, mode) as f:
        f.write(output)
    
    # Print the report file path
    print(f"Test report generated at: {os.path.abspath(report_file_path)}")
    
    # Print summary of test results
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")

if __name__ == '__main__':
    # Example usage:
    # Run specific test cases
    test_cases_to_run = [
        'tests.other.test_purchase_info.PurchaseInfo.test_form_submission',
        'tests.other.test_multi_selector.MultiFlightSelect.test_form_submission',
    ]
    # run_tests(test_names=test_cases_to_run)

    # Run all tests in a specific subfolder
    run_tests(subfolder='flight_selector', append=False)  # Overwrite the report file
    # run_tests(subfolder='links', append=True)  # Append to the report file
    # run_tests(subfolder='end_to_end', append=True)  # Append to the report file
    # run_tests(subfolder='other', append=True)  # Append to the report file