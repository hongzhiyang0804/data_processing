import pandas as pd


def csv_to_xlsx_pd():
    csv = pd.read_csv('name.csv', encoding='utf-8')
    csv.to_excel('fs.xlsx', sheet_name='data')


if __name__ == '__main__':
    csv_to_xlsx_pd()