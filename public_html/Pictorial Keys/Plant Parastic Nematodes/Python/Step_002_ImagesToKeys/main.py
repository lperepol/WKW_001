import pandas as pd
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def GenusSet():
    AGenusSet = {
        "Acontylus",
        "Anguina",
        "Aorolaimus",
        "Aphasmatylenchus",
        "Aphelenchoides",
        "Aphelenchus",
        "Atalodera",
        "Atylenchus",
        "Bakernema",
        "Belonolaimus",
        "Brachydorus",
        "Bursaphelenchus",
        "Bursaphelenchus",
        "Cacopaurus",
        "Caloosia",
        "Carphodorus",
        "Criconema",
        "Criconemoides",
        "Cryphodera",
        "Ditylenchus",
        "Dolichodorus",
        "Eutylenchus",
        "Globodera",
        "Helicotylenchus",
        "Hemicriconemoides",
        "Hemicycliophora",
        "Heterodera",
        "Heterodera",
        "Hirschmanniella",
        "Histotylenchus",
        "Hoplolaimus",
        "Hoplotylus",
        "Longidorus",
        "Macrotrophurus",
        "Meloidodera",
        "Meloidogyne",
        "Morulaimus",
        "Nacobbus",
        "Nothotylenchus",
        "Nothanguina",
        "Paralongidorus",
        "Paratrichodorus",
        "Paratrophurus",
        "Paratrophurus",
        "Paratylenchus",
        "Paratylenchus",
        "Peltamigratus",
        "Pratylenchoides",
        "Pratylenchus",
        "Psilenchus",
        "Radopholoides",
        "Radopholus",
        "Rotylenchoides",
        "Rotylenchulus",
        "Rotylenchus",
        "Scutellonema",
        "Scutylenchus",
        "Sphaeronema",
        "Subanguina",
        "Telotylenchus",
        "Trichotylenchus",
        "Trophotylenchulus",
        "Trophotylenchulus",
        "Trophurus",
        "Tylenchorhynchus",
        "Tylenchulus",
        "Tylenchus",
        "Tylodorus",
        "Xiphinema",
        "Zygotylenchus"
    }
    return AGenusSet


def readImages():
    ppnGenus = GenusSet()
    fn = "../../../../../python/MetaData/Step_002_AddTaxonomies/MasterMetadata_001.xlsx"
    df = pd.read_excel(fn)
    imageDict = dict()
    for index, row in df.iterrows():
        genus = row['genus']
        if genus in ppnGenus:
            ImageName = str(row['image_file']).strip().replace(',', '|')
            media_descriptor = str(row['media_descriptor']).strip().replace(',', '|')
            diagnostic_descriptor = str(row['diagnostic_descriptor']).strip().replace(',', '|')
            caption = str(row['caption']).strip().replace(',', '|')
            copyright_institution = str(row['copyright_institution']).strip().replace(',', '|')
            photographer = str(row['photographer']).strip().replace(',', '|')
            source = str(row['source']).strip().replace(',', '|')
            species = str(row['species']).strip().replace(',', '|')
            gender = str(row['sex']).strip().replace(',', '|')
            identification_method = str(row['identification_method']).strip().replace(',', '|')
            atuple = (
            ImageName, caption,media_descriptor,diagnostic_descriptor, gender, copyright_institution, photographer, genus, species, identification_method, source,caption)

            if genus in imageDict:
                imageDict[genus].append(atuple)
            else:
                imageDict[genus] = list()
                imageDict[genus].append(atuple)
    return imageDict

def associate_key_to_image():
    imageDict = readImages()
    fn = '../../../../../python/Dichotomous Keys/Miai Mullin.xlsx'
    df = pd.read_excel(fn, sheet_name='Sheet1')
    lis = list()
    LinesInKey = dict()
    keyDict = dict()
    jsonDict = dict()
    for index, row in df.iterrows():
        From = row['From']
        To = str(row['To']).strip()
        if From in LinesInKey:
            LinesInKey[From] =  LinesInKey[From] + 1
        else:
            LinesInKey[From] = 1
        Key = str(From).zfill(3)
        Param = 'accordioncollapse-' + str(LinesInKey[From]) + '-' + str(Key)

        spltTo = To.split(' ')
        images = ''
        for i in spltTo:
            if i in imageDict:
                images = imageDict[i]

        if images == '':
            continue

        if Param in jsonDict:
            for img in images:
                jsonDict[Param].append(img)
        else:
            jsonDict[Param] = list()
            for img in images:
                jsonDict[Param].append(img)
    return jsonDict

def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../../files/json/MiaiMullin/Keys.json"
    fn = "Keys.json"
    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def dictToCSV(jsonDict):
    header = 'Key,ImageName,caption,Gender,copyright_institution,photographer,genus,species,identification_method,source'
    with open('test6.csv', 'w') as f:
        f.write("%s\n" % (header))
        for key in jsonDict.keys():
            for row in jsonDict[key]:
                rowstr = str(row)
                rowstr = rowstr[1:]
                rowstr = rowstr.rstrip(rowstr[-1])
                rowstr = rowstr.replace("'", '')
                f.write("%s, %s\n" % (key, rowstr))

def main():
    jsonDict = associate_key_to_image()
    dictToCSV(jsonDict)
    writeDict2Json(jsonDict)


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")




