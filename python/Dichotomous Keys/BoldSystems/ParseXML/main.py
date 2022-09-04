import pandas as pd
import openpyxl
import xml.etree.ElementTree as ET
import xmltodict
import os
class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class XmlDictConfig(dict):
    '''
    Example usage:

    >>> tree = ElementTree.parse('your_file.xml')
    >>> root = tree.getroot()
    >>> xmldict = XmlDictConfig(root)

    Or, if you want to use an XML string:

    >>> root = ElementTree.XML(xml_string)
    >>> xmldict = XmlDictConfig(root)

    And then use xmldict for what it is... a dict.
    '''
    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
            if element:
                # treat like dict - we assume that if the first two tags
                # in a series are different, then they are all different.
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})

def get_taxonomy(record):

    for taxonomy in record.findall('taxonomy'):
        for elem in taxonomy.iter():
            if (elem.tag == 'name'):
                return(elem.text)
                print(elem.tag, elem.text)




def get_images(record ):
    imagesLst = list()
    for specimen_imagery in record.findall('specimen_imagery'):
        for media in specimen_imagery.findall('media'):
            for elem in media.iter():
                imagesLst.append((elem.tag, elem.text))

    return imagesLst


def readXML():
    fn = '../Bold_data/AllNematodeTaxa.xml'
    mytree = ET.parse(fn)
    myroot = mytree.getroot()
    cnt = 0
    img_cnt = 0
    nemaDict = dict()
    for record in myroot.findall('record'):
        record_id = record.find('record_id').text
        #if not record_id == '4357385':
        #    continue
        #if not record_id == '7009663': # Croco
        #    continue
        #if not record_id == '13628106': # other
        #    continue
        #if not record_id == '1703314': # other
        #    continue
        #if not record_id == '2455105': # other
        #    continue
        #if not record_id == '12184390': # other
        #    continue


        xmldict = XmlDictConfig(record)
        nemaDict[record_id] = xmldict
    return nemaDict

def print_xml(nemaDict):
    for i in nemaDict:
        print('*************************************************************')
        print (nemaDict[i]['record_id'])
        print (nemaDict[i]['processid'])
        print (nemaDict[i]['specimen_identifiers'])

        #print (nemaDict[i]['taxonomy']['phylum']['taxon']['name'])
        phylum =''
        if ('phylum' in nemaDict[i]['taxonomy']) :
            print (nemaDict[i]['taxonomy']['phylum']['taxon']['name'])
        else:
            print(phylum)

        #print (nemaDict[i]['taxonomy']['class']['taxon']['name'])
        aclass =''
        if ('class' in nemaDict[i]['taxonomy']) :
            print (nemaDict[i]['taxonomy']['class']['taxon']['name'])
        else:
            print(aclass)

        #print (nemaDict[i]['taxonomy']['order']['taxon']['name'])
        order =''
        if ('order' in nemaDict[i]['taxonomy']) :
            print (nemaDict[i]['taxonomy']['order']['taxon']['name'])
        else:
            print(aclass)

        #print (nemaDict[i]['taxonomy']['family']['taxon']['name'])
        family =''
        if ('family' in nemaDict[i]['taxonomy']) :
            print (nemaDict[i]['taxonomy']['family']['taxon']['name'])
        else:
            print(family)


        #print (nemaDict[i]['taxonomy']['genus']['taxon']['name'])
        genus =''
        if ('genus' in nemaDict[i]['taxonomy']) :
            print (nemaDict[i]['taxonomy']['genus']['taxon']['name'])
        else:
            print(genus)

        species =''
        if ('species' in nemaDict[i]['taxonomy']) :
            print (nemaDict[i]['taxonomy']['species']['taxon']['name'])
        else:
            print(species)

        if 'specimen_desc' in nemaDict[i]:
            sex = ""
            if 'sex' in nemaDict[i]['specimen_desc']:
                print (nemaDict[i]['specimen_desc']['sex'])
            else:
                print(sex)
            #print (nemaDict[i]['specimen_desc']['lifestage'])
            lifestage = ""
            if 'lifestage' in nemaDict[i]['specimen_desc']:
                print (nemaDict[i]['specimen_desc']['lifestage'])
            else:
                print(lifestage)

            if ('coordinates' in nemaDict[i]['collection_event']):
                print (nemaDict[i]['collection_event']['coordinates']['lat'])
                print (nemaDict[i]['collection_event']['coordinates']['lon'])
            site_code = ''
            if ('site_code' in nemaDict[i]['collection_event']) :
                print (nemaDict[i]['collection_event']['site_code'])
            else:
                print(site_code)

        #print (nemaDict[i]['specimen_imagery']['media'])
        if 'specimen_imagery' in nemaDict[i]:
            foo = nemaDict[i]['specimen_imagery']['media']
            if isinstance(foo, XmlListConfig):
                print ('is XmlListConfig')
                for i in foo:
                    caption=''
                    print('Caption')
                    if ('caption' == i ):
                        print (i['caption'])
                    else:
                        print (caption)
                    #print (i['media_descriptor'])
                    media_descriptor=''
                    if ('media_descriptor' in i ):
                        print (i['media_descriptor'])
                    else:
                        print (media_descriptor)
                    #print(i['image_file'])
                    image_file=''
                    if ('image_file' in i ):
                        print (i['image_file'])
                    else:
                        print (image_file)
                    #print(i['copyright'])
                    if 'copyright' in i:
                        copyright_institution=''
                        if ('copyright_institution' in i['copyright'] ):
                            print(i['copyright']['copyright_institution'])
                        else:
                            print (copyright_institution)
                    #print(i['photographer'])
                    photographer=''
                    if ('photographer' in i ):
                        print (i['photographer'])
                    else:
                        print (photographer)
            else:
                caption = ''
                if ('caption' in  foo):
                    print(foo['caption'])
                else:
                    print(caption)

                media_descriptor = ''
                if ('media_descriptor' in foo):
                    print(foo['media_descriptor'])
                else:
                    print(media_descriptor)
                image_file = ''
                if ('image_file' in foo):
                    print(foo['image_file'])
                else:
                    print(image_file)
                # print(i['copyright'])
                if 'copyright' in foo:
                    copyright_institution = ''
                    if ('copyright_institution' in foo['copyright']):
                        print(foo['copyright']['copyright_holder'])
                    else:
                        print(copyright_institution)
                # print(i['photographer'])
                photographer = ''
                if ('photographer' in foo):
                    print(foo['photographer'])
                else:
                    print(photographer)

def write_xml_to_csv(nemaDict):
    f = open("../Bold_data/BoldSystems.csv", "w")
    header = 'record_id,processid,specimen_identifiers,identification_method,'
    header = header + 'phylum,class,order,family,genus,species,'
    header = header + 'sex,lifestage,lat,lon,site_code,caption,media_descriptor,image_file,copyright_institution,'
    header = header + 'photographer'
    header = header + ''
    header = header + ''
    f.write(header + '\n')
    for i in nemaDict:
        line = ''
        print('*************************************************************')
        line = line + str(nemaDict[i]['record_id'])
        line = line + str(',')
        line = line + str(nemaDict[i]['processid'])
        line = line + str(',')
        line = line + str(nemaDict[i]['specimen_identifiers']['sampleid'])
        line = line + str(',')

        if 'identification_method' in nemaDict[i]['taxonomy']:
            line = line + '"' + str(nemaDict[i]['taxonomy']['identification_method'] + '"' )
        line = line + str(',')

            #print (nemaDict[i]['taxonomy']['phylum']['taxon']['name'])
        phylum =''
        if ('phylum' in nemaDict[i]['taxonomy']) :
            line = line + str(nemaDict[i]['taxonomy']['phylum']['taxon']['name'])
        else:
            line = line + str(phylum)
        line = line + str(',')

        #print (nemaDict[i]['taxonomy']['class']['taxon']['name'])
        aclass =''
        if ('class' in nemaDict[i]['taxonomy']) :
            line = line + str(nemaDict[i]['taxonomy']['class']['taxon']['name'])
        else:
            line = line + str(aclass)
        line = line + str(',')

        #print (nemaDict[i]['taxonomy']['order']['taxon']['name'])
        order =''
        if ('order' in nemaDict[i]['taxonomy']) :
            line = line + str(nemaDict[i]['taxonomy']['order']['taxon']['name'])
        else:
            line = line + str(aclass)
        line = line + str(',')

        #print (nemaDict[i]['taxonomy']['family']['taxon']['name'])
        family =''
        if ('family' in nemaDict[i]['taxonomy']) :
            line = line + str(nemaDict[i]['taxonomy']['family']['taxon']['name'])
        else:
            line = line + str(family)
        line = line + str(',')


        #print (nemaDict[i]['taxonomy']['genus']['taxon']['name'])
        genus =''
        if ('genus' in nemaDict[i]['taxonomy']) :
            line = line + str(nemaDict[i]['taxonomy']['genus']['taxon']['name'])
        else:
            print(genus)
        line = line + str(',')

        species =''
        if ('species' in nemaDict[i]['taxonomy']) :
            line = line + str(nemaDict[i]['taxonomy']['species']['taxon']['name'])
        else:
            line = line + str(species)
        line = line + str(',')

        if 'specimen_desc' in nemaDict[i]:
            sex = ""
            if 'sex' in nemaDict[i]['specimen_desc']:
                line = line + str(nemaDict[i]['specimen_desc']['sex'])
            else:
                line = line + str(sex)
            line = line + str(',')
            #print (nemaDict[i]['specimen_desc']['lifestage'])
            lifestage = ""
            if 'lifestage' in nemaDict[i]['specimen_desc']:
                line = line + str(nemaDict[i]['specimen_desc']['lifestage'])
            else:
                line = line + str(lifestage)
            line = line + str(',')

            if ('coordinates' in nemaDict[i]['collection_event']):
                line = line + str(nemaDict[i]['collection_event']['coordinates']['lat'])
                line = line + str(',')
                line = line + str(nemaDict[i]['collection_event']['coordinates']['lon'])
                line = line + str(',')
            else:
                line = line + str(',')
                line = line + str(',')

            site_code = ''
            tmp = ''
            if ('site_code' in nemaDict[i]['collection_event']) :
                tmp =  str(nemaDict[i]['collection_event']['site_code'])
                line = line + str(nemaDict[i]['collection_event']['site_code'])
            else:
                line = line + str(site_code)
            line = line + str(',')
        else:
            line = line + str(',')
            line = line + str(',')
            line = line + str(',')
            line = line + str(',')
            line = line + str(',')

        #print (nemaDict[i]['specimen_imagery']['media'])
        if 'specimen_imagery' in nemaDict[i]:
            foo = nemaDict[i]['specimen_imagery']['media']
            repeatline = line
            if isinstance(foo, XmlListConfig):
                print ('is XmlListConfig')
                lineCnt = 0
                for i in foo:
                    line = repeatline
                    caption=''
                    print('caption')
                    if ('caption' in i ):
                        line = line + '"' + str(i['caption'] + '"')
                    else:
                        line = line + str(caption)
                    line = line + str(',')
                    #print (i['media_descriptor'])
                    media_descriptor=''
                    if ('media_descriptor' in i ):
                        line = line + str(i['media_descriptor'])
                    else:
                        line = line + str(media_descriptor)
                    line = line + str(',')
                    #print(i['image_file'])
                    image_file=''
                    if ('image_file' in i ):
                        line = line + str(i['image_file'])
                    else:
                        line = line + str(image_file)
                    line = line + str(',')
                    #print(i['copyright'])
                    copyright_institution = ''
                    if 'copyright' in i:
                        if ('copyright_institution' in i['copyright'] ):
                            line = line + '"' + str(i['copyright']['copyright_institution']  + '"' )
                        else:
                            line = line + str(copyright_institution)
                    line = line + str(',')
                    #print(i['photographer'])
                    photographer=''
                    if ('photographer' in i ):
                        line = line + '"' + str(i['photographer'] + '"')
                    else:
                        line = line + str(photographer)
                    line = line + '\n'
                    f.write(line)
                    lineCnt = lineCnt +1

            else:
                caption = ''
                tmp =''
                if ('caption' in  foo):
                    tmp = foo['caption']
                    line = line + '"' + str(foo['caption'] + '"'  )
                else:
                    line = line +  str(caption)

                line = line + str(',')

                media_descriptor = ''
                if ('media_descriptor' in foo):
                    line = line + str(foo['media_descriptor'])
                else:
                    line = line + str(media_descriptor)
                line = line + str(',')
                image_file = ''
                if ('image_file' in foo):
                    line = line + str(foo['image_file'])
                else:
                    line = line + str(image_file)
                line = line + str(',')
                # print(i['copyright'])
                if 'copyright' in foo:
                    copyright_institution = ''
                    if ('copyright_institution' in foo['copyright']):
                        line = line +  '"' + str(foo['copyright']['copyright_holder'] + '"' )
                    else:
                        line = line + str(copyright_institution)
                line = line + str(',')
                # print(i['photographer'])
                photographer = ''
                if ('photographer' in foo):
                    line = line + '"' + str(foo['photographer']+ '"')
                else:
                    line = line + str(photographer)
                line = line + '\n'
                f.write(line )

    f.close()

def read_write_csv():
    fn = "../Bold_data/BoldSystems.csv"
    df = pd.read_csv(fn)
    df = df.fillna('')
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



def main():
    # Use a breakpoint in the code line below to debug your script.
    nemaDict = readXML()
    print('*************************************************************')
    print(nemaDict)
    print('*************************************************************')
    print('*************************************************************')
    print_xml(nemaDict)
    write_xml_to_csv(nemaDict)
    print(os.getcwd())
    read_write_csv()
    #print (nemaDict)
    #xx= 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()