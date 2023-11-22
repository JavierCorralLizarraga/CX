import os

def get_latest_excel_filename():
    # Get the current working directory
    cwd = os.getcwd()
    
    # List all files in the current directory
    files = os.listdir(cwd)
    
    # Filter files to include only Excel files
    excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
    
    if not excel_files:
        # No Excel files found
        return None
    
    # Sort Excel files by modification time and get the latest one
    latest_excel_file = max(excel_files, key=lambda file: os.path.getmtime(file))
    
    # Return the full path of the latest Excel file
    return os.path.join(cwd, latest_excel_file)

# Example usage:
excel_filename = get_latest_excel_filename()

if excel_filename:
    print("Latest Excel file:", excel_filename)
else:
    print("No Excel files found in the current directory.")

