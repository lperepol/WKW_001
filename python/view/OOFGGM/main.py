import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn)
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

def get_view(adic, df):
    for index, row in df.iterrows():
        View = str(row['Detail']).strip()
        if View == '0':
            continue
        View = str(row['Detail']).strip()
        adic[View] = SortedDict()
    return adic

def get_order(adic, df):
    for index, row in df.iterrows():
        View = str(row['Detail']).strip()
        if View == '0':
            continue

        Order = str(row['Order']).strip()
        adic[View][Order] = SortedDict()
    return adic

def get_family(adic, df):
    for index, row in df.iterrows():
        View = str(row['Detail']).strip()
        if View == '0':
            continue
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        adic[View][Order][Family] = SortedDict()
    return adic

def get_genus(adic, df):
    for index, row in df.iterrows():
        View = str(row['Detail']).strip()
        if View == '0':
            continue
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        adic[View][Order][Family][Genus] = SortedDict()
    return adic

def get_gender(adic, df):
    for index, row in df.iterrows():
        View = str(row['Detail']).strip()
        if View == '0':
            continue
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Gender = str(row['Gender']).strip()
        adic[View][Order][Family][Genus][Gender] = SortedDict()
    return adic

def get_magnification(adic, df):
    for index, row in df.iterrows():
        View = str(row['Detail']).strip()
        if View == '0':
            continue
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Gender = str(row['Gender']).strip()
        Magnification = str(row['Magnification']).strip()
        adic[View][Order][Family][Genus][Gender][Magnification] = list()
    return adic


def get_image_file_name(adic, df):
    orderSet = set()
    FamilySet = set()
    GenusSet = set()
    ImageSet = set()
    for index, row in df.iterrows():
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Gender = str(row['Gender']).strip()
        Magnification = str(row['Magnification']).strip()
        View = str(row['Detail']).strip()
        orderSet.add(Order)
        FamilySet.add(Family)
        GenusSet.add(Genus)

        if View == '0':
            continue

        ImageName = str(row['ImageName']).strip()
        ImageSet.add(ImageName)

        if ImageName not in adic[View][Order][Family][Genus][Gender][Magnification]:
            adic[View][Order][Family][Genus][Gender][Magnification].append(ImageName)

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
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Gender = str(row['Gender']).strip()
        Magnification = str(row['Magnification']).strip()
        View = str(row['Detail']).strip()
        Location = str(row['Location']).strip()
        Host = str(row['Host']).strip()
        Species = str(row['Species']).strip()
        ImageName = str(row['ImageName']).strip()
        orderSet.add(Order)
        FamilySet.add(Family)
        LocationSet.add(Location)
        ObservationSet.add(View)
        HostSet.add(Location)
        GenusSet.add(Host)
        SpeciesSet.add(Species)
        ImageSet.add(ImageName)

    statsDict = dict()
    statsDict["Orders"] = len(orderSet)
    statsDict['Families'] = len(FamilySet)
    statsDict['Genera'] = len(GenusSet)
    statsDict['Species'] = len(SpeciesSet)
    statsDict['Locations'] = len(LocationSet)
    statsDict['Observations'] = len(ObservationSet)
    statsDict['Micrographs'] = len(ImageSet)

    json_object = json.dumps(statsDict, indent=4)
    fn = "../../../files/json/unl/Unl_stats.json"

    with open(fn, "w") as outfile:
        json.dump(statsDict, outfile,indent=4)



def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../files/json/unl/OOFGGM.json"

    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_metadata()
    df = fixup(df)
    nematode_dict = SortedDict()
    nematode_dict = get_view(nematode_dict, df)
    nematode_dict = get_order(nematode_dict, df)
    nematode_dict = get_family(nematode_dict, df)
    nematode_dict = get_genus(nematode_dict, df)
    nematode_dict = get_gender(nematode_dict, df)
    nematode_dict = get_magnification(nematode_dict, df)
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)
    get_UNL_stats(df)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

