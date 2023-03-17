import concurrent.futures
from datetime import date

import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event


def main(year, outfilename):
    all_calendar = download_yearly_calendar(year)
    cal = make_ical(year, all_calendar)

    with open(outfilename, "wb") as f:
        f.write(cal.to_ical())


def download_yearly_calendar(year):
    all_calendar = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for calendar in executor.map(download_monthly_calendar, [year] * 12, range(1, 13)):
            all_calendar.extend(calendar)
    return all_calendar


def download_monthly_calendar(year, months):
    calendar = []

    url = "https://kaist.ac.kr/kr/html/edu/03110101.html"
    data = {"groups": "university", "year": f"{year}", "month": f"{months:02d}"}

    with requests.post(url, data=data) as res:
        res.raise_for_status()
        html = res.text
    soup = BeautifulSoup(html, "html.parser")

    for row in soup.select(".schedule_table tr"):
        dates, title = row.select("td")
        dates = dates.text.strip()
        title = title.text.strip()
        calendar.append((dates, title))

    return calendar


def parse_date(year, string):
    month = int(string[0:2])
    day = int(string[3:5])
    return date(year, month, day)


def make_ical(year, all_calendar):
    cal = Calendar()
    cal.add("prodid", f"-//KAIST {year} Academic Calendar//codeberg.org/kimerikal/KAIST-ics//")
    cal.add("version", "2.0")

    for dates, title in all_calendar:
        if "~" in dates:
            start_date, end_date = dates.split("~")
            start_date = parse_date(year, start_date.strip())
            end_date = parse_date(year, end_date.strip())
        else:
            start_date = end_date = parse_date(year, dates.strip())

        e = Event()
        e.add("summary", title)
        e.add("dtstart", start_date)
        e.add("dtend", end_date)
        cal.add_component(e)
    return cal


if __name__ == "__main__":
    import argparse
    import datetime

    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=int, default=datetime.date.today().year)
    parser.add_argument("-o", "--outfilename", type=str)
    args = parser.parse_args()

    if args.outfilename is None:
        args.outfilename = f"kaist-calendar-{args.year}.ics"

    main(args.year, args.outfilename)
