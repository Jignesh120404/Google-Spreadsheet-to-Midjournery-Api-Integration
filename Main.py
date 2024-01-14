import re
import gspread
import time
import pyautogui
x=182  #U can change this according where your discord window is present!
y=0    #Initially it is set on first window of chrome from the left, u can check cursor coordinates from pyautogui.positon()
#pyautogui.click(x, y)
# Authenticate using service account credentials
gc = gspread.service_account(filename='grounded-region-410813-4d1795906ffd.json')

# Open the Google Sheet by name
wks = gc.open("PromptToMidjourney").sheet1

# Get the number of rows in the sheet
num_rows = wks.row_count

# Define the time interval (in seconds) between each iteration
time_interval = 60  # Adjust this value as needed

# Iterate through each row starting from row 1
for row_number in range(1, num_rows + 1):
    # Get the value from the current row and cell A1
    cell_value = wks.cell(row_number, 1).value
    cell_value = re.sub(r'^\s*/imagine\s+prompt:\s*', '', cell_value).strip()
    pyautogui.write("/imagine")
    pyautogui.hotkey("Enter")
    pyautogui.write(cell_value)
    pyautogui.hotkey("Enter")
    #Print the cell value without square brackets and single inverted commas
    #print(cell_value)

    # Pause for the specified time interval
    time.sleep(time_interval)

