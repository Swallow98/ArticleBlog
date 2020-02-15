from django.shortcuts import render
from django.http import HttpResponse
from .models import Type

# Create your views here.

def Add_Type(request):
    # 增加  save
    # 第一种
    type = Type()
    type.id=1
    type.name = 'A3'
    type.description = '手机'
    type.save()
    #
    # # 第二种
    type = Type(id=2,name='A4',description='新版手机')
    type.save()
    #
    # # create
    # # 第一种
    Type.objects.create(name='A5',description='新版手机2')
    #
    # # 第二种  字典
    dic = dict(name='A6',description='新版手机3')
    Type.objects.create(**dic) #**解包

    return HttpResponse('type.Add_Type')

def Select_Type(request):

    # all
    # type = Type.objects.all()
    # print(type)
    # for i in type:
    #     print(i)
    #     print(i.name)

    # get
    # type = Type.objects.get(id = 1)
    # print(type)

    # filter
    # type = Type.objects.filter(name= 'A5')
    # print(type[0].name)

    # exclude
    # type = Type.objects.exclude(name= 'A5')
    # for i in type:
        # print(i.description)

    # order_by
    # type = Type.objects.order_by('name')
    # type1 = Type.objects.order_by('-name')

    # print(type)
    # print(type1)

    # reverse
    # type = Type.objects.reverse()
    # type1 = Type.objects.order_by('name').reverse()
    # print(type)
    # print(type1)

    # values
    # type = Type.objects.values()
    # print(type)

    # count
    # type = Type.objects.count()
    # print(type)

    # exists
    # type = Type.objects.filter(name= 'A4').exists()
    # print(type)



    return HttpResponse('select_Type')



