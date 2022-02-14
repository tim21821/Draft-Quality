from basketball_reference_scraper.drafts import get_draft_class
from threading import Thread
import os


def save_draft_class(year):
    data = get_draft_class(year)
    data.to_csv(os.path.join("data", f"draft_{year}.csv"))


if __name__ == "__main__":
    for year in range(1950, 2022):
        t = Thread(target=save_draft_class, args=(year,))
        t.start()
