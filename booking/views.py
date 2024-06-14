from django.shortcuts import render,redirect
import requests   
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialization import TaxiFareSerializer,Navigationdata,Carouseldata
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse

import requests
from .models import *
from rest_framework.decorators import api_view
class TaxiFareAPIView(APIView):
    def get(self, request):
        serializer = TaxiFareSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            url = "https://taxi-fare-calculator.p.rapidapi.com/search-geo"
            headers = {
                "X-RapidAPI-Key": "00dbe9f6fbmsh2e9eadc0a067640p18d2d8jsna36ab702d877",
                "X-RapidAPI-Host": "taxi-fare-calculator.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=data)
            return Response(response.json())
        return Response(serializer.errors, status=400)


class add_navigation_list(GenericAPIView,CreateModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def post(self,request):
        return self.create(request)
class Update_navigation_list(GenericAPIView,UpdateModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def put(self,request,**kwargs):
        return self.update(request, ** kwargs)
class Remove_navigation_list(GenericAPIView,DestroyModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def delete(self,request, **kwargs):
        return self.destroy(request, **kwargs)
class Table_navigation_list(GenericAPIView,RetrieveModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
class Navigationlist(GenericAPIView,ListModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def get(self,request):
        return self.list(request)
    

    
class add_carousel_list(GenericAPIView,CreateModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def post(self,request):
        return self.create(request)
class Update_carousel_list(GenericAPIView,UpdateModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def put(self,request,**kwargs):
        return self.update(request, ** kwargs)
class Remove_carousel_list(GenericAPIView,DestroyModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def delete(self,request, **kwargs):
        return self.destroy(request, **kwargs)
class Table_carousel_list(GenericAPIView,RetrieveModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
class Carousel_list(GenericAPIView,ListModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def get(self,request):
        return self.list(request)
    
def Carousel_home(request):
    carousel=Home_carousel.objects.all()
    return render(request,"carousel_home.html",{'carousel':carousel})
    
def Ticketbooking(request):
    return render(request,"ticketbooking.html")
def footer(request):
    return render(request,"footer.html")
def contactus(request):
    if request.method=="POST":
    
        Name=request.POST['Name']
        Phonenumber=request.POST['Phonenumber']
        Email=request.POST['Email']
        Message=request.POST['Message']
        Status=request.POST['Status']

        msg=Contact(Name=Name,Phonenumber=Phonenumber,Email=Email,Message=Message,Status=Status)
        msg.save()
        return redirect("/contactus")
    return render(request,"contact_form.html")

    
def contact_table(request):
    contact_info=Contact.objects.all()
    return render(request,"contact_table.html",{'contact_info':contact_info})
 
def teerdha_page(request):
    return render(request,"base.html")



    ####     navbar  ####

def navbar_page(request):
    if request.method=="POST":
        photo=request.FILES.get('photo')
        title=request.POST['title']
        url=request.POST['url']
        icon=request.POST['icon']
        nav=navbar(photo=photo, title=title, url=url, icon=icon)
        nav.save()
        return HttpResponse ("record is inserted")
    return render(request,"navbar_insert.html")

def navbar_table(request):
    if request.method=="GET":
       nav=navbar.objects.all()
    return render(request,"nav.html",{'nav':nav})


##...dashboard...##

def dashboard(request):
    return render(request,"admin.html")


def flightoffers_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dt=flights_offerscrudoperations(offer=offer, url=url)
        dt.save()
        return HttpResponse("submitted")
    return render(request,"dashboard_templates/flight_offer.html")

def flight_offertb(request):
    if request.method == "GET":
        up=flights_offerscrudoperations.objects.all()
    return render(request,"dashboard_templates/flight_offersupdate.html",{'up':up})
   
def busoffers_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dk=buses_offerscrudoperations(offer=offer, url=url)
        dk.save()
        return HttpResponse("submitted")
    return render(request,"dashboard_templates/flight_offer.html")

def buses_offertb(request):
    if request.method == "GET":
        op=buses_offerscrudoperations.objects.all()
    return render(request,"dashboard_templates/buses_offersupdate.html",{'op':op})

def caboffers_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dk=cabs_offerscrudoperations(offer=offer, url=url)
        dk.save()
        return HttpResponse("submitted")
    return render(request,"dashboard_templates/cabs_offer.html")

def cabs_offertb(request):
    if request.method == "GET":
        opt=cabs_offerscrudoperations.objects.all()
    return render(request,"dashboard_templates/cabs_offersupdate.html",{'opt':opt})

def hoteloffers_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dk=hotels_offerscrudoperations(offer=offer, url=url)
        dk.save()
        return HttpResponse("submitted")
    return render(request,"dashboard_templates/hotels_offer.html")

def hotels_offertb(request):
    if request.method == "GET":
        pt=hotels_offerscrudoperations.objects.all()
    return render(request,"dashboard_templates/hotels_offersupdate.html",{'pt':pt})