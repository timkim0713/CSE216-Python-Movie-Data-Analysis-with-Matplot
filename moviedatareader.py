from datetime import datetime
import csv

# ----------------------------------------------------------------------

movieItems = []


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    The line is basically a dictionary object.
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        if line["id"] != '':
            mDate = datetime.strptime(line["release_date"], "%m/%d/%Y").date()
            movieItem = {}

            genres = line["genres"]
            movieItem['Genres'] = genres;

            popularity = line["popularity"]
            movieItem['Popularity'] = float(popularity);

            title = line['title']
            movieItem['Movie Title'] = title

            lang = line['original_language']
            movieItem['Movie Language'] = lang    ##lang is string, 2 letters.

            country = line['production_countries']
            movieItem['Production Countries'] = country

            productionCompanies = line["production_companies"]
            movieItem['Production Companies'] = productionCompanies

            revenue = line['revenue']
            movieItem['Revenue'] = int(revenue)

            runTime = line['runtime']
            if (runTime == ""):
                movieItem['Run Time'] = 0
            else:
                movieItem['Run Time'] = int(runTime)

            movieItem['date'] = mDate
            movieItem['record'] = line
            movieItems.append(movieItem)


    print("Total movie items = ", len(movieItems))
    movieItems.sort(key=lambda item: item['date'])
    return movieItems


if __name__ == "__main__":
    with open("movies_metadata_edited.csv", encoding="utf8") as f_obj:
        csv_dict_reader(f_obj)
