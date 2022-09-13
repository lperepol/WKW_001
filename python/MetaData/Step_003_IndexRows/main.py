import pandas as pd
import openpyxl
import xml.etree.ElementTree as ET
import xmltodict
import os

#def test():
#    f = open("../../../Identification_keys_redo/BoldSystems/Bold_data/BoldSystems.csv", "r")
#    f.write("Now the file has more content!")
#    f.close()
#    for index, row in df.iterrows():
#        #ImgIndex = str(row['ImageIndex']).strip()
#        #df.loc[index, 'ImageIndex'] = ImgIndex
#        #count = count + 1

def read_excel(fn, sheet):
    df = pd.read_excel(fn, sheet_name=sheet)
    df = df.fillna('')
    return df

def read_csv(fn):
    df = pd.read_csv(fn, encoding = "utf-8" )
    df = df.fillna('')
    return df
    #df.to_csv(fn, index=False)

def index_rows(df):
    imageCount = 1
    for index, row in df.iterrows():
        ImageIndex = f'ImageIndex_{imageCount:05d}'
        df.loc[index, 'image_index'] = ImageIndex
        imageCount = imageCount + 1
    fn = 'MasterMetadata_001_Indexed.csv'
    df.to_csv(fn, encoding='utf-8', index=False)

def main():

    fn = 'MasterMetadata_001.xlsx'
    master_df = read_excel(fn,'Sheet1')
    index_rows(master_df)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()