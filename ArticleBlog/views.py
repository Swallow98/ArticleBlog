from django.http import HttpResponse
import time
from django.template import Template

# def index(request):
#     return HttpResponse('hello world')
# def about(request,id):
#     nowtime = time.strftime('%Y:%m:%d %H:%M:%S')
#     return HttpResponse(nowtime)
# def indexhtml(request):
#     # 写一个html
#     html = '''
#     <html>
#         <head></head>
#         <bady>
#         <h1>index页面</h1>
#         </bady>
#     </html>
#     '''
#     return HttpResponse(html)

from django.template.loader import get_template
def getindex(request,age):
#     # 返回页面
#     # 1
#     # 创建模板对象
    template_obj = get_template('indexhtml.html')
#     # 渲染
    params = {'name':'杨凯','age':age}
#     # 创建返回对象
    result = template_obj.render(params)
    return HttpResponse(result)

from django.shortcuts import render_to_response
def get_index(request):
#     # 第一个参数是要返回的页面
#     # 第二个参数
    return render_to_response('indexhtml.html')

from django.shortcuts import render
import random
def getIndex(request):
    # 第三种
    # 第一个参数是函数形参，
    # 第二个参数是要返回的页面
    num = random.randint(1,30)
    parmas = {'name':'杨凯','age':num}
    return render(request,'indexhtml.html',parmas)

def template(request):
    # 返回数据
    name = '杨凯'
    age = 24
    hobby = ['吃','睡','喝']
    # score = {'吃':40,'睡':50,'喝':100}
    # return render_to_respondwse('template.html',{"name":name,"age":age})
    # locals()会将所有的局部变量作为字典返回
    return render_to_response('template.html',locals())

def statica(request):
    return render_to_response('static.html')

def about(request):
    return render_to_response('about.html')

def index(request):
    return render_to_response('index.html')
def listpic(request):
    return render_to_response('listpic.html')
def newslistpic(request):
    return render_to_response('newslistpic.html')


