# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph
import pandas as pd
import openpyxl

def fixup(df):
    df = df.fillna(0)
    for index, row in df.iterrows():
        Description = str(row['Description']).strip()
        df.loc[index, 'Description'] = Description
    return df
def readSpreadSheet():
    fn = 'Key to Families of Plant and Soil Nematodes.xlsx'
    df = pd.read_excel(fn, sheet_name='Sheet1')
    df = df.fillna('')
    #df = fixup(df)
    #fn = '../../Bongers_Most_Common_Genera.csv'
    #df.to_csv(fn, index=False)

    return df

def label2(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 3]) for i in range(0, len(words), 3)]
    str = ""
    for i in grouped_words:
        str = str + i + "\n"
    return str

def getFamilyNames(df, g):

    for index, row in df.iterrows():
        KeyTo = str(row['KeyTo']).strip()
        Description = str(row['Description']).strip()
        if not KeyTo.isdigit():
            g.node(KeyTo, KeyTo,fillcolor='aqua',style="filled", shape='hexagon' )
    return g
#        Description = str(row['Description Rewrite']).strip()
#        place = row['place']
#        for item in id_to_place:
#            if item == id:  # this line changed
#                df.loc[index, 'place'] = id_to_place[item]


def draw(df):
    GraphTitle = 'Families of\nPlant and Soil\n Nematodes Howard\n Ferris February 2011'
    g = Digraph('GraphTitle', comment="FOO",filename = 'NematodaKey.gv') #, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    g.graph_attr['rankdir'] = 'LR'
    g.graph_attr['remincross'] = 'True'
    g.attr(label=GraphTitle)

    g = getFamilyNames(df,g)

    for index, row in df.iterrows():
        KeyFrom = str(row['KeyFrom'])
        KeyTo = str(row['KeyTo']).strip()

        if KeyTo.isdigit():
            KeyTo = KeyTo.zfill(3)
        if KeyFrom.isdigit():
            KeyFrom = KeyFrom.zfill(3)

        Description = str(row['Description']).strip()
        g.edge(label2(KeyFrom),label2(KeyTo), label2(Description))


    g.render('NematodaKey.gv', format='svg', view=True)
    g.render('NematodaKey.gv', format='jpg', view=False)
    g.render('NematodaKey.gv', format='pdf', view=False)


    #g.node('', '',fillcolor='aqua',style="filled" )
    #g.edge('','', label2('')
    #g.edge('','', label2('')


def main():
    # Use a breakpoint in the code line below to debug your script.
    df = readSpreadSheet()
    draw(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
