import subprocess

def snyk_logic():
    print("*INFO* To use this service please create an account or login to Snyk. https://docs.snyk.io/getting-started/quickstart/create-a-snyk-account.")
    print("FOLLOW steps on Snyk webpage to setut account and download Snyk CLI through 'npm install -g snyk' to get going *INFO*")
    folder_path = input("Enter the path of the folder to scan: ")
    
    # Run the Snyk CLI command to scan the folder
    command = f"snyk test {folder_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Check the result and print the output
    if result.returncode == 0:
        print("Scan completed successfully.")
    else:
        print("Scan failed.")
    
    # Print the command output
    print(result.stdout)