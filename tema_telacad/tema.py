def job3dejob (a):
    x=list()
    for i in range(3):
        maxi = 0
        for y,z in a.items():
            if(z>maxi):
                aux=y
                maxi=z
        x.append(aux)
        del a[aux]
    return x


g = open('test_file', mode='rt', encoding='utf-8')

x = g.readlines()

dictionar={'average_age':0, 'best_paid_job':0, 'best_paid_employee':0, 'no_employees':0, 'top_3_jobs':0, 'no_seniors':0, 'no_middle':0, 'no_juniors':0}
best3jobs={}
sal_job_max=0

for i in x:
    i=i.split("\t")
    i[4]=i[4].rstrip()
    i[1]=int(i[1])
    i[3]=int(i[3])
    i[4]=int(i[4])
    dictionar['average_age']+=i[1]
    dictionar['no_employees']+=1

    if i[3]>sal_job_max:
        dictionar['best_paid_job']=i[2]
        dictionar['best_paid_employee']=i[0]
        sal_job_max=i[3]

    if i[2] not in best3jobs:
        best3jobs.update({i[2]:1})
    else:
        best3jobs[i[2]]+=1

    if i[4]>5:
        dictionar['no_seniors']+=1
    else:
        if i[4]<3:
            dictionar['no_juniors']+=1
        else:
            dictionar['no_middle']+=1


dictionar['top_3_jobs']=job3dejob(best3jobs)
dictionar['average_age']=float(dictionar['average_age'])/dictionar['no_employees']

print("{")
for a,b in dictionar.items():
    print("\t'{key}': {value},".format(key=a, value=b))
print("}")