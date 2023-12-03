import csv
import os
from datetime import date, datetime
from datetime import timedelta
import os.path
from os.path import isfile, join

import pandas as pd
import numpy as np

""""функции поиска значения в датасетах"""


def findValueDataset(path: str, _date: str) -> str:
    """возвращает значение по дате из файла dataset"""
    """Reading Dollar rates from dataset.csv"""
    df = pd.read_csv(f'{path}/dataset.csv', names=['Date', 'Dollar_Rate'])
    try:
        return df[df.Date == date].Dollar_Rate.item()
    except:
        return None


def findValueXY(path: str, _date: str) -> str:
    """возвращает значение по дате из файла X"""
    df1 = pd.read_csv(f'{path}/X.csv', names=['Date'])
    try:
        idx = df1[df1.Date == date].Date.index[0]
        df2 = pd.read_csv(f'{path}/Y.csv', names=['Dollar_Rate'])
        return df2.at[idx, 'Dollar_Rate']
    except:
        return None


def findValueYear(path: str, _date: str) -> str:
    """возвращает значение по дате из файлов по неделям"""
    need_path = ''
    folder = [f for f in os.listdir(f'{path}/script2') if isfile(join(f'{path}/script2', f))]
    try:
        for file in folder:
            if date[:4] == file[:4]:
                need_path = file
        df = pd.read_csv(f'{path}/script2/{need_path}', names=['Date', 'Dollar_Rate'])
        return df[df.Date == date].Dollar_Rate.item()
    except:
        return None


def findValueWeek(path: str, _date: str) -> str:
    """возвращает значение по дате из файла по годам"""
    date_dt = datetime(int(date[:4]), int(date[5:7]), int(date[8:10]))
    folder = [f for f in os.listdir('script3') if isfile(join('script3', f))]
    try:
        for file in folder:
            date_start, date_end = (datetime(int(file[:4]), int(file[4:6]), int(file[6:8])),
                                    datetime(int(file[9:13]), int(file[13:15]), int(file[15:17])))
            if date_start <= date_dt <= date_end:
                df = pd.read_csv(f'{path}/script3/{file}', names=['Date', 'Dollar_Rate'])
                return df[df.Date == date].Dollar_Rate.item()
    except:
        return None