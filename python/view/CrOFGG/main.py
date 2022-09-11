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

def get_view(adic, df):
    for index, row in df.iterrows():
        View = str(row['copyright_institution']).strip()
        View = str(row['copyright_institution']).strip()
        adic[View] = SortedDict()
    return adic

def get_order(adic, df):
    for index, row in df.iterrows():
        View = str(row['copyright_institution']).strip()

        Order = str(row['order']).strip()
        adic[View][Order] = SortedDict()
    return adic

def get_family(adic, df):
    for index, row in df.iterrows():
        View = str(row['copyright_institution']).strip()
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        adic[View][Order][Family] = SortedDict()
    return adic

def get_genus(adic, df):
    for index, row in df.iterrows():
        View = str(row['copyright_institution']).strip()
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        Genus = str(row['genus']).strip()
        adic[View][Order][Family][Genus] = SortedDict()
    return adic

def get_species(adic, df):
    for index, row in df.iterrows():
        View = str(row['copyright_institution']).strip()
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        Genus = str(row['genus']).strip()
        Species = str(row['species']).strip()
        adic[View][Order][Family][Genus][Species] = list()
    return adic


def get_image_file_name(adic, df):
    orderSet = set()
    FamilySet = set()
    GenusSet = set()
    ImageSet = list()
    for index, row in df.iterrows():
        View = str(row['copyright_institution']).strip()
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        Genus = str(row['genus']).strip()
        Species = str(row['species']).strip()
        orderSet.add(Order)
        FamilySet.add(Family)
        GenusSet.add(Genus)


        ImageName = str(row['image_file']).strip()
        caption = str(row['caption']).strip()
        copyright_institution = str(row['copyright_institution']).strip()
        photographer = str(row['photographer']).strip()
        source = str(row['source']).strip()
        identification_method = str(row['identification_method']).strip()
        tup = (ImageName,caption,copyright_institution,photographer,Genus,Species,identification_method, source )

        ImageSet.append(ImageName)

        if tup not in adic[View][Order][Family][Genus][Species]:
            adic[View][Order][Family][Genus][Species].append(tup)

    print ("Order:" + str(len(orderSet)) + ", Family:" + str(len(FamilySet)) + ", Genus:" + str(len(GenusSet)) + ", Completed:" + str(len(ImageSet)) )
    # Order:12, Family:67, Genus:248
    return adic

def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "CrOFGG.json"

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
    nematode_dict = get_species(nematode_dict, df)
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

