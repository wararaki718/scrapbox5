from datetime import datetime

import pandas as pd
import xlsxwriter


def main():
    filename = "sample.xlsx"
    with xlsxwriter.Workbook(filename) as workbook:
        worksheet = workbook.add_worksheet()

        worksheet.set_column("A:A", 20)
        bold = workbook.add_format({"bold": True})
        worksheet.write("A1", "hello")
        worksheet.write("A2", "world", bold)
        worksheet.write(2, 0, datetime.now())

    df = pd.read_excel(filename)
    print(df)
    df.to_excel(filename)

    print("DONE")


if __name__ == "__main__":
    main()
