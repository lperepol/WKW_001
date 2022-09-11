import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata():
    fn = "../../MetaData/Step_002_AddTaxonomies/MasterMetadata_001.csv"
    df = pd.read_csv(fn)
    df = df.fillna('Not Specified')
    return df


def fixup(df):
    return
    df = df.fillna('')
    for index, row in df.iterrows():
        Magnification = str(row['Magnification']).strip()
        if Magnification.isdigit():
            Magnification = int(Magnification)
            Magnification = "{:03d}X".format(Magnification)
        df.loc[index, 'Magnification'] = Magnification
    return df


def get_order(adic, df):
    for index, row in df.iterrows():

        Order = str(row['order']).strip()
        adic[Order] = SortedDict()
    return adic

def get_family(adic, df):
    for index, row in df.iterrows():
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        adic[Order][Family] = SortedDict()
    return adic

def get_genus(adic, df):
    for index, row in df.iterrows():
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        Genus = str(row['genus']).strip()
        adic[Order][Family][Genus] = list()
    return adic

def get_image_file_name(adic, df):
    for index, row in df.iterrows():
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        Genus = str(row['genus']).strip()
        ImageName = str(row['image_file']).strip()
        caption = str(row['caption']).strip()
        copyright_institution = str(row['copyright_institution']).strip()
        photographer = str(row['photographer']).strip()
        source = str(row['source']).strip()
        species = str(row['species']).strip()
        Gender = str(row['sex']).strip()
        identification_method = str(row['identification_method']).strip()
        tup = (ImageName,caption,Gender, copyright_institution,photographer,Genus,species,identification_method, source )


        if tup not in adic[Order][Family][Genus]:
            adic[Order][Family][Genus].append(tup)

    return adic


def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "OFG.json"

    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_metadata()
    #df = fixup(df)
    nematode_dict = SortedDict()
    nematode_dict = get_order(nematode_dict, df)
    nematode_dict = get_family(nematode_dict, df)
    nematode_dict = get_genus(nematode_dict, df)
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

