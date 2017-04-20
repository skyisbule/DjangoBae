#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms

def add(req):
   num=open('num').read()
   f=open("num",'w')
   now=int(num)+1
   f.write(str(now))
   f.close()
   if req.method == 'POST':
      boy=req.POST['boy']
      girl=req.POST['girl']
      time=req.POST['time']
      res='/love?b='+boy+'&g='+girl+'&t='+time
      res=res.encode('UTF-8')
      return HttpResponseRedirect(res)
   else:
      return render_to_response('index.html',{'num':num},context_instance=RequestContext(req))

def love(req):
    num=open('num').read()
    f=open("num",'w')
    now=int(num)+1
    f.write(str(now))
    f.close()
    boy=req.GET['b']
    gril=req.GET['g']
    time=req.GET['t']
    boy=boy.encode('utf-8')
    gril=gril.encode('utf-8')
    return render_to_response('love.html',{'boy':boy,'girl':gril,'time':time})
