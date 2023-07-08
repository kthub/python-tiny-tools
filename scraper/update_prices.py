"""
File: update_prices.py
Author: Keiichi Tsuda
Email: keiichi.tsuda@gmail.com
Github: github.com/kthub
Description: This script updates prices.csv
"""
import os, re, csv, threading
from datetime import datetime, timedelta
import yahoo_japan_scraper as scraper

DATA_DIR = '/Users/keiichi/home/gitrepo/jupyter-demo/data/'
DATA_FILE = 'prices.csv'
CSV_IDX_ASSET_NAME = 0
CSV_IDX_CODE = 1
CSV_IDX_CURRENT_PRICE = 3
NA = 'N/A'
TMP_SUFFIX = 'tmp'
DATE_FORMAT = "%Y%m%d%H%M"

current_csv = os.path.join(DATA_DIR, DATA_FILE)
tmp_csv = os.path.join(DATA_DIR, DATA_FILE + TMP_SUFFIX)
print_lock = threading.Lock()
housekeep = True

##
## Update row
##
def update_row(row):
  # Check if the row has at least 4 elements
  if len(row) > 3:
    original = int(row[CSV_IDX_CURRENT_PRICE])
    try:
      updated = scraper.get_price(row[CSV_IDX_CODE])
    except Exception as e:
      with print_lock:
        print(f"Error updating price for {row[CSV_IDX_ASSET_NAME]}: {e}")
      return
    row[CSV_IDX_CURRENT_PRICE] = updated

    # calculate change rate
    cr = round((updated - original)/original, 4) * 100
    formatted_rate = f"{'+' if cr > 0 else ''}{cr:.2f}"

    # print result
    with print_lock:
      print(f'price for {row[CSV_IDX_ASSET_NAME]} is updated from {original} to {updated} ({formatted_rate}%)')

##
## Main
##
if __name__ == "__main__":
  # Read from the current data file
  with open(current_csv, 'r') as current_file:
    reader = csv.reader(current_file)
    rows = list(reader)

  # Update prices (multi-threading)
  threads = []
  for index, row in enumerate(rows):
    if index == 0 or row[CSV_IDX_CODE] == NA:
      continue
    thread = threading.Thread(target=update_row, args=(row,))
    thread.start()
    threads.append(thread)
  for thread in threads:
    thread.join()

  # Write to the temporary file
  with open(tmp_csv, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(rows)

  # Backup current data file
  formatted_date = datetime.now().strftime(DATE_FORMAT)
  os.rename(current_csv, current_csv + '.' + formatted_date)

  # Replace the current data file with the updated one
  os.rename(tmp_csv, current_csv)

  # Housekeep
  if (housekeep):
    regex = re.compile(f'{DATA_FILE}\.\d+')
    bkup_csv_list = [f for f in os.listdir(DATA_DIR) if regex.match(f)]

    # Use list comprehension to filter the list of backup files
    removable_bkup_csv_list = [
        bkup for bkup in bkup_csv_list
        if datetime.strptime(bkup.rsplit(".", 1)[-1], DATE_FORMAT) < datetime.now() - timedelta(weeks=1)
    ]

    # Remove the old backup files
    for bkup in removable_bkup_csv_list:
        print(f'remove file (older than 1 weeks) : {DATA_DIR}{bkup}')
        os.remove(os.path.join(DATA_DIR, bkup))