from django.shortcuts import render
from basic.datas import *
from basic.defs import *
import random
sagilist=sagilist()
hisagilist=hisagilist()
# Create your views here.
def basic_template(request):
    return render(request,"basic.html")


def basic_form_show(request):
    return render(request,"basicresult.html")

def basic_form_show2(request):
    return render(request,"basicresult2.html")


def basic_form_show3(request):
    return render(request,"basicresult3.html")

def basic_form_show4(request):
    return render(request,"basicresult4.html")

def basic_form(request):
    
    S1=sagilist[0]
    S2=sagilist[1]
    S3=sagilist[2]
    S4=sagilist[3]
    S5=sagilist[4]
    S11=hisagilist[0]
    S12=hisagilist[1]
    S13=hisagilist[2]
    S14=hisagilist[3]
    S15=hisagilist[4]
    groupA=[S1,S2,S3,S4,S5,S11,S12,S13,S14,S15]
    random.shuffle(groupA)



    A1_result=groupA[0]
    A2_result=groupA[1]
    A3_result=groupA[2]
    A4_result=groupA[3]
    A5_result=groupA[4]
    A6_result=groupA[5]
    A7_result=groupA[6]
    A8_result=groupA[7]
    A9_result=groupA[8]
    A10_result=groupA[9]



    payload={
        'A1_result':A1_result,
        'A2_result':A2_result,
        'A3_result':A3_result,
        'A4_result':A4_result,
        'A5_result':A5_result,
        "A6_result":A6_result,
        "A7_result":A7_result,
        "A8_result":A8_result,
        "A9_result":A9_result,
        "A10_result":A10_result,
        }

    return render(request,'basicresult.html',payload)


def basic_form2(request):
    S1=sagilist[5]
    S2=sagilist[6]
    S3=sagilist[7]
    S4=sagilist[8]
    S5=sagilist[9]
    S11=hisagilist[5]
    S12=hisagilist[6]
    S13=hisagilist[7]
    S14=hisagilist[8]
    S15=hisagilist[9]
    groupA=[S1,S2,S3,S4,S5,S11,S12,S13,S14,S15]
    random.shuffle(groupA)




    A1_result=groupA[0]
    A2_result=groupA[1]
    A3_result=groupA[2]
    A4_result=groupA[3]
    A5_result=groupA[4]
    A6_result=groupA[5]
    A7_result=groupA[6]
    A8_result=groupA[7]
    A9_result=groupA[8]
    A10_result=groupA[9]



    payload={
        'A1_result':A1_result,
        'A2_result':A2_result,
        'A3_result':A3_result,
        'A4_result':A4_result,
        'A5_result':A5_result,
        "A6_result":A6_result,
        "A7_result":A7_result,
        "A8_result":A8_result,
        "A9_result":A9_result,
        "A10_result":A10_result,
        }

    return render(request,'basicresult2.html',payload)

def basic_form4(request):
    S1=A21()
    S2=A22()
    S3=A23()
    S4=A24()
    S5=A25()
    S11=A26()
    S12=A27()
    S13=A28()
    S14=A29()
    S15=A30()
    groupA=[S1,S2,S3,S4,S5,S11,S12,S13,S14,S15]
    random.shuffle(groupA)



    A1_result=groupA[0]
    A2_result=groupA[1]
    A3_result=groupA[2]
    A4_result=groupA[3]
    A5_result=groupA[4]
    A6_result=groupA[5]
    A7_result=groupA[6]
    A8_result=groupA[7]
    A9_result=groupA[8]
    A10_result=groupA[9]



    payload={
        'A1_result':A1_result,
        'A2_result':A2_result,
        'A3_result':A3_result,
        'A4_result':A4_result,
        'A5_result':A5_result,
        "A6_result":A6_result,
        "A7_result":A7_result,
        "A8_result":A8_result,
        "A9_result":A9_result,
        "A10_result":A10_result,
        }

    return render(request,'basicresult4.html',payload)
