import subprocess
import os

def bandit_logic():
    """
    Function to run Bandit vulnerability scanner on the code in the current working directory.
    """
    print("Running Bandit scanner...")

    # Get the current working directory
    code_path = os.getcwd()

    # Build the configuration file path based on the current working directory
    config_file = os.path.join(code_path, "bandit.yaml")

    # Check if the configuration file exists
    if not os.path.exists(config_file):
        print("Configuration file 'bandit.yaml' not found in the current directory.")
        return

    # Run Bandit command with the specified configuration file and capture the output
    bandit_cmd = ["bandit", "-r", code_path, "-c", config_file]
    result = subprocess.run(bandit_cmd, capture_output=True, text=True)

    # Check the return code to determine if the scan was successful
    if result.returncode == 0:
        # Print the scan results
        print(result.stdout)
        print("Bandit scan completed successfully.")
    else:
        # Print any error messages
        print(result.stderr)
        print("Bandit scan encountered an error.")

if __name__ == "__main__":
    bandit_logic()
