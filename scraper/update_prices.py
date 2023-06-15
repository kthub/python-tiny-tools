import os
import re
import csv
from datetime import datetime, timedelta
import yahoo_japan_scraper as scraper

data_dir = '/Users/keiichi/home/gitrepo/jupyter-demo/'
data_file = 'prices.csv'
current_csv = data_dir + data_file
tmp_csv = data_dir + data_file + 'tmp'

if __name__ == "__main__":
  print('start updating prices...')

  # Read from current data file
  with open(current_csv, 'r') as current_file:
    reader = csv.reader(current_file)
    rows = list(reader)

  # Update prices
  lnum = 0
  for row in rows:
    lnum += 1
    if lnum == 1:
      continue
    if row[1] == 'N/A':
      continue
    if len(row) > 3:
      row[3] = scraper.get_price(row[1])

  # Write to temporary file
  with open(tmp_csv, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(rows)

  # Backup
  now = datetime.now()
  formatted_date = now.strftime("%Y%m%d%H%M")
  os.rename(current_csv, current_csv + '.' + formatted_date)

  # Replace current data file with updated file
  os.rename(tmp_csv, current_csv)

  # Housekeep (optional)
  pattern = r'prices.csv.\d+'
  regex = re.compile(pattern)
  bkup_csv_list = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f)) and regex.match(f)]

  for bkup in bkup_csv_list:
    parts = bkup.rsplit(".", 1)
    date_str = parts[-1]
    datetime_object = datetime.strptime(date_str, "%Y%m%d%H%M")

    # Get the datetime for two weeks ago
    two_weeks_ago = datetime.now() - timedelta(weeks=2)

    # Compare the two datetimes
    if datetime_object < two_weeks_ago:
      # remove
      print("removing file (older than 2 weeks) : " + data_dir + bkup)
      os.remove(data_dir + bkup)

  print('done')