import pandas as pd
import openpyxl
import xml.etree.ElementTree as ET
import xmltodict
import os

#def test():
#    f = open("../../../Identification_keys_redo/BoldSystems/Bold_data/BoldSystems.csv", "r")
#    f.write("Now the file has more content!")
#    f.close()
#    for index, row in df.iterrows():
#        #ImgIndex = str(row['ImageIndex']).strip()
#        #df.loc[index, 'ImageIndex'] = ImgIndex
#        #count = count + 1

def read_excel(fn, sheet):
    df = pd.read_excel(fn, sheet_name=sheet)
    df = df.fillna('Not Specified')
    return df

def read_csv(fn):
    df = pd.read_csv(fn, encoding = "utf-8" )
    df = df.fillna('Not Specified')
    return df
    #df.to_csv(fn, index=False)

def get_Genus(df):
    genusDict = dict()
    for index, row in df.iterrows():
        genus = str(row['Genus']).strip()
        Family = str(row['Family']).strip()
        Order = str(row['Order']).strip()
        Class1 = str(row['Class']).strip()
        Phylum = str(row['Phylum']).strip()
        ScientificName_accepted = str(row['ScientificName_accepted']).strip()
        ScientificName = str(row['ScientificName']).strip()
        values = (Family,Order,Class1,Phylum,ScientificName_accepted,ScientificName)
        genusDict[genus] = values
    return genusDict

def get_CommonNames(df):
    df['genus'] = ''
    commonNamesDict = dict()
    for index, row in df.iterrows():
        Genus = str(row['Genus or Genus and species']).strip()
        Genus = Genus.split()
        Genus =  str(Genus[0]).strip(' ')
        df.loc[index, 'genus'] = Genus
        commonNamesDict[Genus] = list()
    for index, row in df.iterrows():
        genus = str(row['genus']).strip()
        CommonName = str(row['Common Name']).strip()
        commonNamesDict[genus].append(CommonName)
    return commonNamesDict

def fix_collection(df,genusDict,commonNamesDict):
    df['scientificName_accepted'] = ''
    df['scientificName'] = ''
    df['CommonName'] = ''
    imageCount = 1
    for index, row in df.iterrows():
        ImageIndex = f'ImageIndex_{imageCount:05d}'
        df.loc[index, 'ImageIndex'] = ImageIndex
        imageCount = imageCount + 1
        genus = str(row['genus']).strip()
        source = str(row['source']).strip()
        if (source == 'https://nematodes.myspecies.info'):
            df.loc[index, 'copyright_institution'] = 'Nematology Research Unit  Ghent University'

        copyright_institution = str(row['copyright_institution']).strip()
        if copyright_institution == 'Tom Powers':
            df.loc[index, 'copyright_institution'] = 'University of Nebraska'
        if copyright_institution == 'University of Nebraska-Lincoln':
            df.loc[index, 'copyright_institution'] = 'University of Nebraska'
        if copyright_institution == 'El Colegio de la Frontera Sur':
            df.loc[index, 'copyright_institution'] = 'El Colegio de la Frontera Sur, Unidad Chetumal'

        (family,order,class1,phylum,scientificName_accepted,scientificName) = genusDict[genus]

        df.loc[index, 'family'] = family
        df.loc[index, 'order'] = order
        df.loc[index, 'class'] = class1
        df.loc[index, 'phylum'] = phylum
        df.loc[index, 'scientificName_accepted'] = scientificName_accepted
        df.loc[index, 'scientificName'] = scientificName
        CommonName = ''
        if genus in commonNamesDict:
            for i in commonNamesDict[genus]:
                CommonName = CommonName + i + ' | '
        df.loc[index, 'CommonName'] = CommonName
    fn = 'MasterMetadata_001.csv'
    df = df.fillna('Not Specified')
    df = df.replace({'None': 'Not Specified'}, regex=True)
    df = df.replace({'none': 'Not Specified'}, regex=True)
    df.to_csv(fn, encoding='utf-8', index=False)

def main():
    fn = './NematodeCommonNames.csv'
    commonNames_df = read_csv(fn)
    commonNamesDict = get_CommonNames(commonNames_df)
    fn = '../Step_001/ConcatinatedFixGenus.csv'
    con_df = read_csv(fn)
    fn = './genus_matched.xlsx'
    gen_df = read_excel(fn,'Nemys match')
    genusDict = get_Genus(gen_df)

    fix_collection(con_df,genusDict, commonNamesDict)
    print(gen_df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()