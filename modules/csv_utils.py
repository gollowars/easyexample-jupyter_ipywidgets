"""This module contains classes and functions to handle csv files."""
import datetime
import csv

class SocialRow:
    """This class represents a row in the csv file."""

    def __init__(self, created_date: datetime.date, twitter: int, instagram: int, tiktok: int, comment: str) -> None:
        self.created_date = created_date
        self.twitter = twitter
        self.instagram = instagram
        self.tiktok = tiktok
        self.comment = comment

    def to_dict(self) -> dict:
        """This method returns a dict of the row."""
        return {
            'Created Date': self.created_date,
            'Twitter': self.twitter,
            'Instagram': self.instagram,
            'TikTok': self.tiktok,
            'Comment': self.comment

        }

    @classmethod
    def get_header(cls) -> list:
        return ['Created Date', 'Twitter', 'Instagram', 'TikTok', 'Comment']


class CsvHandler:
    """This class handles the csv file."""

    def __init__(self, file_path: str, header: list) -> None:
        self.file_path = file_path
        self.header = header

        self._add_header_if_not_exist()

    def _add_header_if_not_exist(self) -> None:
        with open(self.file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.header)
            if csvfile.tell() == 0:
                writer.writeheader()

    # check if the row is valid related header
    def _check_row(self, row: dict) -> bool:
        return set(row.keys()) == set(self.header)

    # add row to csv file

    def add_row(self, row: dict) -> None:
        """This method adds a row to the csv file."""
        if self._check_row(row):
            with open(self.file_path, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.header)
                writer.writerow(row)

    def read(self) -> list:
        """ This method reads the csv file and returns a list of rows."""
        data = []
        with open(self.file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        return data

    def get_header(self) -> list:
        """This method returns the header of the csv file."""
        return self.header
