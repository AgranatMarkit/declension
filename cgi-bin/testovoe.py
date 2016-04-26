def main(value):
    import pymorphy2
    morph = pymorphy2.MorphAnalyzer()
    parse = morph.parse(value)

##    for i in parse.lexeme:
##        print(i[0])

    forPrint = []

    for i in range(0,len(parse)):
        x = parse[i].lexeme
        #print(x)
        for j in range(0,len(x)):
            if(forPrint.count(x[j][0])==0):
               forPrint.append(x[j][0])
            #print(x[j][0])
    
##    for i in forPrint:
##        print(i)
    result = '\n'.join(forPrint)
    return result