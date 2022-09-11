import pandas as pd
import openpyxl
import xml.etree.ElementTree as ET
import xmltodict
import os

# Nomalized Headers
#	ImageIndex
#	identification_method
#	phylum
#	class
#	order
#	family
#	genus
#	species
#	sex
#	lifestage
#	lat
#	lon
#	caption
#	media_descriptor
#	image_file
#	copyright_institution
#	photographer
#	source

def read_excel(fn, sheet):
    df = pd.read_excel(fn, sheet_name=sheet)
    df = df.fillna('')
    return df

def read_csv(fn):
    df = pd.read_csv(fn, encoding = "utf-8" )
    df = df.fillna('')
    return df
    #df.to_csv(fn, index=False)

#def test():
#    f = open("../../../Identification_keys_redo/BoldSystems/Bold_data/BoldSystems.csv", "r")
#    f.write("Now the file has more content!")
#    f.close()
#    for index, row in df.iterrows():
#        #ImgIndex = str(row['ImageIndex']).strip()
#        #df.loc[index, 'ImageIndex'] = ImgIndex
#        #count = count + 1

def NormalizedBoldData():
    fn = "../../BoldSystems/Bold_data/BoldSystems.csv"
    df = read_csv(fn)
    df['source'] = 'http://boldsystems.org/index.php/Taxbrowser_Taxonpage?taxid=19'
    df.drop('record_id', axis=1, inplace=True)
    df.drop('processid', axis=1, inplace=True)
    df.drop('specimen_identifiers', axis=1, inplace=True)
    df.drop('lat', axis=1, inplace=True)
    df.drop('lon', axis=1, inplace=True)
    df.drop('site_code', axis=1, inplace=True)
    fn = 'NormalizedBoldData.csv'
    df.to_csv(fn, index=False)
    return df

def NormalizedUNLData():
    fn = "../../UNL/Python/Metadata/ManualEdits/KeepMetadata_002.xlsx"
    sheet = 'KeepMetadata_003_test'
    df = read_excel(fn, sheet)
    df['source'] = 'https://nematode.unl.edu'
    df['phylum'] = 'Nematoda'
    df = df.rename(columns={"ImageName": "image_file", "Gender": "sex"})
    df = df.rename(columns={"ImageName": "image_file", "Gender": "sex"})
    df.drop('General', axis=1, inplace=True)
    df.drop('Descr', axis=1, inplace=True)
    df.drop('Location', axis=1, inplace=True)
    df.drop('Host', axis=1, inplace=True)
    df = df.rename(columns={"Detail": "caption", "KeyArea": "media_descriptor"})
    df['copyright_institution'] = 'University of Nebraska'
    df.drop('ScientificName_accepted', axis=1, inplace=True)
    df.drop('ScientificName', axis=1, inplace=True)
    df.drop('Magnification', axis=1, inplace=True)
    df = df.rename(columns={"Species": "species", "Class": "class"})
    df = df.rename(columns={"Order": "order", "Class": "class"})
    df = df.rename(columns={"Family": "family", "Genus": "genus"})
    return df

def NormalizedWURData():
    fn = "../../WUR/Python/Step_00s_Get_Images/ImagesOnWUR.csv"
    df = read_csv(fn)
    df['source'] = 'https://www.wur.nl'
    df['phylum'] = 'Nematoda'
    df = df.rename(columns={"genus": "species", "href": "image_file"})
    df = df.rename(columns={"author": "photographer", "href": "image_file"})
    df.drop('title', axis=1, inplace=True)
    df['copyright_institution'] = 'Wageningen University & Research'
    for index, row in df.iterrows():
        species = str(row['species']).strip()
        if species == 'Achromadora':
            gg =0
        splt = species.split(' ')
        if len(splt) > 1 :
            df.loc[index, 'genus'] = str(splt[0]).strip()
        www = len(splt)
        if len(splt) == 1 :
            df.loc[index, 'genus'] = species
            df.loc[index, 'species'] = ''

    return df

def nematodes_myspecies_info():
    fn = "X:/nemtode/general/Supplementary/nematodes.myspecies.info/python/Step_003/Query1.xlsx"
    df = read_excel(fn,'Sheet1')
    df['source'] = 'https://nematodes.myspecies.info'
    df['phylum'] = 'Nematoda'
    df.drop('Catalogue-number', axis=1, inplace=True)
    df = df.rename(columns={"Basis-of-record": "media_descriptor"})
    df = df.rename(columns={"Institution-code": "copyright_institution"})
    df = df.rename(columns={"Collector": "photographer"})
    df = df.rename(columns={"Identification-qualifier": "identification_method"})
    df = df.rename(columns={"Lifestage": "lifestage"})
    df = df.rename(columns={"Remarks": "caption"})

    for index, row in df.iterrows():
        Taxonomic_name = str(row['Taxonomic-name']).strip()
        df.loc[index, 'Taxonomic-name'] = Taxonomic_name
    df = df.rename(columns={"Taxonomic-name": "species"})
    df['FileReffernce'] = ''
    for index, row in df.iterrows():
        FileName = str(row['FileName']).strip()
        app = 'https://github.com/lperepol/Supplementary/blob/main/nematodes.myspecies.info/Images/'
        app = 'https://raw.githubusercontent.com/lperepol/Supplementary/main/nematodes.myspecies.info/Images/'
        FileName = app + FileName
        df.loc[index, 'FileReffernce'] = FileName

        species = str(row['species']).strip()
        splt = species.split(' ')
        if len(splt) > 1 :
            df.loc[index, 'genus'] = str(splt[0]).strip()
        www = len(splt)
        if len(splt) == 1 :
            df.loc[index, 'genus'] = species
            df.loc[index, 'species'] = ''


    df = df.rename(columns={"FileReffernce": "image_file"})
    df.drop('Join', axis=1, inplace=True)
    df.drop('Specimen', axis=1, inplace=True)
    df.drop('ID', axis=1, inplace=True)
    df.drop('Collection-code', axis=1, inplace=True)
    df.drop('Collector-number', axis=1, inplace=True)
    df.drop('Date-collected', axis=1, inplace=True)
    df.drop('Field-number', axis=1, inplace=True)
    df.drop('Type-status', axis=1, inplace=True)
    df.drop('Identified-by', axis=1, inplace=True)
    df.drop('Date-identified', axis=1, inplace=True)
    df.drop('Count', axis=1, inplace=True)
    df.drop('GenBank-number-s-', axis=1, inplace=True)
    df.drop('Location', axis=1, inplace=True)
    df.drop('Image', axis=1, inplace=True)
    df.drop('FileName', axis=1, inplace=True)
    df.drop('Field-notes', axis=1, inplace=True)
    fn = "nematodes_myspecies_info.csv"
    df.to_csv(fn, index=False)
    return df

def main():
    df1 = NormalizedBoldData()
    df2 = NormalizedUNLData()
    df3 = NormalizedWURData()
    df4 = nematodes_myspecies_info()
    df = pd.concat([df1, df2])
    df = pd.concat([df, df3])
    df = pd.concat([df, df4])
    fn = 'Concatinated.csv'
    df.to_csv(fn, index=False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()