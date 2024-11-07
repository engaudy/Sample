import great_expectations as ge
import yaml

class DataValidator:
    def __init__(self, dataframe, expectations_file):
        self.data_ge = ge.from_pandas(dataframe)
        self.expectations_file = expectations_file

    def load_expectations(self):
        """Load expectations from a YAML file."""
        with open(self.expectations_file, 'r') as file:
            expectations = yaml.safe_load(file).get('expectations', [])
        return expectations

    def run_validations(self):
        """Run validations based on expectations loaded from YAML file."""
        expectations = self.load_expectations()
        all_success = True

        for expectation in expectations:
            expectation_type = expectation['expectation_type']
            kwargs = expectation['kwargs']
            result = getattr(self.data_ge, expectation_type)(**kwargs)
            success = result.success
            message = f"{expectation_type} on {kwargs.get('column')}: {'Passed' if success else 'Failed'}"
            print(message)
            all_success = all_success and success

        if all_success:
            print("All validations passed.")
        else:
            print("Some validations failed.")
