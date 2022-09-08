import pandas as pd

def readKeys():
    fn = '../../../../Identification_keys_redo/Miai Mullin.xlsx'
    df = pd.read_excel(fn, sheet_name='Miai Mullin')
    return df

    #fn = '../../../../Identification_keys_redo/Miai Mullin.xlsx'
    #f = open(fn, "w")
    #f.write("Woops! I have deleted the content!")
    #f.close()

def readImages():
    fn = '../../../../UNL/Python/Metadata/ManualEdits/KeepMetadata_002.xlsx'
    df = pd.read_excel(fn, sheet_name='KeepMetadata_003_test')
    imageDict = dict()
    for index, row in df.iterrows():
        Genus = row['Genus']
        ImageName = row['ImageName']
        Detail = row['Detail']
        atuple = (ImageName, Detail)
        if Genus in imageDict:
            imageDict[Genus].append(atuple)
        else:
            imageDict[Genus] = list()
            imageDict[Genus].append(atuple)
    return imageDict

def associate_key_to_image():
    imageDict = readImages()
    df = readKeys()
    lis = list()
    keyDict = dict()
    for index, row in df.iterrows():
        KeyFrom = row['KeyFrom']
        Description = row['Description']
        KeyTo = row['KeyTo']
        imageList = list()
        if KeyTo in imageDict:
            imageList = imageDict[KeyTo]
        atuple = (Description,KeyTo,imageList)
        if KeyFrom in keyDict:
            keyDict[KeyFrom].append(atuple)
        else:
            keyDict[KeyFrom] = list()
            keyDict[KeyFrom].append(atuple)

    return keyDict

def write_key_file(keyDict):
    header = 'Key,Param,Image,Obs,Genus,Include,ImageDetail\n'
    with open('Keys.csv', 'w', encoding="utf-8") as f:
        f.write(header)
        Key = ''
        Param = ''
        Image = ''
        Obs = ''
        genus = ''
        Include = 'Yes'
        ImageDetail = ''
        for i in keyDict:
            line = ''
            KeyFrom = i
            Key = KeyFrom
            Key = str(Key).zfill(3)
            count = 1;
            for j in keyDict[i]:
                Obs = j[0]
                genus = j[1]
                imageList = j[2]
                for k in imageList:
                    (ImageName, ImageDetail) = k
                    Param = 'accordioncollapse-' + str(count) + '-' + str(Key)
                    ss = 0
                    line = str(KeyFrom) + ','
                    line = line + Param + ','
                    line = line + ImageName + ','
                    line = line + '"' + Obs + '"' + ','
                    line = line + genus + ','
                    line = line + Include + ','
                    line = line + ImageDetail + '\n'
                    f.write(line)
                count = count + 1

def main():
    keyDict = associate_key_to_image()
    write_key_file(keyDict)


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")




