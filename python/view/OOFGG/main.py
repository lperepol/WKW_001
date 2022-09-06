import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata():
    fn = "../../MetaData/AddTaxonomies/MasterMetadata_000.csv"
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
    orderSet = set()
    FamilySet = set()
    GenusSet = set()
    ImageSet = list()
    for index, row in df.iterrows():
        View = str(row['media_descriptor']).strip()
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        Genus = str(row['genus']).strip()
        Gender = str(row['sex']).strip()
        orderSet.add(Order)
        FamilySet.add(Family)
        GenusSet.add(Genus)


        ImageName = str(row['image_file']).strip()
        caption = str(row['caption']).strip()
        copyright_institution = str(row['copyright_institution']).strip()
        photographer = str(row['photographer']).strip()
        source = str(row['source']).strip()
        species = str(row['species']).strip()
        Gender = str(row['sex']).strip()
        identification_method = str(row['identification_method']).strip()
        tup = (ImageName,caption,Gender, copyright_institution,photographer,Genus,species,identification_method, source )

        ImageSet.append(ImageName)

        if tup not in adic[View][Order][Family][Genus][Gender]:
            adic[View][Order][Family][Genus][Gender].append(tup)

    print ("Order:" + str(len(orderSet)) + ", Family:" + str(len(FamilySet)) + ", Genus:" + str(len(GenusSet)) + ", Completed:" + str(len(ImageSet)) )
    # Order:12, Family:67, Genus:248
    return adic

def get_UNL_stats(df):
    orderSet = set()
    FamilySet = set()
    GenusSet = set()
    LocationSet = set()
    ObservationSet = set()
    HostSet = set()
    SpeciesSet = set()
    ImageSet = set()
    for index, row in df.iterrows():
        Order = str(row['order']).strip()
        Family = str(row['family']).strip()
        Genus = str(row['genus']).strip()
        Gender = str(row['sex']).strip()
        View = str(row['media_descriptor']).strip()
        ImageName = str(row['image_file']).strip()
        orderSet.add(Order)
        FamilySet.add(Family)
        ObservationSet.add(View)
        GenusSet.add(Genus)
        ImageSet.add(ImageName)

    statsDict = dict()
    statsDict["Orders"] = len(orderSet)
    statsDict['Families'] = len(FamilySet)
    statsDict['Genera'] = len(GenusSet)
    statsDict['Observations'] = len(ObservationSet)
    statsDict['Micrographs'] = len(ImageSet)

    json_object = json.dumps(statsDict, indent=4)
    fn = "stats.json"

    with open(fn, "w") as outfile:
        json.dump(statsDict, outfile,indent=4)



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
    get_UNL_stats(df)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

