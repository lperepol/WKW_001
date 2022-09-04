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



def get_genus(adic, df):
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if len(image_file) < 1:
            continue
        genus = str(row['genus']).strip()
        adic[genus] = list()
    return adic

def get_image_file_name(adic, df):
    for index, row in df.iterrows():
        image_file = str(row['image_file']).strip()
        if len(image_file) < 1:
            continue
        genus = str(row['genus']).strip()
        species = str(row['species']).strip()
        caption = str(row['caption']).strip()
        copyright_institution = str(row['copyright_institution']).strip()
        photographer = str(row['photographer']).strip()
        identification_method = str(row['identification_method']).strip()

        image_file = str(row['image_file']).strip()
        mylist = [image_file, caption, copyright_institution, photographer,genus,species, identification_method]
        if mylist not in adic[genus]:
            adic[genus].append(mylist)

    return adic



def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../files/json/boldsystems/ToJSonGenus.json"

    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_write_csv()
    nematode_dict = SortedDict()
    nematode_dict = get_genus(nematode_dict, df)
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

