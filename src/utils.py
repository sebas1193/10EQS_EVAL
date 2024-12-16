import pandas as pd
from dateutil import parser


def parse_date(date_str):
    """
    This function tries to parse a date string using pandas.to_datetime. 
    If it fails, it tries to parse it using dateutil.parser.

    That can manage different date formats.
    """
    try:
        return pd.to_datetime(date_str, errors='raise')
    except Exception:
        try:
            return pd.to_datetime(parser.parse(date_str), errors='coerce')
        except Exception:
            return pd.NaT