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


def get_sup_images(df):
    imageDict = dict()
    for index, row in df.iterrows():
        image_file = str(row['Images']).strip()
        imageDict[image_file] = image_file
    return imageDict

def update_citations(df, imageDict):
    imagePath = 'https://raw.githubusercontent.com/lperepol/Supplementary/main/Plant-Parasitic_Nematodes_William_Mai_Sup/images/'
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if image_file in imageDict:
            fnLoc = imagePath + image_file
            df.loc[index, 'image_file'] = fnLoc
    fn = 'MasterMetadata_001_Indexed_Updated.csv'
    df.to_csv(fn, encoding='utf-8', index=True)

def main():

    fn = 'MasterMetadata_001.xlsx'
    master_df = read_excel(fn,'Sheet1')

    fn = 'Images.csv'
    images_df = read_csv(fn)
    imageDict = get_sup_images(images_df)
    update_citations(master_df,imageDict)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()