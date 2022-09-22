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

def get_view(adic, df):
    for index, row in df.iterrows():
        View = str(row['media_descriptor']).strip()
        View = str(row['media_descriptor']).strip()
        adic[View] = SortedDict()
    return adic

def get_order(adic, df):
    for index, row in df.iterrows():
        View = str(row['media_descriptor']).strip()

        Order = str(row['order']).strip()
        adic[View][Order] = SortedDict()
    return adic

def get_family(adic, df):
    for index, row in df.iterrows():
        View = str(row['media_descriptor']).strip()
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        adic[View][Order][Family] = SortedDict()
    return adic

def get_genus(adic, df):
    for index, row in df.iterrows():
        View = str(row['media_descriptor']).strip()
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        Genus = str(row['genus']).strip()
        adic[View][Order][Family][Genus] = SortedDict()
    return adic

def get_gender(adic, df):
    for index, row in df.iterrows():
        View = str(row['media_descriptor']).strip()
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        Genus = str(row['genus']).strip()
        Gender = str(row['sex']).strip()
        adic[View][Order][Family][Genus][Gender] = list()
    return adic


def get_image_file_name(adic, df):
    for index, row in df.iterrows():
        View = str(row['media_descriptor']).strip()
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        genus = str(row['genus']).strip()
        image_index = str(row['image_index']).strip().replace(',', ';')
        image_name = str(row['image_file']).strip().replace(',', ';')
        media_descriptor = str(row['media_descriptor']).strip().replace(',', '|')
        diagnostic_descriptor = str(row['diagnostic_descriptor']).strip().replace(',', ';')
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
            image_index, image_name, caption, media_descriptor, diagnostic_descriptor, gender, copyright_institution,
            photographer, genus, species, identification_method, source, common_name, citation
        )


        if atuple not in adic[View][Order][Family][genus][gender]:
            adic[View][Order][Family][genus][gender].append(atuple)

    return adic


def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "OOFGG.json"

    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_metadata()
    #df = fixup(df)
    nematode_dict = SortedDict()
    nematode_dict = get_view(nematode_dict, df)
    nematode_dict = get_order(nematode_dict, df)
    nematode_dict = get_family(nematode_dict, df)
    nematode_dict = get_genus(nematode_dict, df)
    nematode_dict = get_gender(nematode_dict, df)
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

