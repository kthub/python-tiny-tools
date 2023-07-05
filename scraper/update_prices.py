import os, re, csv, threading
from datetime import datetime, timedelta
import yahoo_japan_scraper as scraper

# !! CHANGE HERE !!
data_dir = '/DATA_DIRECTORY/'
data_file = 'prices.csv'

current_csv = data_dir + data_file
tmp_csv = data_dir + data_file + 'tmp'
print_lock = threading.Lock()
housekeep = True

##
## Update row
##
def update_row(row):
  if len(row) > 3:
    original = int(row[3])
    updated = scraper.get_price(row[1])
    row[3] = updated

    # change rate
    cr = round((updated - original)/original, 4) * 100
    formatted_rate = f"{'+' if cr > 0 else ''}{cr:.2f}"

    # print result
    with print_lock:
      print('price for ' + row[0] + ' is updated from ' +
            str(original) + ' to ' + str(updated) +
            ' (' + formatted_rate + '%)')

##
## Main
##
if __name__ == "__main__":
  print('start updating prices...')

  # Read from current data file
  with open(current_csv, 'r') as current_file:
    reader = csv.reader(current_file)
    rows = list(reader)

  # Update prices
  lnum = 0
  threads = []
  for row in rows:
    lnum += 1
    if lnum == 1:
      continue
    if row[1] == 'N/A':
      continue
    else:
      thread = threading.Thread(target=update_row, args=(row,))
      thread.start()
      threads.append(thread)
  for thread in threads:
    thread.join()

  # Write to temporary file
  with open(tmp_csv, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(rows)

  # Backup current data file
  formatted_date = datetime.now().strftime("%Y%m%d%H%M")
  os.rename(current_csv, current_csv + '.' + formatted_date)

  # Replace current data file with updated file
  os.rename(tmp_csv, current_csv)

  # Housekeep
  if (housekeep):
    regex = re.compile(r'prices.csv.\d+')
    bkup_csv_list = [f for f in os.listdir(data_dir) if regex.match(f)]

    for bkup in bkup_csv_list:
      parts = bkup.rsplit(".", 1)
      date_str = parts[-1]
      datetime_object = datetime.strptime(date_str, "%Y%m%d%H%M")

      remove_criteria = datetime.now() - timedelta(weeks=1)
      if datetime_object < remove_criteria:
        #print("remove file (older than 1 weeks) : " + data_dir + bkup)
        os.remove(data_dir + bkup)

  print('done')