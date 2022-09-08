import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict


def read_keys():
    fn = "../Step_002_ImagesToKeys/ManualEditKeys.csv"
    df = pd.read_csv(fn,  encoding= 'unicode_escape')
    df = df.fillna('')
    return df

def fixup(df):
    df = df.fillna(0)
    for index, row in df.iterrows():
        Magnification = str(row['Magnification']).strip()
        if Magnification.isdigit():
            Magnification = int(Magnification)
            Magnification = "{:03d}X".format(Magnification)
        df.loc[index, 'Magnification'] = Magnification
    return df

def get_Keys(adic, df):
    for index, row in df.iterrows():
        Param = str(row['Param']).strip()
        Image = str(row['Image' ]).strip()
        Include = str(row['Include' ]).strip()
        if len(Include) > 1:
            adic[Param] = list()
    return adic

def get_images(adic, df):
    for index, row in df.iterrows():
        Include = str(row['Include' ]).strip()
        if len(Include) < 2:
            continue;
        Param = str(row['Param']).strip()
        Image = str(row['Image' ]).strip()
        Genus = str(row['Genus' ]).strip()
        Obs = str(row['Obs' ]).strip()
        ImageDetail = str(row['ImageDetail' ]).strip()
        Source = str(row['Source' ]).strip()
        lst = [Image, Genus, Obs,ImageDetail,Source]
        if lst not in adic[Param]:
            adic[Param].append(lst)
    return adic

def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../files/json/MiaiMullin/Keys.json"
    fn = "../../../../files/json/MiaiMullin/Keys.json"
    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    #df = fixup(df)
    df = read_keys()
    nematode_dict = SortedDict()
    nematode_dict = get_Keys(nematode_dict, df)
    nematode_dict = get_images(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)

if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

