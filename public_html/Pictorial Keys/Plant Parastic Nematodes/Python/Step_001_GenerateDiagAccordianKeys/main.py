import pandas as pd
def readTemplate():
    accordian = ""
    fn = 'AccordianKeyTemplate.html'
    with open(fn) as f:
        accordian = f.read()
    return accordian

def readKeys():
    fn = '../../../../Identification_keys_redo/Miai Mullin.xlsx'
    df = pd.read_excel(fn, sheet_name='Miai Mullin')
    return df

    #fn = '../../../../Identification_keys_redo/Miai Mullin.xlsx'
    #f = open(fn, "w")
    #f.write("Woops! I have deleted the content!")
    #f.close()


def write_key(htmltemplate, key, valuesList):
    htmltemplate = str(htmltemplate)
    keystr = str(key).zfill(3)
    fn = '../../Key/AccordianKey_' + keystr + '.html'
    with open(fn,"w", encoding="utf-8") as f:
        tempTemplate = htmltemplate.replace('[KEY]', keystr)
        lll = len(valuesList)
        tempTemplate = tempTemplate.replace('[Accordion Item #1]', valuesList[0])
        if lll > 1:
            tempTemplate = tempTemplate.replace('[Accordion Item #2]', valuesList[1])
        if lll > 2:
            tempTemplate = tempTemplate.replace('[Accordion Item #3]', valuesList[2])
        f.write(tempTemplate)


def main():
    df = readKeys()
    lis = list()
    keyDict = dict()
    for index, row in df.iterrows():
        KeyFrom = row['KeyFrom']
        Description = row['Description']
        if KeyFrom in keyDict:
            keyDict[KeyFrom].append(Description)
        else:
            keyDict[KeyFrom] = list()
            keyDict[KeyFrom].append(Description)

    htmltemplate = readTemplate()
    for key in keyDict:
        write_key(htmltemplate,key, keyDict[key])


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")




