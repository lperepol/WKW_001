import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata():
    fn = "../../MetaData/Step_004/MasterMetadata_001_Indexed_Updated.xlsx"
    df = pd.read_excel(fn, sheet_name='Sheet1')
    df = df.fillna('Not Specified')

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
        genus = str(row['genus']).strip()
        image_index = str(row['image_index']).strip().replace(',', ';')
        image_name = str(row['image_file']).strip().replace(',', ';')
        media_descriptor = str(row['media_descriptor']).strip().replace(',', '|')
        view_of_001 = str(row['view_of_001']).strip().replace(',', ';')
        caption = str(row['caption']).strip().replace(',', ';')
        copyright_institution = str(row['copyright_institution']).strip().replace(',', ';')
        photographer = str(row['photographer']).strip().replace(',', ';')
        source = str(row['source']).strip().replace(',', ';')
        species = str(row['species']).strip().replace(',', ';')
        gender = str(row['sex']).strip().replace(',', ';')
        identification_method = str(row['identification_method']).strip().replace(',', ';')
        common_name = str(row['common_name']).strip().replace(',', ';').replace('"', '')
        citation = str(row['citation']).strip().replace('|', ';').replace('"', '')

        atuple = (
            image_index, image_name, caption, media_descriptor, view_of_001, gender, copyright_institution,
            photographer, genus, species, identification_method, source, common_name, citation
        )

        if atuple not in adic[Order][Family][genus]:
            adic[Order][Family][genus].append(atuple)

    return adic


def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "OFG.json"

    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_metadata()
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

