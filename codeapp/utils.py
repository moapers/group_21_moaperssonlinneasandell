# built-in imports
# standard library imports
import csv
import pickle
from datetime import date
from typing import Dict, List

import requests

# external imports
from flask import current_app

# internal imports
from codeapp import db
from codeapp.models import Sales


def get_data_list() -> list[Sales]:
    """
    Function responsible for downloading the dataset from the source, translating it
    into a list of Python objects, and saving it to a Redis list.
    """
    if db.exists("dataset_list") > 0:
        current_app.logger.info("Dataset already downloaded.")
        dataset_stored: list[Sales] = []
        raw_dataset: list[bytes] = db.lrange("dataset_list", 0, -1)
        for item in raw_dataset:
            dataset_stored.append(pickle.loads(item))
        return dataset_stored

    url = "https://onu1.s2.chalmers.se/datasets/Europe_Sales_Records.csv"
    response = requests.get(url, timeout=5)
    with open("eu_sales.csv", "wb") as file:
        file.write(response.content)
    print("download sucess")

    dataset_base: List[Sales] = []
    with open("eu_sales.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_sales = Sales(
                order_id=int(row["Order ID"]),
                country=row["Country"],
                item_type=row["Item Type"],
                order_priority=row["Order Priority"],
                order_date=date(2000, 5, 25),
                ship_date=date(2001, 9, 17),
                units_sold=int(row["Units Sold"]),
                profit=float(row["Total Profit"]),
            )
            db.rpush("dataset_list", pickle.dumps(new_sales))
            dataset_base.append(new_sales)
    return dataset_base


def calculate_statistics(dataset: List[Sales]) -> Dict[str, float]:
    """
    Receives the dataset in the form of a list of Python objects, and calculates the
    statistics necessary.
    """
    total_profit_per_type = {}
    count_per_type = {}

    for sale in dataset:
        if sale.item_type not in total_profit_per_type:
            total_profit_per_type[sale.item_type] = 0
            count_per_type[sale.item_type] = 0
        total_profit_per_type[sale.item_type] += int(sale.profit)
        count_per_type[sale.item_type] += 1

    average_profit_per_type = {}
    for item_type, total_profit in total_profit_per_type.items():
        count = count_per_type[item_type]
        average_profit_per_type[item_type] = total_profit / count

    return average_profit_per_type


def prepare_figure(input_figure: str) -> str:
    """
    Method that removes limits to the width and height of the figure. This method must
    not be changed by the students.
    """
    output_figure = input_figure.replace('height="345.6pt"', "").replace(
        'width="460.8pt"', 'width="100%"'
    )
    return output_figure
