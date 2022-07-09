from django.shortcuts import render
from django.http import HttpResponse
from cmsappli.models import CourseDetails,StreamDetails,UserDetails
import cx_Oracle



# _________________________SHOW COURSE DATA______________________

def showdata(request):
    CourseD = CourseDetails.objects.all()
    return render(request,"showdata.html",{'CD':CourseD})

# _________________________SHOW STREAM DATA______________________

def showstreams(request):
    StreamS = StreamDetails.objects.all()
    return render(request,"showstreams.html",{'CS':StreamS})

# _________________________SHOW USER DATA ______________________

def showuserd(request):
    userd = UserDetails.objects.all()
    return render(request,"showuserd.html",{'UDT':userd})



# _________________________ADD COURSE DATA FORM______________________

C_id = ''
C_name = ''
S_name = ''
def addcourse(request):
    global C_id,C_name,S_name
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        co=request.POST
        for key,value in co.items():
            if key=="C_id":
                C_id=value
            if key=="C_name":
                C_name=value
            if key=="S_name":
                S_name=value      
        cursor.execute("insert into add_c(C_id,C_name,S_name) values('{}','{}','{}')".format(C_id,C_name,S_name))
        conn.commit()
    return render(request,"addcourse.html")

# _______________________DELETE COURSE DATA FORM______________________


C_id = ''
C_name = ''
S_name = ''
def delc(request):
    global C_id,C_name,S_name
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        co=request.POST
        for key,value in co.items():
            if key=="C_id":
                C_id=value
            if key=="C_name":
                C_name=value
            if key=="S_name":
                S_name=value      
        cursor.execute("delete from add_c where c_id='{}' and c_name='{}' ".format(C_id,C_name,S_name))
        # admin_name='{}' and admin_pass='{}' ".format(admin_name,admin_pass))
        conn.commit()
    return render(request,"delc.html")

# _______________________UPDATE COURSE DATA FORM______________________

C_id = ''
C_name = ''
S_name = ''
def updatec(request):
    global C_id,C_name,S_name
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        co=request.POST
        for key,value in co.items():
            if key=="C_id":
                C_id=value
            if key=="C_name":
                C_name=value
            if key=="S_name":
                S_name=value      
        cursor.execute("update add_c set c_name='{}', s_name='{}' where c_id='{}'".format(C_name,S_name,C_id))
        conn.commit()
    return render(request,"updatec.html")





# _______________________ADD STREAM DATA FORM______________________

S_id = ''
S_name = ''
def addstream(request):
    global S_id,S_name
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        co=request.POST
        for key,value in co.items():
            if key=="st":
                S_id=value
            if key=="co":
                S_name=value      
        cursor.execute("insert into add_s(S_id,S_name) values('{}','{}')".format(S_id,S_name))
        conn.commit()
    return render(request,"addstream.html")

# _______________________DELETE STREAM DATA FORM______________________

S_id = ''
S_name = ''
def dels(request):
    global S_id,S_name
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        co=request.POST
        for key,value in co.items():
            if key=="st":
                S_id=value
            if key=="co":
                S_name=value      
        cursor.execute("delete from add_s where s_id='{}' and s_name='{}' ".format(S_id,S_name))
        conn.commit()
    return render(request,"dels.html")

# _______________________UPDATE STREAM DATA FORM______________________

S_id = ''
S_name = ''
def updates(request):
    global S_id,S_name
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        co=request.POST
        for key,value in co.items():
            if key=="st":
                S_id=value
            if key=="co":
                S_name=value      
        cursor.execute("update add_s set s_name='{}' where s_id='{}'".format(S_name,S_id))
        conn.commit()
    return render(request,"updates.html")




#=================///////////////////================
#<-----------------Admin Login Page----------------->
#=================///////////////////================

admin_name = ''
admin_pass = ''
def admin_login(request):
    global admin_name,admin_pass
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="adname":
                admin_name=value
            if key=="adpass":
                admin_pass=value

        cursor.execute("select * from admin where admin_name='{}' and admin_pass='{}' ".format(admin_name,admin_pass))
        t = tuple(cursor.fetchall())
        if t==():
            return render(request,'aderror.html')
        else:
            return render(request,'crudop.html')

    return render(request,"admin_login.html")


Id_Number = ''
Stream_Name = ''

def add_stream(request):
    global Id_Number,Stream_Name
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        reg=request.POST
        for key,value in reg.items():
            if key=="st":
                Id_Number=value
            if key=="co":
                Stream_Name=value
        c="insert into streampannel values('{}','{}','{}')".format(Id_Number,Stream_Name)
        # c="insert into user_info values('%s,%s')"
        cursor.execute(c)
        conn.commit()
    return render(request,'register.html')



#=====================///////////////////===================
#<-----------------------Main Menu------------------------>
#=====================///////////////////===================



def index(request):
    return render(request,"index.html")



#=====================///////////////////===================
# <-----------------------Home Page--------------------->
#=====================///////////////////===================


def home(request):

    return render(request,"home.html")



#=====================///////////////////===================
# <------------------------Login Form----------------------->
#=====================///////////////////===================




user_name = ''
user_psswd =''

def login(request):
    global user_name,user_psswd
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        lg=request.POST
        for key,value in lg.items():
            if key=="username":
                user_name=value
            if key=="password":
                user_psswd=value
        
        st="select * from userdetails where user_name='{}' and user_psswd='{}' ".format(user_name,user_psswd)
        cursor.execute(st)
        t = tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')

        else:
            return render(request,'home.html')

    return render(request,"login.html")



#=====================///////////////////===================
# <---------------------Register Form---------------------->
#=====================///////////////////===================



user_name = ''
user_email =''
user_psswd =''

def register(request):
    global user_name,user_email,user_psswd
    if request.method=="POST":
        conn = cx_Oracle.connect('rajan/harpal@localhost:1521/xe')
        cursor=conn.cursor()
        reg=request.POST
        for key,value in reg.items():
            if key=="username":
                user_name=value
            if key=="email":
                user_email=value
            if key=="password":
                user_psswd=value
        c="insert into userdetails values('{}','{}','{}')".format(user_name,user_email,user_psswd)
        # c="insert into user_info values('%s,%s')"
        cursor.execute(c)
        conn.commit()
    return render(request,'register.html')

