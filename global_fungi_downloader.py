# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:32:30 2024

@author: dylan
"""

import os
import csv
import shutil
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# File paths
csv_file = r"C:\Users\dylan\OneDrive\Desktop\PhD\gap_analysis\global_fungi_SHs_rest.csv"
output_folder = r"C:\Users\dylan\OneDrive\Desktop\PhD\gap_analysis\Databases\Global_Fungi\Sequences"

# Configure Chrome options to change the download folder
chrome_options = Options()
prefs = {"download.default_directory": output_folder, "safebrowsing.enabled": "false"}
chrome_options.add_experimental_option("prefs", prefs)

# Set up the WebDriver
service = Service("C:/Users/dylan/OneDrive/Desktop/PhD/gap_analysis/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # Replace with the path to your chromedriver
driver = webdriver.Chrome(service=service)

# Read SH numbers from the CSV file
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    SH_numbers = [row[0] for row in reader]  # Assuming SH numbers are in the first column

# Loop through each SH number
for SH_number in SH_numbers:
    try:
        print(f"Processing SH number: {SH_number}")
        url = f"https://globalfungi.com/?SH={SH_number}"
        driver.get(url)

        # Wait for the page to load
        time.sleep(15)  # Wait 15 seconds for the page to fully load

        # Wait for the iframe to load and switch to it
        wait = WebDriverWait(driver, 30)  # Wait up to 60 seconds for the iframe
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe")))
        driver.switch_to.frame(iframe)

        # Wait for the download button to become clickable
        download_button = wait.until(EC.element_to_be_clickable((By.ID, "id_results-results_variants-downloadFASTA")))

        # Click the download button
        download_button.click()

        # Wait for a few seconds to let the download start
        time.sleep(20)  # Allow more time for the download to begin

        # Rename the downloaded file if it has a "SH_" prefix and move it to the desired folder
        downloaded_filename = f"SH_{SH_number}.zip"  # Assuming files are ZIP and prefixed with "SH_"
        destination_filename = f"{SH_number}.zip"
        downloaded_path = os.path.join(output_folder, downloaded_filename)
        destination_path = os.path.join(output_folder, destination_filename)

        # Check if the downloaded file exists and rename it
        if os.path.exists(downloaded_path):
            os.rename(downloaded_path, destination_path)
            print(f"Renamed and moved file: {destination_filename}")
        else:
            print(f"File not found for SH {SH_number}")

        # Optionally, unzip the file
        with zipfile.ZipFile(destination_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder)
            print(f"Extracted ZIP file for SH {SH_number}")

        # Switch back to the default content after processing each SH number
        driver.switch_to.default_content()

    except Exception as e:
        print(f"Failed to process SH number {SH_number}: {e}")

# Close the browser after completing the downloads
driver.quit()
