from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import redirect
from . forms import Userform
from. forms1 import Policeform
from. forms2 import Hospitalform
from. forms3 import loginform
from. forms4 import UserMissingform
from . models import Users,Station1,Hospitals,Login
from .models1 import Usermissingadds
from.models2 import Accidents
from.forms5 import Accidentform
from.models3 import Casesheet
from. forms6 import Casesheet1
from.models4 import Enquiry
from. forms7 import Enquiryform,Replyform
from django.utils import timezone
from datetime import date
from .models5 import Complaint
from .forms8 import ComplaintForm
from django.db.models import Max
from django.shortcuts import get_object_or_404
from.models6 import Public_Enquiry
from.forms9 import Public_Enquiryform,Public_Replyform
from.models7 import Missing_found
from.forms10 import Found
from django.db.models import F
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import cv2
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('punkt')
nltk.download('vader_lexicon')



# Create your views here.
def admin(request):
    template=loader.get_template('adminindex.html')
    return render(request,'adminindex.html')

    
def Index(request):
    template=loader.get_template('index.html')
    return render(request,'index.html')

def userIndex(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('index')
    try:
        user = Users.objects.get(pk=user_id)
        return render(request, 'userindex.html', {'ser': user})  # Use pk instead of id
    except Users.DoesNotExist:
        return redirect('index')


def policeindex(request):
    Station_id = request.session.get('Station_id')
    if not Station_id:
        return redirect('index')
    try:
        user = Station1.objects.get(pk=Station_id)
        return render(request, 'policeindex.html', {'ser': user})  # Use pk instead of id
    except Station1.DoesNotExist:
        return redirect('index')



def hospital_index(request):
    hospital_id = request.session.get('hospital_id')
            
    if not hospital_id:
        return redirect('index')
        
    try:
        user = Hospitals.objects.get(pk=hospital_id)
        return render(request, 'hospitalindex.html', {'ser': user})  # Use pk instead of id
    except Hospitals.DoesNotExist:
        return redirect('index')
   

def loginindex(request):
    template=loader.get_template('loginindex.html')
    return render(request,'loginindex.html')



def useradd(request):
    
    if request.method=='POST':
        fm=Userform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('Useradd')
    else:
        fm=Userform()
    return render(request,'Useradd.html',{'form1':fm})

# def useradd(request):
#     if request.method == 'POST':
#         fm = Userform(request.POST)
#         if fm.is_valid():
#             phone = fm.cleaned_data['Phone']
#             password = fm.cleaned_data['Password']
            
#             # Perform server-side validation for phone number
#             if not phone.isdigit() or len(phone) != 10:
#                 fm.add_error('Phone', 'Invalid phone number. Please enter a 10-digit numeric phone number.')
#                 return render(request, 'Useradd.html', {'form1': fm})
            
#             # Perform server-side validation for password
#             if len(password) < 8 or not any(char.isdigit() for char in password):
#                 fm.add_error('Password', 'Invalid password. Password must be at least 8 characters long and contain at least one digit.')
#                 return render(request, 'Useradd.html', {'form1': fm})
            
#             # If all validations pass, save the form data
#             fm.save()
#             return redirect('Useradd')  # Assuming 'Useradd' is the name of the URL pattern
#     else:
#         fm = Userform()
    
#     return render(request, 'Useradd.html', {'form1': fm})


  
    

def dataview(request):
    register = Users.objects.all()  # Query the New model
    return render(request, 'userview.html', {'view': register})

    # user_id = request.session.get('user_id')
    # if not user_id:
    #     return redirect('index')
    # try:
    #     user = Users.objects.get(pk=user_id)
    #     return render(request, 'userview.html', {'ser': user})  # Use pk instead of id
    # except Users.DoesNotExist:
    #     return redirect('index')

def useredit(request,user_id):
    if request.method == 'POST':
        mydata = Users.objects.get(user_id=user_id)
        fm = Userform(request.POST, instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        mydata = Users.objects.get(user_id=user_id)
        fm = Userform(instance=mydata)
    return render(request, 'useradd.html', {'form1': fm})

def userdelete(request,user_id):
    obj1 = Users.objects.get(user_id=user_id)
    obj1.delete()
    return HttpResponseRedirect(reverse('userview')) 

def policeadd(request):
    user_id = request.session.get('Station_id')
    if not user_id:
        return redirect('index')
    try:
        if request.method=='POST':
            fm=Policeform(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('policeadd')
        else:
            fm=Policeform()
        return render(request,'policeadd.html',{'form1':fm})
    except Users.DoesNotExist:
        return redirect('index')
    
    
    
   
        # user = Station1.objects.get(pk=user_id)
        # return render(request, 'index.html', {'ser': user})  # Use pk instead of id
    
    

def policeview(request):
    
    register = Station1.objects.all()  # Query the New model
    return render(request, 'policeview.html', {'view': register}) 

def editpoliceview(request, id):
    if request.method == 'POST':
        mydata = Station1.objects.get(Station_id=id)
        fm = Policeform(request.POST, instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        mydata = Station1.objects.get(Station_id=id)
        fm = Policeform(instance=mydata)
    return render(request, 'editpoliceview.html', {'form1': fm})

def deletepoliceview(request, id):
    obj1 = Station1.objects.get(Station_id=id)
    obj1.delete()
    return HttpResponseRedirect(reverse('policeview'))

def userpoliceview(request):
    new_id = request.session.get('user_id')
    if not new_id:
        return redirect('index')
    try:
        register = Station1.objects.all().values()  # Query the New model
        return render(request, 'userpoliceview.html', {'view': register}) 
    except Users.DoesNotExist:
        return redirect('index')
    

def hospitaladd(request):
    if request.method=='POST':
        fm=Hospitalform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('hospitaladd')
    else:
        fm=Hospitalform()
    return render(request,'hospitaladd.html',{'form1':fm})

   

def hospitalview(request):
    register = Hospitals.objects.all()  # Query the New model
    return render(request, 'hospitalview.html', {'view': register}) 

def hospitaledit(request,hospital_id):
    if request.method=='POST':
        mydata=Hospitals.objects.get(hospital_id=hospital_id)
        fm=Hospitalform(request.POST,request.FILES,instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        mydata=Hospitals.objects.get(hospital_id=hospital_id)
        fm=Hospitalform(instance=mydata)
    return render(request,'hospitaladd.html',{'form1':fm})

def hospitaldelete(request,hospital_id):
    obj2 = Hospitals.objects.get(hospital_id=hospital_id)
    obj2.delete()
    return HttpResponseRedirect(reverse('hospitalview'))

def useradminview(request):
    register = Users.objects.all()  # Query the New model
    return render(request, 'useradminview.html', {'view': register})

# def useradmindelete(request,user_id):
#     obj2 = Users.objects.get(user_id=user_id)
#     obj2.delete()
#     return HttpResponseRedirect(reverse('useradminview'))

def hospitaladminview(request):
    register = Hospitals.objects.all()  # Query the New model
    return render(request, 'hospitaladminview.html', {'view': register})

def policeadminview(request):
    register = Station1.objects.all()  # Query the New model
    return render(request, 'policeadminview.html', {'view': register})


    
def loginindex(request, usertype):
    if usertype == "User":
        if request.method == 'POST':
            form = loginform(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    user = Users.objects.get(Email=email, Password=password)
                    request.session['user_id'] = user.user_id  # Use the actual primary key field name
                    print(user.user_id)  
                    return redirect('userindex')  # Corrected the redirect URL name
                except Users.DoesNotExist:
                    form.add_error(None, 'Invalid Username or Password')
        else:
            form = loginform()
        return render(request, 'loginindex.html', {'form': form})
    
    if usertype=="Police":
        if request.method == 'POST':
            form = loginform(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    user = Station1.objects.get(Email=email, Password=password)  # Use the actual field names from your User model
                    request.session['Station_id'] = user.id
                    return redirect('policeindex')  # Replace 'adminindex' with the URL name for the successful login page
                except Station1.DoesNotExist:
                    form.add_error(None, 'Invalid Username or Password')
        else:
            form = loginform()
        return render(request, 'loginindex.html', {'form': form})
    
    if usertype == "Hospitals":
        if request.method == 'POST':
            form = loginform(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    user = Hospitals.objects.get(Email=email, Password=password)
                    request.session['hospital_id'] = user.hospital_id  # Use the correct primary key field name
                    return redirect('hospitalindex')
                except Hospitals.DoesNotExist:
                    form.add_error(None, 'Invalid Username or Password')
        else:
            form = loginform()
        return render(request, 'loginindex.html', {'form': form})
    
    if usertype == "Adminlogin":
        if request.method == 'POST':
            form = loginform(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    user = Login.objects.get(email=email, password=password)
                    request.session['id'] = user.id  # Use the correct primary key field name
                    return redirect('adminindex')
                except Login.DoesNotExist:
                    form.add_error(None, 'Invalid Username or Password')
        else:
            form = loginform()
        return render(request, 'loginindex.html', {'form': form})


# def logout(request):
#     logout(request)
#     request.session.clear()
#     return redirect('index')
@never_cache
def logout(request):
    auth_logout(request)  # Use Django's logout function
    request.session.flush()  # Clear the session
    response = redirect('index')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # HTTP 1.1
    response['Pragma'] = 'no-cache'  # HTTP 1.0
    response['Expires'] = '0'  # Proxies
    return response
# def logout(request):
#     auth_logout(request)  # Use Django's logout function
#     request.session.flush()  # Clear the session
#     return redirect('index')

def Update_User_profile(request, user_id):
    if user_id is None:
        return redirect('loginindex')
    
    try:
        mydata = Users.objects.get(user_id=user_id)
    except Users.DoesNotExist:
        return redirect('loginindex')
    
    if request.method == 'POST':
        fm = Userform(request.POST, instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        fm = Userform(instance=mydata)
    
    return render(request, 'edit_User.html', {'ser': fm})


def Update_Police_profile(request, Station_id):
    if Station_id is None:
        return redirect('loginindex')
    
    try:
        mydata = Station1.objects.get(Station_id=Station_id)
    except Station1 .DoesNotExist:
        return redirect('loginindex')
    
    if request.method == 'POST':
        fm = Policeform(request.POST, instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        fm = Policeform(instance=mydata)
    
    return render(request, 'edit_police.html', {'ser': fm})

def update_Hospitals_profile(request, hospital_id):
    if hospital_id is None:
        return redirect('loginindex')
    
    try:
        mydata = Hospitals.objects.get(hospital_id=hospital_id)
    except Hospitals .DoesNotExist:
        return redirect('loginindex')
    
    if request.method == 'POST':
        fm = Hospitalform(request.POST, instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        fm = Hospitalform(instance=mydata)
    
    return render(request, 'edit_Hospital.html', {'ser': fm})


def User_missingadd(request):
    if request.method == 'POST':
        fm = UserMissingform(request.POST, request.FILES)
        if fm.is_valid():
            # Check for duplicate entry
            name = fm.cleaned_data['Name']
            gender = fm.cleaned_data['Gender']
            age = fm.cleaned_data['Age']
            height = fm.cleaned_data['Height']
            weight = fm.cleaned_data['Weight']
            missing_date = fm.cleaned_data['Missing_date']
            missing_place = fm.cleaned_data['Missing_place']
            other_details = fm.cleaned_data['Other_details']
            # photo = fm.cleaned_data['Photo']
            # Photo=request.FILES.get('Photo')
            # print(Photo)
            if Usermissingadds.objects.filter(Name=name, Gender=gender, Age=age, Height=height, Weight=weight,
                                               Missing_date=missing_date, Missing_place=missing_place,
                                               Other_details=other_details).exists():
                return render(request, 'error.html', {'message': 'Duplicate entry found'})
            else:
                # fm.save()
                instance = fm.save(commit=False)
                instance.Photo = request.FILES['Photo']
                instance.save()
                return redirect('Usermissingadd')
    else:
        fm = UserMissingform()
    
    return render(request, 'Usermissingadd.html', {'form1': fm})  
def usermissingview(request):
    new_id = request.session.get('user_id')
    if not new_id:
        return redirect('index')
    try:
        register = Usermissingadds.objects.all()  # Query the New model
        return render(request, 'usermissingview.html', {'view': register}) 
    except Users.DoesNotExist:
        return redirect('index')

def edituser_missing(request,id):
    if request.method=='POST':
        mydata=Usermissingadds.objects.get(id=id)
        fm=UserMissingform(request.POST,request.FILES,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('usermissingview')
    else:
        mydata=Usermissingadds.objects.get(id=id)
        fm=UserMissingform(instance=mydata)
    return render(request,'editusermissingadd.html',{'form1':fm})

def deleteuser_missing(request, id):
    obj2 = Usermissingadds.objects.get(id=id)
    obj2.delete()
    return HttpResponseRedirect(reverse('usermissingview'))


def policemissingview(request):
    hospital_id = request.session.get('Station_id')
    if not hospital_id:
        return redirect('index')
    try:
        register = Usermissingadds.objects.all() 
        return render(request, 'policemissingview.html', {'view': register})
    except Station1.DoesNotExist:
        return redirect('index')
def missing_people_view_public(request, id):
    obj2 = Usermissingadds.objects.get(id=id)
    print(id)
    obj2.Pass_to_public = 1
    

    obj2.save()
    print(obj2)
    return HttpResponseRedirect(reverse('policemissingview'))

def public_missing_view(request):
    view = Usermissingadds.objects.filter(Pass_to_public=1).values()
    # obj2 = Accidents.objects.get(id=id)
    return render(request, 'public_missing_view.html', {'view': view})




def Accident(request):
    new_id = request.session.get('user_id')
    if not new_id:
        return redirect('index')
    try:
        if request.method=='POST':
            fm=Accidentform(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect('userindex')
        else:
            fm=Accidentform()
        return render(request,'Accidentadd.html',{'form1':fm})
    except Users.DoesNotExist:
        return redirect('index')



#check at last
def accidentview(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        return redirect('index')
    try:
        stu = Accidents.objects.all().values()  # Query the New model
        return render(request, 'accidentview.html', {'view': stu})
    except Hospitals.DoesNotExist:
        return redirect('index')

def policeaccidentview(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        return redirect('index')
    try:
        stu = Accidents.objects.all().values()  # Query the New model
        return render(request, 'policeaccidentview.html', {'view': stu})
    except Hospitals.DoesNotExist:
        return redirect('index') 

def editaccident(request,id):
    if request.method=='POST':
        mydata=Accidents.objects.get(id=id)
        fm=Accidentform(request.POST,request.FILES,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('accidentview')
    else:
        mydata=Accidents.objects.get(id=id)
        fm=Accidentform(instance=mydata)
    return render(request,'Accidentadd.html',{'form1':fm})

def accidentdelete(request, id):
    obj2 = Accidents.objects.get(id=id)
    obj2.delete()
    return HttpResponseRedirect(reverse('accidentview'))



def casesheetadd(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        return redirect('index')
    try:
        if request.method=='POST':
            fm=Casesheet1(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect('casesheetadd')
        else:
            fm=Casesheet1()
        return render(request,'casesheetadd.html',{'form1':fm})
    except Hospitals.DoesNotExist:
        return redirect('index')
    
@never_cache
def casesheetview(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        return redirect('index')
    try:
        register = Casesheet.objects.all()  # Query the New model
        return render(request, 'casesheetview.html', {'view': register})
    except Hospitals.DoesNotExist:
        return redirect('index') 

def editcasesheetadd(request, id):
    if request.method == 'POST':
        mydata = Casesheet.objects.get(Patient_id=id)
        fm = Casesheet1(request.POST,request.FILES, instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('casesheetview')
    else:
        mydata = Casesheet.objects.get(Patient_id=id)
        fm = Casesheet1(instance=mydata)
    return render(request, 'editcasesheet.html', {'form1': fm})

def deletecasesheetadd(request, id):
    obj1 = Casesheet.objects.get(Patient_id=id)
    obj1.delete()
    return HttpResponseRedirect(reverse('casesheetview'))

def policecasesheetview(request):
    hospital_id = request.session.get('Station_id')
    if not hospital_id:
        return redirect('index')
    try:
        register = Casesheet.objects.all().values()  # Query the New model
        return render(request, 'policecasesheetview.html', {'view': register}) 
    except Station1.DoesNotExist:
        return redirect('index')

def user_enquiry(request):
    new_id = request.session.get('user_id')
    if not new_id:
        return redirect('index')
    try:
        register = Hospitals.objects.all()  # Query the New model
        return render(request, 'user_enquiry.html', {'view': register})

    except Users.DoesNotExist:
            return redirect('index')
    
def user_enquiryaddDetails(request, hospital_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('index')
    try:

        print("User ID:", user_id)  # Print the user_id to debug
        # Print all values of Hospitals
        all_hospitals_values = Hospitals.objects.values()
        print("All Hospitals Values:", all_hospitals_values)

        if request.method == 'POST':
            hospital_instance = Hospitals.objects.get(hospital_id=hospital_id)
            fm = Enquiryform(request.POST)
            
            if fm.is_valid():
                enquiry_instance=fm.cleaned_data
                enquiry_instance = fm.save(commit=False)
                enquiry_instance.user_id_id = user_id  # Assuming 'user_id' is the foreign key field in Enquiries_hosp_police
                enquiry_instance.hospital_id = hospital_instance.hospital_id  # Assign the hospital_id directly
                enquiry_instance.Current_Date = date.today()

                # max_enquiry_id=Enquiry.objects.aggregate(Max('enquiry_id'))['enquiry_id_max'] or 0
                # enquiry_instance.enquiry_id=max_enquiry_id + 1
                enquiry_instance.save()
                return redirect('user_enquiry')

        else:
            fm = Enquiryform()

        return render(request, 'user_enquirypage.html', {'form1': fm})
    except Users.DoesNotExist:
        return redirect('index')

def user_enquiryview(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        return redirect('index')
    try:

        user_id = request.session.get('user_id')
        if user_id:
         register = Enquiry.objects.filter(user_id=user_id).all() # Query the Enquirys model
        else:
            register = Enquiry.objects.all()
        return render(request, 'user_enquiryview.html', {'view': register})
    except Hospitals.DoesNotExist:
        return redirect('index')


def user_replyadd(request,enquiry_id):
    # user_id = request.session.get('user_id')
    # print("User ID:", user_id)  # Print the user_id to debug

    # Retrieve the existing Enquirys instance or return a 404 response if not found
    enquiry_instance = Enquiry.objects.get(enquiry_id=enquiry_id)
    print(enquiry_instance)

    if request.method == 'POST':
        # Create a form with the POST data and the instance of the existing Enquirys
        fm = Replyform(request.POST, instance=enquiry_instance)

        if fm.is_valid():
            print("reply", request.POST.get('Reply'))
            # Save the form to update the existing Enquirys instance
            fm.save()
            # Redirect to publicenquiryview after successful form submission
            return redirect('user_enquiryview')
    else:
        # Create a form with the instance of the existing Enquirys for editing
        fm = Replyform(instance=enquiry_instance)

    return render(request, 'user_replyadd.html', {'form1': fm})

def user_replyview(request):
    new_id = request.session.get('user_id')
    if not new_id:
        return redirect('index')
    try:
        inquiries_with_replies = Enquiry.objects.all()
        for inquiry in inquiries_with_replies:
            # Assuming 'field_name' is the name of the field you want to print
            if inquiry.enquiry_id is not None:
                print(f'{inquiry.enquiry_id},{inquiry.Reply},{inquiry.Enquiry_detail}')

        return render(request, 'user_replyview.html', {'inquiries_with_replies': inquiries_with_replies})
    except Users.DoesNotExist:
        return redirect('index')


def police_enquiry(request):
    hospital_id = request.session.get('Station_id')
    if not hospital_id:
        return redirect('index')
    try:
        register = Hospitals.objects.all()  # Query the New model
        return render(request, 'police_enquiry.html', {'view': register})
    except Station1.DoesNotExist:
        return redirect('index')

def police_enquiryaddDetails(request, hospital_id):
    Station_id = request.session.get('Station_id')
    if not Station_id:
        return redirect('index')
    try:
        print('Station_id')
        if request.method == 'POST':
            hospital_instance = Hospitals.objects.get(hospital_id=hospital_id)  # Get hospital data
            fm = Enquiryform(request.POST)

            if fm.is_valid():
                try:
                    station_instance = Station1.objects.get(Station_id=Station_id)
                except Station1.DoesNotExist:
                    # Handle the case where Station1 with the specified Station_id does not exist
                    # For example, you can return an error message or redirect to a different page.
                    return redirect('police_enquiry')
                enquiry_instance = fm.save(commit=False)
                enquiry_instance.Station_id = station_instance  # Set the Station1 instance
                enquiry_instance.hospital = hospital_instance

                # Set current date
                enquiry_instance.Current_Date = date.today()
                enquiry_instance.save()
                
        else:
            fm = Enquiryform()
        return render(request, 'police_enquirypage.html', {'form1': fm})
    except Station1.DoesNotExist:
        return redirect('index')

def police_enquiryview(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        return redirect('index')
    try:

        register = Enquiry.objects.all()  # Query the Enquirys model
        return render(request, 'police_enquiryview.html', {'view': register})
    except Hospitals.DoesNotExist:
        return redirect('index')


def replyadd_police(request,enquiry_id):
    # user_id = request.session.get('user_id')
    # print("User ID:", user_id)  # Print the user_id to debug

    # Retrieve the existing Enquirys instance or return a 404 response if not found
    enquiry_instance = Enquiry.objects.get(enquiry_id=enquiry_id)
    print(enquiry_instance)

    if request.method == 'POST':
        # Create a form with the POST data and the instance of the existing Enquirys
        fm = Replyform(request.POST, instance=enquiry_instance)

        if fm.is_valid():
            print("reply", request.POST.get('Reply'))
            # Save the form to update the existing Enquirys instance
            fm.save()
            # Redirect to publicenquiryview after successful form submission
            return redirect('police_enquiryview')
    else:
        # Create a form with the instance of the existing Enquirys for editing
        fm = Replyform(instance=enquiry_instance)

    return render(request, 'replyadd_police.html', {'form1': fm})

def replyview_police(request):
    hospital_id = request.session.get('Station_id')
    if not hospital_id:
        return redirect('index')
    try:

        inquiries_with_replies = Enquiry.objects.all()
        for inquiry in inquiries_with_replies:
            # Assuming 'field_name' is the name of the field you want to print
            if inquiry.enquiry_id is not None:
                print(f'{inquiry.enquiry_id},{inquiry.Reply},{inquiry.Enquiry_detail}')

        return render(request, 'replyview_police.html', {'inquiries_with_replies': inquiries_with_replies})
    
    except Station1.DoesNotExist:
            return redirect('index')




def file_complaint(request,Station_id ):
    Station_id = request.session.get('Station_id')
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaintadd')  # Redirect to a thank you page or any other view
    else:
        form = ComplaintForm()
    return render(request, 'complaintadd.html', {'form': form})

def complaintview(request):
    register = Complaint.objects.all() # Query the Enquirys model
    return render(request, 'complaintview.html', {'view': register})


def public_enquiry(request):
    hospitals = Hospitals.objects.all()  # Fetch all hospitals for the dropdown
    
    # List of districts in Kerala (replace with actual districts)
    kerala_districts = ['Thiruvananthapuram', 'Kollam', 'Pathanamthitta', 'Alappuzha', 'Kottayam', 'Idukki', 'Ernakulam', 'Thrissur', 'Palakkad', 'Malappuram', 'Kozhikode', 'Wayanad', 'Kannur', 'Kasaragod']
    # kerala_districts = list(Hospitals.objects.values_list('District', flat=True).distinct())
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        enquiry_text = request.POST.get('enquiry')
        selected_hospital_id = request.POST.get('hospital')
        print(selected_hospital_id)

        # Save the public enquiry to the database
        Public_Enquiry.objects.create(Name=name, Phone=phone, Enquiry=enquiry_text, hospital_id=selected_hospital_id)

        # Redirect to a success page or any other page you prefer
        
        print(enquiry_text)
        return redirect('index')
    return render(request, 'public_enquiry.html', {'hospitals': hospitals, 'kerala_districts': kerala_districts})

# def replyview_public(request):
#     inquiries_with_replies = Public_Enquiry.objects.all()
#     for inquiry in inquiries_with_replies:
#         # Assuming 'field_name' is the name of the field you want to print
#         if inquiry.enquiry_id is not None:
#             print(f'{inquiry.enquiry_id},{inquiry.Reply},{inquiry.Enquiry}')

#     return render(request, 'public_reply_view.html', {'inquiries_with_replies': inquiries_with_replies})

def enquiryview_public(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        return redirect('index')
    try:

        register = Public_Enquiry.objects.all() # Query the Enquirys model
        return render(request, 'public_enquiryview.html', {'view': register})
    except Hospitals.DoesNotExist:
        return redirect('index')

def reply_public_add(request,enquiry_id):
    enquiry_instance = Public_Enquiry.objects.get( enquiry_id=enquiry_id)
    print(enquiry_instance)

    if request.method == 'POST':
        # Create a form with the POST data and the instance of the existing Enquirys
        fm = Public_Replyform(request.POST, instance=enquiry_instance)

        if fm.is_valid():
            print("reply", request.POST.get('Reply'))
            # Save the form to update the existing Enquirys instance
            fm.save()
            # Redirect to publicenquiryview after successful form submission
            return redirect('public_enquiryview')
    else:
        # Create a form with the instance of the existing Enquirys for editing
        fm = Public_Replyform(instance=enquiry_instance)

    return render(request, 'reply_add_public.html', {'form1': fm})

def replyview_public(request):
    inquiries_with_replies = Public_Enquiry.objects.all()
    for inquiry in inquiries_with_replies:
        # Assuming 'field_name' is the name of the field you want to print
        if inquiry.enquiry_id is not None:
            print(f'{inquiry.enquiry_id},{inquiry.Reply},{inquiry.Enquiry}')

    return render(request, 'replyview_public.html', {'inquiries_with_replies': inquiries_with_replies})



def missing_found(request, id):
    if request.method == 'POST':
        missing_data = Usermissingadds.objects.get(id=id)
        fm = Found(request.POST,request.FILES)
        if fm.is_valid():
            found_data = fm.save(commit=False)
            found_data.found_Usermissing = missing_data
            found_data.save()
            return redirect('public_missing_view')
    else:
        fm = Found()
    return render(request, 'found_missing_add.html', {'form1': fm})

def found_view(request):
    hospital_id = request.session.get('Station_id')
    if not hospital_id:
        return redirect('index')
    try:
        view = Missing_found.objects.filter().values()
        return render(request, 'found_view.html', {'view': view})
    except Station1.DoesNotExist:
        return redirect('index')

def find_missing_person(request, missing_person_id):
    missing_person = get_object_or_404(Usermissingadds, id=missing_person_id)
    context = {
        'missing_person': missing_person,
    }
    return render(request, 'missing_person_temp.html', context)
# def run_apriori_algorithm(request):
#     if request.method == 'POST':
#         missing_person_id = request.POST.get('missing_person_id')
#         missing_person = get_object_or_404(Usermissingadds, id=missing_person_id)

#         # Create a list of transactions (lists of items) based on your data
#         transactions = []

#         # Fetch matching cases from Casesheet based on attributes of missing_person
#         matching_cases = Casesheet.objects.filter(Patient_Name=missing_person.Name)

#         # Load the missing person's photo (check if it's None)
#         missing_person_photo = cv2.imread(str(missing_person.Photo.path))
#         if missing_person_photo is None:
#             return render(request, 'error.html', {'message': 'Missing person photo could not be loaded.'})

#         # Initialize NLTK SentimentIntensityAnalyzer
#         analyzer = SentimentIntensityAnalyzer()
#         threshold = 50
#         photo_matched = False  # Initialize photo_matched flag

#         for case in matching_cases:
#             case_photo = cv2.imread(str(case.Photo.path))
#             if case_photo is None:
#                 continue

#             # Resize both images to the same dimensions
#             case_photo_resized = cv2.resize(case_photo, (missing_person_photo.shape[1], missing_person_photo.shape[0]))

#             # Check image dimensions (for debugging)
#             print("Missing Person Photo Dimensions:", missing_person_photo.shape)
#             print("Case Photo Dimensions:", case_photo_resized.shape)

#             # Calculate MSE
#             mse = ((missing_person_photo - case_photo_resized) ** 2).mean()

#             # Print MSE value (for debugging)
#             print("MSE:", mse)

#             # Tokenize and analyze the description text
#             description_text = case.Description
#             words = word_tokenize(description_text)
#             word_freq = FreqDist(words)

#             # Perform sentiment analysis on the description
#             sentiment = analyzer.polarity_scores(description_text)
#             positive_sentiment = round(sentiment['pos'], 2)  # Round the positive sentiment score to 2 decimal places
#             negative_sentiment = round(sentiment['neg'], 2)

#             # Define a transaction with sentiment analysis scores
#             transaction = [
#                 f"Gender_{1 if missing_person.Gender == 'F' else 0}",  # Ensure binary values
#                 # positive_sentiment,  # Store positive sentiment score as numeric value
#                 # negative_sentiment,  # Store negative sentiment score as numeric value
#                 mse <= threshold,
#                 # Add other attributes as needed
#             ]
#             transactions.append(transaction)

#             # Set photo_matched to True if a match is found
#             if mse <= threshold:
#                 photo_matched = True
           
#         # Create a DataFrame with one-hot encoding
#         oht = pd.get_dummies(pd.DataFrame(transactions), columns=[0])

#         # Use Apriori to find frequent itemsets (adjust min_support as needed)
#         frequent_itemsets = apriori(oht, min_support=0.1, use_colnames=True)

#         # Extract association rules from the frequent itemsets (adjust min_threshold as needed)
#         rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

#         context = {
#             'missing_person': missing_person,
#             'matching_cases': matching_cases,
#             'frequent_itemsets': frequent_itemsets,
#             'rules': rules,
#             'photo_matched': photo_matched,
#         }
#         if(context != ''):
#             return render(request, 'matched_details.html', context)
#         else:
#             context = {
#             'missing_person': 'No matching details',
#             'matching_cases': 'No matching details',
#             'frequent_itemsets': 'No matching details',
#             'rules': rules,
#             'photo_matched': 'No matching details',
#             }
#             return render(request, 'matched_details.html', 'No matching details')

#     return redirect('usernewtable')

def run_apriori_algorithm(request):
    if request.method == 'POST':
        missing_person_id = request.POST.get('missing_person_id')
        missing_person = get_object_or_404(Usermissingadds, id=missing_person_id)
        # print(missing_person.Photo.path)
        # Create a list of transactions (lists of items) based on your data
        transactions = []

        # Fetch matching cases from Casesheet based on attributes of missing_person
        matching_cases = Casesheet.objects.filter(Patient_Name=missing_person.Name)

        # Load the missing person's photo (check if it's None)
        missing_person_photo = cv2.imread(str(missing_person.Photo.path))
        # print(missing_person_photo)
        if missing_person_photo is None:
            return render(request, 'error.html', {'message': 'Missing person photo could not be loaded.'})

        # Initialize NLTK SentimentIntensityAnalyzer
        analyzer = SentimentIntensityAnalyzer()
        threshold = 50
        photo_matched = False  # Initialize photo_matched flag

        for case in matching_cases:
            case_photo = cv2.imread(str(case.Photo.path))
            if case_photo is None:
                continue

            # Resize both images to the same dimensions
            case_photo_resized = cv2.resize(case_photo, (missing_person_photo.shape[1], missing_person_photo.shape[0]))

            # Check image dimensions (for debugging)
            print("Missing Person Photo Dimensions:", missing_person_photo.shape)
            print("Case Photo Dimensions:", case_photo_resized.shape)

            # Calculate MSE
            mse = ((missing_person_photo - case_photo_resized) ** 2).mean()

            # Print MSE value (for debugging)
            print("MSE:", mse)

            # Tokenize and analyze the description text
            description_text = case.Description
            words = word_tokenize(description_text)
            word_freq = FreqDist(words)

            # Perform sentiment analysis on the description
            sentiment = analyzer.polarity_scores(description_text)
            positive_sentiment = round(sentiment['pos'], 2)  # Round the positive sentiment score to 2 decimal places
            negative_sentiment = round(sentiment['neg'], 2)

            # Define a transaction with sentiment analysis scores
            transaction = [
                f"Gender_{1 if missing_person.Gender == 'F' else 0}",  # Ensure binary values
                # positive_sentiment,  # Store positive sentiment score as numeric value
                # negative_sentiment,  # Store negative sentiment score as numeric value
                mse <= threshold,
                # Add other attributes as needed
            ]
            transactions.append(transaction)

            # Set photo_matched to True if a match is found
            if mse >= threshold:
                photo_matched = True

        # Check if transactions list is empty
        if not transactions:
            context = {
                'missing_person': ('No matching details'),
                'matching_cases': ('No matching details'),
                'frequent_itemsets': ('No matching details'),
                'rules': ('No matching details'),
                'photo_matched': ('No matching details'),
            }
            return render(request, 'matched_details.html', context)

        # Create a DataFrame with one-hot encoding
        oht = pd.get_dummies(pd.DataFrame(transactions), columns=[0])

        # Use Apriori to find frequent itemsets (adjust min_support as needed)
        frequent_itemsets = apriori(oht, min_support=0.1, use_colnames=True)

        # Extract association rules from the frequent itemsets (adjust min_threshold as needed)
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

        context = {
            'missing_person': missing_person,
            'matching_cases': matching_cases,
            'frequent_itemsets': frequent_itemsets,
            'rules': rules,
            'photo_matched': photo_matched,
        }
        
        return render(request, 'matched_details.html', context)

    return redirect('usernewtable')
# def run_apriori_algorithm(request):
#     if request.method == 'POST':
#         missing_person_id = request.POST.get('missing_person_id')
#         missing_person = get_object_or_404(Usermissingadds, id=missing_person_id)
#         # print(missing_person.Photo.path)
#         # Create a list of transactions (lists of items) based on your data
#         transactions = []

#         # Load the missing person's photo (check if it's None)
#         missing_person_photo = cv2.imread(str(missing_person.Photo.path))
#         # print(missing_person_photo)
#         if missing_person_photo is None:
#             return render(request, 'error.html', {'message': 'Missing person photo could not be loaded.'})

#         # Initialize NLTK SentimentIntensityAnalyzer
#         analyzer = SentimentIntensityAnalyzer()
#         threshold = 50
#         photo_matched = False  # Initialize photo_matched flag

#         # Fetch all cases from Casesheet
#         all_cases = Casesheet.objects.filter(Patient_Name=missing_person.Name)

#         matching_cases = []

#         for case in all_cases:
#             if case.Photo:  # Ensure case has a photo
#                 case_photo = cv2.imread(str(case.Photo.path))
#                 if case_photo is None:
#                     continue

#                 # Resize both images to the same dimensions
#                 case_photo_resized = cv2.resize(case_photo, (missing_person_photo.shape[1], missing_person_photo.shape[0]))

#                 # Calculate MSE
#                 mse = ((missing_person_photo - case_photo_resized) ** 2).mean()

#                 if mse <= threshold:
#                     matching_cases.append(case)
#                     photo_matched = True
#                     break

#         # Check if photo is matched
#         if not photo_matched:
#             # Photo not matched
#             context = {
#                 'missing_person': missing_person,
#                 'matching_cases': [],
#                 'frequent_itemsets': [],
#                 'rules': [],
#                 'photo_matched': False,
#             }
#             return render(request, 'matched_details.html', context)

#         # If photo is matched, then proceed with data check
#         for case in matching_cases:
#             # Tokenize and analyze the description text
#             description_text = case.Description
#             words = word_tokenize(description_text)

#             # Perform sentiment analysis on the description
#             sentiment = analyzer.polarity_scores(description_text)
#             positive_sentiment = round(sentiment['pos'], 2)  # Round the positive sentiment score to 2 decimal places
#             negative_sentiment = round(sentiment['neg'], 2)

#             # Define a transaction with sentiment analysis scores
#             transaction = [
#                 f"Gender_{1 if missing_person.Gender == 'F' else 0}",  # Ensure binary values
#                 # positive_sentiment,  # Store positive sentiment score as numeric value
#                 # negative_sentiment,  # Store negative sentiment score as numeric value
#                 True,  # Photo matched
#                 # Add other attributes as needed
#             ]
#             transactions.append(transaction)

#         # Create a DataFrame with one-hot encoding
#         oht = pd.get_dummies(pd.DataFrame(transactions), columns=[0])

#         # Use Apriori to find frequent itemsets (adjust min_support as needed)
#         frequent_itemsets = apriori(oht, min_support=0.1, use_colnames=True)

#         # Extract association rules from the frequent itemsets (adjust min_threshold as needed)
#         rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

#         context = {
#             'missing_person': missing_person,
#             'matching_cases': matching_cases,
#             'frequent_itemsets': frequent_itemsets,
#             'rules': rules,
#             'photo_matched': photo_matched,
#         }
        
#         return render(request, 'matched_details.html', context)

#     return redirect('usernewtable')
