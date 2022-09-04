import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_write_excel():
    fn = "../../../Key to the suborder of the Rhabdita.xlsx"
    df = pd.read_excel(fn,sheet_name='Sheet1')
    df = df.fillna('')
    return df

    df["ImageIndex"] = ''
    count = 1
    ImageIndex = df['ImageIndex']
    df.drop(labels=['ImageIndex'], axis=1, inplace=True)
    df.insert(0, 'ImageIndex', ImageIndex)
    for index, row in df.iterrows():
        ImgIndex = str(row['ImageIndex']).strip()
        ImgIndex = "ImgIndex_" + str(count).zfill(4)
        df.loc[index, 'ImageIndex'] = ImgIndex
        count = count + 1
    df.to_csv(fn, index=False)

def clean(df):
    df = df.replace('\n', '', regex=True)
    fn = "../../../Key to the suborder of the Rhabdita.csv"
    df.to_csv(fn, index=False)

def main():
    df = read_write_excel()
    clean(df)

if __name__ == '__main__':
    print("Begin")
    main()
    print("End")