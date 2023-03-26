# -*- coding: utf-8 -*-

import yaml

# Function - concatLocLst
def concatLocLst(locLst):
    ret = ''
    for loc in locLst:
        ret += loc
    if (ret.endswith('/')):
        ret = ret[:len(ret)-1]
    return ret

# Function - printCI
def printCI(locLst, elements):
    for element in elements:
        if (type(element) == dict):
            # print name and type
            nameVal = element.get('name')
            typeVal = element.get('type')
            if (nameVal != None and typeVal != None):
                print(concatLocLst(locLst) + "\t" + nameVal + "\t" + typeVal)
            
            # if a type of the element is a 'list',
            # then call the function recursively.
            for delem in element.values():
                thisLocLst = locLst.copy()
                if (type(delem) == list):
                    dirVal = element.get('directory')
                    nameVal = element.get('name')
                    if (dirVal != None):
                        thisLocLst.append(dirVal + '/')
                    elif (nameVal != None):
                        thisLocLst.append(nameVal + '/')
                    printCI(thisLocLst, delem)

# main
if __name__ == "__main__":

    # open yaml file
    f = open("infra.yaml", "r+")

    # parse yaml
    data = yaml.load(f)

    # traverse yaml tree
    locLst = []
    printCI(locLst, data['spec'])
