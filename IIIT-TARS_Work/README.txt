In order to run IIIT-TARS_Drive_Scraper.py do the following:

1. Navigate to the directory that you wish to download the google drive folder into and place IIIT-TARS_Drive_Scraper.py there.
2. Open a terminal at the directory location.
3. Run pip install -r requirements.txt
4. Ensure the URL provided in the code is correct, and the name of the folder is correct. 
5. Run python IIIT-TARS_Drive_Scraper.py
6. The code will download the files, however please note that it may fail if you have already downloaded them very recently. You can always download them manually if it doesn't work. If the folder is already downloaded in the same directory, it will not attempt to redownload it.
7. The program will then sort the files based on their file name format. This should leave only unformatted files unsorted.