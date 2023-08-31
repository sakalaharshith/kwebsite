
from flask import Flask,redirect,url_for,render_template,request
import requests
import contentful
from flask_mail import Mail, Message


det={"option1":" uniform and excellent vegetative growth", "option2":"Krish Poshak can be used for both spray and drip", "option3":"Krish Poshak prevents detoriation of soil texture","option4":"Krish Poshak is a 100% water soluble fertilisers","option5":"Krish Poshak is a 100% water soluble fertilisers"}
details1={'option1':{"option1":" uniform and excellent vegetative growth", "option2":"Krish Poshak can be used for both spray and drip", "option3":"Krish Poshak prevents detoriation of soil texture","option4":"Krish Poshak is a 100% water soluble fertilisers","option5":"Krish Poshak is a 100% water soluble fertilisers"},
     'option2':{"option1":" data2", "option2":"data2", "option3":"data2","option4":"data2","option5":"data2"},'option3':{"option1":" data2", "option2":"data2", "option3":"data2","option4":"data2","option5":"data2"}}
try:
    client=contentful.Client('oax5w1uuj25z','ITG8SJpPUIhY0PYh0proG54U8HcgbDm1pLdbVFtBpQs')
except requests.exceptions.ConnectionError:
    print("Connection rejected by contentful")

entries = client.entries({'content_type':"waterSoluble"})
object_dict={}

#3mTCCZ2ddRuupUzT5E6WeX
assets1=client.assets()
#print("the length of assets",len(assets1))
for asset in assets1:
    print("the asset url is",asset.url())




for x in entries:
    dictionary={"name":x.name,}
    name=""+x.name
    
   # print(name)
    features1=x.features
    features1=features1.split('.')
    field1=x.fields()
    #print("**************************** the name of the fields",x.fields()['product_image'])
    image_asset=x.fields()['product_image']
    #print("the image url is ",image_asset.url())
    dictionary['features']=features1
    dictionary['image_url']=image_asset.url()
    #print(dictionary)
    object_dict[name]=dictionary
    #print(object_dict)
    

app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='krishchem.fertilizers@gmail.com'
#app.config['MAIL_PASSWORD']='pwehvghpyoctjqai'
app.config['MAIL_PASSWORD']='pkwtnlskwenwwhrf'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)


@app.route('/')
def welcome():
    product_type='water Soluble'
    about_us={'name':'COMPANY PROFILE','information':'Krish Chem Ltd is an importer, marketer and supplier of 100% water soluble speciality fertilizers , micronutrient fertilisers , plant growths and etc . We constantly research and look through lense for various innovative products available in the market globally and thoroughly vet our suppliers in the selection process. As a result, we only partner with industry leading manufacturers which employ cutting edge technologies in producing top of the quality agriculture products consistently. We do all the hard work for you so you dont have to go through this painstakingly cumbersome process but simply contact and consult with us for your needs.'}
    about_us1={'name':'COMPANY PROFILE','information':'Krish Chem Ltd is an importer, marketer and supplier of 100% water soluble speciality fertilizers , micronutrient fertilisers , plant growths and etc . We constantly research and look through lense for various innovative products available in the market globally and thoroughly vet our suppliers in the selection process. As a result, we only partner with industry leading manufacturers which employ cutting edge technologies in producing top of the quality agriculture products consistently. We do all the hard work for you so you dont have to go through this painstakingly cumbersome process but simply contact and consult with us for your needs.'}
    aboutus_entries=client.entries({'content_type':"aboutus"})
    
    about_us_array=[]
    for entry in aboutus_entries:
        print('the name of the entry is',entry.name)
    for entry in aboutus_entries:
        dictionary={}
        dictionary['name']=entry.name
        dictionary['information']=entry.information
        image_asset_aboutus= entry.fields()['aboutus_image']
        dictionary['url']=image_asset_aboutus.url()
        print(dictionary)
        about_us_array.append(dictionary)
        print("inside the list",about_us_array)
    #print("the length of the array is ",len(about_us_array))
    #print("the first array is ", type(about_us_array))
    #print("the first array is ",about_us_array[0])
    #print("the second array is ",about_us_array[1])
    
    #about_us_array=[]
    #about_us_array.append(about_us)
    #about_us_array.append(about_us1)
    #print('inside welcome')
    #print("the home information", about_us_array)

    #return render_template('contactus2.html',contact=['text-danger','this form is not submitted yet'])


    return render_template('homepage.html',details=[about_us_array[2]])




@app.route('/submit',methods=['GET','POST'])
def message():
     if request.method=='POST':
         emptyness_checker=[]
         name=request.form['personname']
         if (len(name)==0):
             emptyness_checker.append('Name')
         email=request.form['email']
         if (len(email)==0):
             emptyness_checker.append('Email')
         contactno=request.form['contactNo']
         if (len(contactno)==0):
             emptyness_checker.append('ContactNo')
         query=request.form['query']
         if (len(query)==0):
             emptyness_checker.append('Query')
         if (len(emptyness_checker)!=0):
             return render_template('contactus2.html',contact=['text-danger','You have forgotten to enter these fields {fields}'.format(fields=emptyness_checker[0:])])

         msg=Message('Query from  Krish Chem website', sender='krishchem.fertilizers@gmail.com',recipients=['krishchem.fertilizers@gmail.com'])
         msg.body='Name of the Person: '+name+'\n'+'Email-ID: '+email+'\n'+'contactno: '+contactno+'\n'+'Query: '+query
         mail.send(msg)
         return render_template('contactus2.html',contact=['text-success','The form is submitted successfully, soon we will contact you with solution.'])
     
     
     return render_template('contactus2.html')
       




@app.route('/aboutus/<string:value>',methods=['GET','POST'])
def about_us_page(value):
    aboutus_entries=client.entries({'content_type':"aboutus"})
    whychooseus_asset=client.asset('ZD0FSqaGcCpWs7QhDEqPC').url()
    ourmission=client.asset('4X7f0S3SAt4c0Mq6Ske4Sx').url()
    companysprofile=client.asset('6N134KrLMQl6xsRoOn1wvC').url()
    
    about_us_array=[]
    for entry in aboutus_entries:
        print('the name of the entry is',entry.name)
    for entry in aboutus_entries:
        dictionary={}
        dictionary['name']=entry.name
        dictionary['information']=entry.information
        image_asset_aboutus= entry.fields()['aboutus_image']
        dictionary['url']=image_asset_aboutus.url()
        print(dictionary)
        about_us_array.append(dictionary)
        print("inside the list",about_us_array)
    #print("the length of the array is ",len(about_us_array))
    #print("the first array is ", type(about_us_array))
    #print("the first array is ",about_us_array[0])
    #print("the second array is ",about_us_array[1])
    
    #about_us_array=[]
    #about_us_array.append(about_us)
    #about_us_array.append(about_us1)
    #print('inside welcome')
    #print("the home information", about_us_array)
    if value=='whychooseus':
        return render_template('aboutus.html',details=[about_us_array[0],companysprofile,whychooseus_asset,ourmission])
    
    if value=='ourmission':
        return render_template('aboutus.html',details=[about_us_array[1],companysprofile,whychooseus_asset,ourmission])
    
    if value=='companyprofile':
         return render_template('aboutus.html',details=[about_us_array[2],companysprofile,whychooseus_asset,ourmission])
    


    return render_template('aboutus.html',details=[about_us_array[1],companysprofile,whychooseus_asset,ourmission])
    

@app.route('/contactus2/')
def contactus():
    
   return render_template('contactus2.html',contact=['text-danger',' Note: The form is not submitted yet'])
   

@app.route('/header-test3/<string:value>',methods=['GET','POST'])
def products(value):
    entries=0
    product_type=''
    if value=='0':
        entry = client.entries({'content_type':"waterSolubleFertilisers"})
        entries=entry
        print("the value of entries is ",entries)
        product_type='NPK Water Soluble Fertilizers'
    if value=='1':
        entry = client.entries({'content_type':"waterSoluble"})
        entries=entry
        product_type='Water Soluble'
    if value=='2':
        entry = client.entries({'content_type':"specialitywatersoluble"})
        entries=entry
        product_type='Speciality Water Soluble Fertilisers'
    if value=='3':
        entry = client.entries({'content_type':"edtaMicronutrients"})
        entries=entry
        product_type='EDTA Micro Nutrients'
    if value=='4':
        entry = client.entries({'content_type':"growthPromoters"})
        entries=entry
        product_type='Growth Promoters'
    if value=='5':
        entry=client.entries({'content_type':'micronutrients'})
        entries=entry
        product_type='Micro Nutrients'
    object_dict={}
    for x in entries:
        dictionary={"name":x.name,}
        name=""+x.name
        image_asset=x.fields()['product_image']
        print("the image url is ",image_asset.url())
        dictionary['image_url']=image_asset.url()
        print(name)
        features1=x.features
        features1=features1.split('.')
        dictionary['features']=features1
        print(dictionary)
        object_dict[name]=dictionary
        print(object_dict)
        
    return render_template('header-test3.html',details=[object_dict,product_type])

@app.route('/main')
def main():
    return render_template('home_page.html')


if __name__=='__main__':
    app.run(debug=True) 
