"""
File: update_prices_async.py
Author: Keiichi Tsuda
Email: keiichi.tsuda@gmail.com
Github: github.com/kthub
Description: This script updates prices.csv
"""
import os, re, csv
from datetime import datetime, timedelta
import yahoo_japan_scraper_async as scraper
import asyncio, nest_asyncio
nest_asyncio.apply()

DATA_DIR = '/Users/keiichi/home/gitrepo/jupyter-demo/data/'
DATA_FILE = 'prices.csv'
CSV_IDX_ASSET_NAME = 0
CSV_IDX_CODE = 1
CSV_IDX_CURRENT_PRICE = 3
CSV_IDX_CURRENT_DATE = 4
CSV_IDX_PREVIOUS_PRICE = 5
CSV_IDX_PREVIOUS_DATE = 6
NA = 'N/A'
TMP_SUFFIX = 'tmp'
DATE_FORMAT = "%Y%m%d%H%M"

current_csv = os.path.join(DATA_DIR, DATA_FILE)
tmp_csv = os.path.join(DATA_DIR, DATA_FILE + TMP_SUFFIX)
housekeep = True

##
## Update row
##
async def update_row(row):
  # Check if the row has at least 7 elements
  if len(row) > 6:
    original = (int(row[CSV_IDX_CURRENT_PRICE]), row[CSV_IDX_CURRENT_DATE])
    try:
      updated = await scraper.get_price(row[CSV_IDX_CODE])
    except Exception as e:
      print(f"Error updating price for {row[CSV_IDX_ASSET_NAME]}: {e}")
      return
    
    # overwrite previous data
    if (original[1] != updated[1]):
      row[CSV_IDX_PREVIOUS_PRICE] = original[0]
      row[CSV_IDX_PREVIOUS_DATE] = original[1]

    # update current data
    row[CSV_IDX_CURRENT_PRICE] = updated[0]
    row[CSV_IDX_CURRENT_DATE] = updated[1]

    # calculate change rate
    #cr = round((updated - original)/original, 4) * 100
    #formatted_rate = f"{'+' if cr > 0 else ''}{cr:.2f}"

    # print result
    #print(f'price for {row[CSV_IDX_ASSET_NAME]} is updated from {original} to {updated} ({formatted_rate}%)')

##
## Main
##
async def main():
  # Read from the current data file
  with open(current_csv, 'r') as current_file:
    reader = csv.reader(current_file)
    rows = list(reader)

  # Update prices (async)
  tasks = []
  for index, row in enumerate(rows):
    if index == 0 or row[CSV_IDX_CODE] == NA:
      continue
    task = asyncio.create_task(update_row(row))
    tasks.append(task)
  await asyncio.gather(*tasks)

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
    regex = re.compile(DATA_FILE + '.¥d+')
    bkup_csv_list = [f for f in os.listdir(DATA_DIR) if regex.match(f)]

    # Use list comprehension to filter the list of backup files
    removable_bkup_csv_list = [
        bkup for bkup in bkup_csv_list
        if datetime.strptime(bkup.rsplit(".", 1)[-1], DATE_FORMAT) < datetime.now() - timedelta(weeks=1)
    ]

    # Remove the old backup files
    for bkup in removable_bkup_csv_list:
        #print(f'remove file (older than 1 weeks) : {DATA_DIR}{bkup}')
        os.remove(os.path.join(DATA_DIR, bkup))


if __name__ == "__main__":
  asyncio.run(main())
