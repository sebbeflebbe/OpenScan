import subprocess
import os

def bandit_logic():
    """
    Function to run Bandit vulnerability scanner on the code in the current working directory.
    """
    print("Running Bandit scanner...")

    # Get the current working directory
    code_path = os.getcwd()

    # Run Bandit command and capture the output
    bandit_cmd = ["bandit", "-r", code_path]
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
