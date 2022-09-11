import pandas as pd
def readTemplate():
    accordian = ""
    fn = 'Template_001.html'
    with open(fn) as f:
        accordian = f.read()
    return accordian

def readKeys():
    fn = '../../../../Dichotomous Keys/Key to Plant Parasitic Nematodes Miai Mullin/Miai Mullin.xlsx'
    df = pd.read_excel(fn, sheet_name='Sheet1')
    return df



def write_key(htmltemplate, key, valuesList,backKeyDict):
    htmltemplate = str(htmltemplate)
    keystr = str(key).zfill(3)
    fn = '../../Keys/Key_' + keystr + '.html'
    fn = '../../Keys/Key_' + keystr + '.html'
    backKeyStr = ''
    if key in backKeyDict:
        backKey = backKeyDict[key]
        backKeyStr = str(backKeyDict[key]).zfill(3)
    with open(fn,"w", encoding="utf-8") as f:
        tempTemplate = htmltemplate.replace('[Key]', keystr)
        lll = len(valuesList)
        tempTemplate = tempTemplate.replace('[Accordion Item #1]', valuesList[0][0])
        ttt= 'accordioncollapse-1-' + keystr
        tempTemplate = tempTemplate.replace('[accordioncollapseOne001-image-target]', ttt)
        target = 'Previous <a href="/Pictorial%20Keys/Fresh%20Water%20Nematodes/Keys/Key_001.html">001</a>'
        replaceStr = 'Previous <a href="/Pictorial%20Keys/Plant%20Parastic%20Nematodes/Keys/Key_' + backKeyStr + '.html">' + backKeyStr + '</a>'
        tempTemplate = tempTemplate.replace(target, replaceStr)

        toKeystr = str(valuesList[0][1])
        if toKeystr.isdigit():
            toKeystr = str(valuesList[0][1]).zfill(3)
            target = 'Next <a href="/Pictorial%20Keys/Fresh%20Water%20Nematodes/Keys/Key_002.html">002</a>'
            replaceStr = 'Next <a href="/Pictorial%20Keys/Plant%20Parastic%20Nematodes/Keys/Key_' + toKeystr + '.html">' + toKeystr + '</a>'
            tempTemplate = tempTemplate.replace(target, replaceStr)
        else:
            target = 'Next <a href="/Pictorial%20Keys/Fresh%20Water%20Nematodes/Keys/Key_002.html">002</a>'
            replaceStr = ' Remove '
            tempTemplate = tempTemplate.replace(target, replaceStr)

        if lll > 1:
            tempTemplate = tempTemplate.replace('[Accordion Item #2]', valuesList[1][0])
            ttt= 'accordioncollapse-2-' + keystr
            tempTemplate = tempTemplate.replace('[accordioncollapseTwo001-image-target]', ttt)

            toKeystr = str(valuesList[1][1])
            if toKeystr.isdigit() :
                toKeystr = str(valuesList[1][1]).zfill(3)
                target = 'Next <a href="/Pictorial%20Keys/Fresh%20Water%20Nematodes/Keys/Key_003.html">003</a>'
                replaceStr = 'Next <a href="/Pictorial%20Keys/Plant%20Parastic%20Nematodes/Keys/Key_' + toKeystr + '.html">' + toKeystr + '</a>'
                tempTemplate = tempTemplate.replace(target, replaceStr)
            else :
                target = 'Next <a href="/Pictorial%20Keys/Fresh%20Water%20Nematodes/Keys/Key_003.html">003</a>'
                replaceStr = ' Remove '
                tempTemplate = tempTemplate.replace(target, replaceStr)


        if lll > 2:
            tempTemplate = tempTemplate.replace('[Accordion Item #3]', valuesList[2][0])
            ttt = 'accordioncollapse-3-' + keystr
            tempTemplate = tempTemplate.replace('[accordioncollapseThree001-image-target]', ttt)
            toKeystr = str(valuesList[2][1])
            if toKeystr.isdigit() :
                toKeystr = str(valuesList[2][1]).zfill(3)
                target = 'Next <a href="/Pictorial%20Keys/Fresh%20Water%20Nematodes/Keys/Key_004.html">004</a>'
                replaceStr = 'Next <a href="/Pictorial%20Keys/Plant%20Parastic%20Nematodes/Keys/Key_' + toKeystr + '.html">' + toKeystr + '</a>'
                tempTemplate = tempTemplate.replace(target, replaceStr)
            else :
                target = 'Next <a href="/Pictorial%20Keys/Fresh%20Water%20Nematodes/Keys/Key_004.html">004</a>'
                replaceStr = ' Remove '
                tempTemplate = tempTemplate.replace(target, replaceStr)
        f.write(tempTemplate)


def main():
    df = readKeys()
    lis = list()
    fromDict = dict()
    backKey = dict()
    for index, row in df.iterrows():
        From = row['From']
        To = row['To']
        backKey[To] = From
        Description = row['Key To Plant Parasitic Nematodes, Miai, Mullin (1975)']
        tup = (Description, To)
        if From in fromDict:
            fromDict[From].append(tup)
        else:
            fromDict[From] = list()
            fromDict[From].append(tup)

    htmltemplate = readTemplate()
    count = 0
    for key in fromDict:
        write_key(htmltemplate,key, fromDict[key], backKey)
        if count > 100:
            break
        count = count + 1


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")




