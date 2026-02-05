from win32com.client import Dispatch
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess
import re
import zipfile
import shutil
import os
import json
from pathlib import Path


def extract_config_path():
    global currentpath
    currentpath = os.getcwd()
    currentpath = currentpath.replace('\\','/')
    currentpath = currentpath.replace('/scripts','')
    confpath = currentpath + '/paths.json'
    print(confpath)

    with open(confpath) as fjson:
        path_data = json.load(fjson)

    print(path_data)

    global Local_driver_path
    global zip_file_path
    global extraction_path
    global Archieve_path
    global Archieve_path_rename

    Local_driver_path=path_data['Local_driver_path']
    zip_file_path = path_data['zip_file_path']
    extraction_path = path_data['Extraction_path']
    Archieve_path = path_data['Archieve_path']
    Archieve_path_rename = path_data['Archieve_path_rename']

#==================================================================================================================
def rename_file(old_name, new_name):
    try:
        old_path = Path(old_name)
        new_path = old_path.with_name(new_name)
        old_path.rename(new_path)
        print(f"File renamed successfully from {old_name} to {new_name}")
    except FileNotFoundError:
        print(f"Error: The file {old_name} does not exist.")
    except Exception as e:
        print(f"Error: {e}")


#Extracting config path
extract_config_path()
#PC chromedriver version
def get_exe_version(file_path):
    try:
        output = subprocess.check_output([file_path, '--version'], universal_newlines=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Replace with the actual path to the EXE file
exe_path = Local_driver_path

version = get_exe_version(exe_path)
string_regex = version
pattern =r'(\d+)'
match = re.search(pattern, string_regex)
version_number = match.group(1)
print(version_number)
#=================================================================================================================

#Latest version of chromedriver available 
online_version =""
#temp  = "119.0.6045.105"

driver = webdriver.Chrome()
driver.get('https://googlechromelabs.github.io/chrome-for-testing/#stable')
target_element = driver.find_element(By.XPATH,'/html/body/section[1]/p/code[1]')
if target_element:
   target_element_value = target_element.text
   match_online = re.search(pattern, target_element_value)
   online_version = match_online.group(1)
   print(online_version)
   pattern_2=r'(\d+.\d+.\d+.\d+)'
   match_url = re.search(pattern_2,target_element_value)
   url_version = match_url.group(1)
   print(url_version)
else :
   print("No element on website")
driver.quit()
#==================================================================================================================

if online_version==version_number:
    print("same version")
else:
    print("Need changes")

    #==================================================================================================================
    #Moving to archieve
    #os.rename("chromedriver.exe", "chromedriver_"+version_number+".exe")
    shutil.move(Local_driver_path,Archieve_path)
    old_file_name = Archieve_path
    name = "chromedriver_"+version_number+".exe"
    new_file_name=name
    rename_file(old_file_name, new_file_name)
    


    #==================================================================================================================
    #Downloading zip file
    creating_url = 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/'+url_version +'/win64/chromedriver-win64.zip'
    print(creating_url)
    response = requests.get(creating_url)
    file_name = "chromedriver-win64.zip"
    with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f'File downloaded as {file_name}')


    #==================================================================================================================
    #Extracting zip file
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)
        print(f'Zip file extracted to {extraction_path}')
    except zipfile.BadZipFile as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

    
    shutil.move(extraction_path+"/chromedriver-win64/chromedriver.exe",Local_driver_path)
    #==================================================================================================================
   

