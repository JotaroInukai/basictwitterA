from django.shortcuts import render
from basic.datas import *
from basic.defs import *
import random
import functools
@functools.lru_cache()
def func():
    
    sagilistA=sagilist()
    hisagilistA=hisagilist()
    
    return [sagilistA,hisagilistA]
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
    function=func()

    S1=function[0][0]
    S2=function[0][1]
    S3=function[0][2]
    S4=function[0][3]
    S5=function[0][4]
    S11=function[1][0]
    S12=function[1][1]
    S13=function[1][2]
    S14=function[1][3]
    S15=function[1][4]
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
    function=func()
    S1=function[0][5]
    S2=function[0][6]
    S3=function[0][7]
    S4=function[0][8]
    S5=function[0][9]
    S11=function[1][5]
    S12=function[1][6]
    S13=function[1][7]
    S14=function[1][8]
    S15=function[1][9]
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
    function=func()
    S1=function[0][10]
    S2=function[0][11]
    S3=function[0][12]
    S4=function[0][13]
    S5=function[0][14]
    S11=function[1][10]
    S12=function[1][11]
    S13=function[1][12]
    S14=function[1][13]
    S15=function[1][14]
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

