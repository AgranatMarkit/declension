def main(value):
    import pymorphy2
    morph = pymorphy2.MorphAnalyzer()
    parse = morph.parse(value)

    forPrint = []

    for i in range(0,len(parse)):
        x = parse[i].lexeme
        for j in range(0,len(x)):
            if(forPrint.count(x[j][0])==0):
               forPrint.append(x[j][0])
               
    result = '\n'.join(forPrint)
    return result