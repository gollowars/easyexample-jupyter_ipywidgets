"""This module contains the widgets and the logic to interact with the widgets"""""
import datetime
import ipywidgets as widgets
from IPython.display import display, clear_output
import pandas as pd

from modules.csv_utils import SocialRow, CsvHandler


class WidgetManager:
    def __init__(self, csv_handler: CsvHandler) -> None:
        self.csv_handler = csv_handler
        self._create_widgets()
        self._update_csv_data()

    def _create_widgets(self) -> None:
        self.twitter = widgets.IntText(description='twitter : ')
        self.instagram = widgets.IntText(description='instagram : ')
        self.tiktok = widgets.IntText(description='tiktok : ')
        # get the date value of the widgets
        self.datePicker = widgets.DatePicker()
        self.datePicker.value = datetime.date.today()

        self.comment_area = widgets.Textarea(description='comment : ')
        self.button = widgets.Button(description="Write CSV")
        self.output = widgets.Output(layout={'border': '1px solid black'})

        self.my_widgets = widgets.VBox(
            [self.datePicker, self.twitter, self.instagram, self.tiktok, self.comment_area, self.button, self.output])

        self.button.on_click(self._add_new_row)

    def _update_csv_data(self) -> pd.DataFrame:
        data = self.csv_handler.read()
        headers = self.csv_handler.get_header()
        self.pd_df = pd.DataFrame(data[1:], columns=headers)

    def _write_csv(self) -> None:
        row = SocialRow(self.datePicker.value, self.twitter.value,
                        self.instagram.value, self.tiktok.value, self.comment_area.value).to_dict()
        self.csv_handler.add_row(row)

    def _get_widgets_values(self) -> dict:
        return SocialRow(self.datePicker.value, self.twitter.value, self.instagram.value, self.tiktok.value, self.comment_area.value).to_dict()

    def _get_widgets_values_as_string(self) -> str:
        values = self._get_widgets_values()
        return f'Created Date : {values["Created Date"]}, Twitter : {values["Twitter"]}, Instagram : {values["Instagram"]}, TikTok : {values["TikTok"]}'

    def _add_new_row(self, button: widgets.Button) -> None:
        values = self._get_widgets_values_as_string()
        print(f'write values : {values}')
        self._write_csv()
        self._clear_widgets()
        self.show_widgets()

    def _clear_widgets(self) -> None:
        self.output.capture(clear_output=True, wait=True)
        clear_output(wait=True)
        self._update_csv_data()

    def show_widgets(self) -> None:
        """Show the widgets and the csv data"""
        display(self.my_widgets)
        display(self.pd_df)
