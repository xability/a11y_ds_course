# Downloading weather data using Python as a CSV using the Visual Crossing Weather API
# See https://www.visualcrossing.com/resources/blog/how-to-load-historical-weather-data-using-python-without-scraping/ for more information.
import time
import csv
import codecs
import urllib.request
import sys

# This is the core of our weather query URL
BaseURL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/"
location = '"Louisville, KY"'
# Set up the location parameter for our query
QueryLocation = "&location=" + urllib.parse.quote(location)

# Set up the query type parameter for our query ('FORECAST' or 'HISTORY')
QueryType = "HISTORY".upper()

# Set up the key parameter for our query
QueryKey = "&key=" + "ND3B2RTGS72DHDST8FSY5EZT2"

# Writing to a CSV file
with open("total_2023.csv", "w", newline="", encoding="utf-8") as csvfile:

    FromDateParam = "2023-01-01"
    ToDateParam = "2023-12-31"

    print(" - Fetching history for date: ", FromDateParam, "-", ToDateParam)

    # History requests require a date.  We use the same date for start and end since we only want to query a single date in this example
    QueryDate = (
        "&startDateTime="
        + FromDateParam
        + "T00:00:00&endDateTime="
        + ToDateParam
        + "T23:59:59"
    )
    QueryTypeParams = (
        "history?&aggregateHours=24&unitGroup=us&dayStartTime=0:0:00&dayEndTime=0:0:00"
        + QueryDate
    )

    # Build the entire query
    URL = BaseURL + QueryTypeParams + QueryLocation + QueryKey

    print(" - Running query URL: ", URL)

    print()

    # Parse the results as CSV
    CSVBytes = urllib.request.urlopen(URL)
    CSVText = csv.reader(codecs.iterdecode(CSVBytes, "utf-8"))
    csv_writer = csv.writer(csvfile)
    for row in CSVText:
        csv_writer.writerow(row)
