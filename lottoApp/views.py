from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    lines=request.GET['lottoLines']
    linecount=int(lines)
    linesList=list(range(0,linecount))
    lottoList=[[] for row in range(0,linecount)]
    for i in range(0,linecount):
        randList=list(range(1,46))
        for a in range(0,6):
            num=random.randint(0,len(randList)-1)
            lottoList[i].append(randList[num])
            del randList[num]
        

    return render(request, 'result.html',{"count":lines,"lottoResult":lottoList,"lines":linesList})