import pandas as pd
import json
from sortedcontainers import SortedList, SortedSet, SortedDict


def readKeys():
    fn = "../Step_002_ImagesToKeys/keys-expanded.xlsx"
    df = pd.read_excel(fn)
    df = df.fillna('Not Specified')
    jsonDict = dict()
    for index, row in df.iterrows():
        diagnostic_key = row['diagnostic_key']
        image_index = row['image_index']
        image_name = row['image_name']
        caption = row['caption']
        media_descriptor = row['media_descriptor']
        diagnostic_descriptor = row['diagnostic_descriptor']
        gender = row['gender']
        copyright_institution = row['copyright_institution']
        photographer = row['photographer']
        genus = row['genus']
        species = row['species']
        identification_method = row['identification_method']
        source = row['source']
        common_name = row['common_name']
        include_in_diagnostic_key = row['include_in_diagnostic_key']
        atuple = (
            #diagnostic_key,
            image_index,
            image_name,
            caption,
            media_descriptor,
            diagnostic_descriptor,
            gender,
            copyright_institution,
            photographer,
            genus,
            species,
            identification_method,
            source,
            common_name,
            include_in_diagnostic_key
            )
        if diagnostic_key in jsonDict:
            jsonDict[diagnostic_key].append(atuple)
        else:
            jsonDict[diagnostic_key] = list()
            jsonDict[diagnostic_key].append(atuple)

    return jsonDict


def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../../files/json/MiaiMullin/Keys.json"
    fn = "Keys.json"
    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    jsonDict = readKeys()
    writeDict2Json(jsonDict)


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")




