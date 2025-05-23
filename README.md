**ChromeDriver Auto-Update Script**
**Overview**
This script automates the process of checking, downloading, and updating the ChromeDriver executable to match the latest version of Google Chrome's stable release. It does so by performing several operations, including extracting paths from a configuration file, checking the current ChromeDriver version, comparing it with the latest version available online, and updating the executable if necessary.

**Functionality**
1. Configuration Path Extraction
The script begins by extracting paths from a JSON configuration file (paths.json). This file should contain paths relevant to the operation, such as:
Local_driver_path: Path where the current ChromeDriver is located.
zip_file_path: Path where the downloaded zip file will be saved.
extraction_path: Path where the contents of the zip file will be extracted.
Archieve_path: Path where the old ChromeDriver executable will be archived.
Archieve_path_rename: Path for renaming the archived ChromeDriver.

2. Current ChromeDriver Version Check
It uses a subprocess call to check the version of the local ChromeDriver executable.

3. Online Version Check
The script uses Selenium to scrape the latest stable version of ChromeDriver available online from the Google Chrome Labs website.

4. Version Comparison
It compares the local ChromeDriver version with the online version.
If the versions match, no action is taken.
If the versions differ, the script proceeds to update the ChromeDriver.

5. Archiving Current ChromeDriver
 The current ChromeDriver is moved to an archive location and renamed for record-keeping.

6. Downloading and Extracting Latest ChromeDriver
The script constructs a URL to download the latest ChromeDriver zip file.
It downloads and extracts the zip file to the specified location.

7. Updating ChromeDriver
After extraction, the new ChromeDriver executable is moved to the local path specified in the configuration file, replacing the old version.

**Requirements**
Python 3.x
Libraries:
win32com.client
requests
selenium
subprocess
re
zipfile
shutil
os
json
pathlib

The paths.json configuration file with the necessary paths.


**Usage**
Ensure all dependencies are installed.
Set up the paths.json file with the appropriate paths.
Run the script to automatically update the ChromeDriver if a newer version is available online.

**Notes**
Be sure to have Chrome installed and updated on your system to ensure compatibility.
This script assumes Windows as the operating system. Paths and operations might need adjustments for other systems.
Ensure that the paths.json file is correctly formatted and located in the expected directory.
