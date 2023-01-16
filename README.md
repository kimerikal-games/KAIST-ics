KAIST Academic iCalendar
========================

This script downloads the academic calendar of KAIST and converts it to iCalendar format.
The iCalendar file can be imported to Google Calendar, Outlook, etc.

Usage
-----

1. Install the required packages.
    ```
    $ pip install -r requirements.txt
    ```
2. Run the script. The ics file will be generated in the current directory.
    ```
    $ python script.py -y 2023
    ```
3. Import the generated iCalendar file to your calendar application.
    - Google Calendar: https://support.google.com/calendar/answer/37118
    - Outlook: https://support.microsoft.com/en-us/office/import-or-subscribe-to-a-calendar-in-outlook-com-cff1429c-5af6-41ec-a5b4-74f2c278e98c

License
-------

The Unlicense. See LICENSE.txt for full text.

References
----------

- https://kaist.ac.kr/kr/html/edu/03110101.html
