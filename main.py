import csv


def keywordreader(keyword):
    companies = []

    file = open('output.csv')
    type(file)

    csvreader = csv.reader(file)

    final = []

    rows = []

    for row in csvreader:
        rows.append(row)

    for i in rows:

        li = i[1].split()

        for j in range(0, len(li)):
            li[j] = li[j].replace(",", "")
            li[j] = li[j].replace(".", "")
            li[j] = li[j].replace(";", "")

        if li.count(keyword) > 0:
            companies.append(i)

    newarr = []
    for i in companies:

        newarr.append(float(i[4]))

    newarr.sort()

    for i in newarr:
        for j in companies:
            if j[4] == str(i):

                final.insert(0, j)
                companies.remove(j)

    file.close()

    return final


""" inp = input('What is your prefered industry: ')
out = keywordreader(inp)

print(out) """

def sentencekeywordreader(sentence):
    companies=[]

    keywords=sentence.split()
    for i in range(0,len(keywords)):
        keywords[i]=keywords[i].capitalize()
        keywords[i]=keywords[i].replace(",","")
        keywords[i]=keywords[i].replace(".","")
        keywords[i]=keywords[i].replace(";","")

    
    file = open('output.csv')
    type(file)

    csvreader = csv.reader(file)

    final=[]

    rows = []

    for row in csvreader:
        rows.append(row)

   

    for i in rows:
        
        li=i[1].split()
        
        for j in range(0,len(li)):
            li[j]=li[j].replace(",","")
            li[j]=li[j].replace(".","")
            li[j]=li[j].replace(";","")

        for k in keywords:
            
            if li.count(k)>0:
                if companies.count(i)==0:
                    companies.append(i)
        
    
    

    
            

    newarr=[]
    for i in companies:
        
        newarr.append(float(i[4]))

    newarr.sort()

 
    
    for i in newarr:
        for j in companies:
            if j[4] == str(i):
                
            
                final.insert(0,j)
                companies.remove(j)

    file.close()

    return final
