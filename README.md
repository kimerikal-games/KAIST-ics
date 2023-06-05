KAIST Academic iCalendar
========================

The purpose of this repository is two-fold:

1. To provide an iCalendar file for KAIST academic calendar.
2. To demonstrate how to use Python to scrape a website and convert the data to iCalendar format.

Add calendar to your application
--------------------------------

The iCalendar files, suitable for import into most calendar applications, are
available in the [generated](generated) directory of this repository.

Most calendar applications support loading .ics files via URL.

1. Enter [generated](generated) directory.
2. Choose the year you want to import.
3. Right-click the "Raw" button and select "Copy link".
4. Paste the copied link into your calendar application.

Alternatively, you can download the .ics file. After choosing the .ics file,

* Click on the "Download" button. Or,
* Right-click the "Raw" button and select "Save link as".

Generate the iCalendar file
---------------------------

The script included in this repository is designed to download the academic
calendar from official KAIST website and convert it into the iCalendar format.

1. Install the required python packages.
    ```
    $ pip install -r requirements.txt
    ```
2. Run the script. The .ics file will be generated in the current directory.
    ```
    $ python script.py -y 2023
    ```

License
-------

The Unlicense. See LICENSE.txt for full text.

References
----------

- https://kaist.ac.kr/kr/html/edu/03110101.html
