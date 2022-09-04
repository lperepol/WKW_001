import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_write_csv():
    fn = "../Bold_data/BoldSystems.csv"
    df = pd.read_csv(fn)
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


def get_view(adic, df):
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if len(image_file) < 1:
            continue

        media_descriptor = str(row['media_descriptor']).strip()
        adic[media_descriptor] = SortedDict()
    return adic

def get_order(adic, df):
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if len(image_file) < 1:
            continue

        media_descriptor = str(row['media_descriptor']).strip()

        order = str(row['order']).strip()
        adic[media_descriptor][order] = SortedDict()
    return adic

def get_family(adic, df):
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if len(image_file) < 1:
            continue
        media_descriptor = str(row['media_descriptor']).strip()

        order = str(row['order']).strip()
        family = str(row['family']).strip()
        adic[media_descriptor][order][family] = SortedDict()
    return adic

def get_genus(adic, df):
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if len(image_file) < 1:
            continue

        media_descriptor = str(row['media_descriptor']).strip()
        order = str(row['order']).strip()
        family = str(row['family']).strip()
        genus = str(row['genus']).strip()
        adic[media_descriptor][order][family][genus] = SortedDict()
    return adic

def get_species(adic, df):
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if len(image_file) < 1:
            continue
        media_descriptor = str(row['media_descriptor']).strip()

        order = str(row['order']).strip()
        family = str(row['family']).strip()
        genus = str(row['genus']).strip()
        species = str(row['species']).strip()
        adic[media_descriptor][order][family][genus][species] = SortedDict()
    return adic

def get_gender(adic, df):
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if len(image_file) < 1:
            continue

        media_descriptor = str(row['media_descriptor']).strip()
        order = str(row['order']).strip()
        family = str(row['family']).strip()
        genus = str(row['genus']).strip()
        species = str(row['species']).strip()
        gender = str(row['sex']).strip()
        adic[media_descriptor][order][family][genus][species][gender] = list()
    return adic


def get_image_file_name(adic, df):
    orderSet = set()
    FamilySet = set()
    GenusSet = set()
    speciesSet = set()
    ImageSet = set()
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if len(image_file) < 1:
            continue
        media_descriptor = str(row['media_descriptor']).strip()

        order = str(row['order']).strip()
        family = str(row['family']).strip()
        genus = str(row['genus']).strip()
        species = str(row['species']).strip()
        gender = str(row['sex']).strip()
        media_descriptor = str(row['media_descriptor']).strip()
        caption = str(row['caption']).strip()
        copyright_institution = str(row['copyright_institution']).strip()
        photographer = str(row['photographer']).strip()
        identification_method = str(row['identification_method']).strip()
        orderSet.add(order)
        FamilySet.add(family)
        GenusSet.add(genus)
        speciesSet.add(species)

        image_file = str(row['image_file']).strip()
        ImageSet.add(image_file)
        mylist = [image_file, caption, copyright_institution, photographer,genus,species, identification_method]
        if mylist not in adic[media_descriptor][order][family][genus][species][gender]:
            adic[media_descriptor][order][family][genus][species][gender].append(mylist)

    print ("order:" + str(len(orderSet)) + ", family:" + str(len(FamilySet)) + ", genus:" + str(len(GenusSet)) + "species:" + str(len(speciesSet)) +  ", Completed:" + str(len(ImageSet)) )
    # order:12, family:67, genus:248
    return adic



def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../files/json/boldsystems/OOFGS.json"

    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_write_csv()
    nematode_dict = SortedDict()
    nematode_dict = get_view(nematode_dict, df)
    nematode_dict = get_order(nematode_dict, df)
    nematode_dict = get_family(nematode_dict, df)
    nematode_dict = get_genus(nematode_dict, df)
    nematode_dict = get_species(nematode_dict, df)
    nematode_dict = get_gender(nematode_dict, df)
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

