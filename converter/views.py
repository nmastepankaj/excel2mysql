from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from converter.models import Contact,UploadCSV
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
import csv

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('conName')
        email = request.POST.get('conMail')
        phone = request.POST.get('conPhone')
        desc = request.POST.get('conContant')
        contact = Contact(name = name,email= email, phone=phone,desc =desc,date =datetime.today())
        contact.save()
    return render(request,'contact.html')

# def validate_file(name):


def csv_upload(request):
    if request.method == 'POST' and request.FILES['filetoupload']:
        myfile = request.FILES['filetoupload']
        if not myfile.name.endswith('.csv'):
            return HttpResponse("Please Upload Only CSV file")
        fs = FileSystemStorage()
        file_name = fs.save("upload/"+myfile.name, myfile)
        filename = file_name.split('/')[1]
        # uploaded_file_url = fs.url("upload/"+filename)
        uploadFile = UploadCSV(csv_file_name = filename)
        uploadFile.save()
        # return render(request, 'convertToCSV.html', {
        #     'uploaded_file_name': filename
        # })
        response = redirect('/convertcsv/'+filename)
        return response
    return render(request, 'index.html')

def csv_convert(request,file_name):
    # fileName = request.GET.get('file_name')  
    print(file_name)
    downloadName = file_name.split('.')[0]+".sql"
    print(downloadName)
    if request.method == 'POST':
        table_name = request.POST.get('table_name')
        if request.POST.get('table_name') == "":
            table_name = "test"

        if request.POST.get('checkId'):
            auto_inc = '`id` int(255) NOT NULL AUTO_INCREMENT,'
            primary_key = ',PRIMARY KEY (`id`) '
        else:
            auto_inc = ""
            primary_key = ""
        file_object = open('files/download/'+downloadName, 'w')
        with open('files/upload/'+file_name,'r') as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=','))
            line_count = 0
            # print(csv_reader[0][0])
            for row in csv_reader:
            # Append 'hello' at the end of file
                if line_count == 0:
                    create_table = f'CREATE TABLE `{table_name}` ({auto_inc}'
                    j = len(csv_reader[0])
                    for column in row:
                        j = j - 1
                        if j != 1:
                            create_table += f'`{column}` varchar(1000) COLLATE utf8_unicode_ci  DEFAULT NULL'
                        else:
                            create_table += f'`{column}` varchar(1000) COLLATE utf8_unicode_ci  DEFAULT NULL ,'
                    create_table += f'{primary_key} ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1; \n \n \n \n'
                    file_object.write(create_table)
                    line_count += 1
                else:
                    no_of_column = len(csv_reader[0])
                    create_column = f'INSERT INTO `test` ('
                    for i in range(no_of_column):
                        if(i == no_of_column - 1):
                            create_column += f'`{csv_reader[0][i]}`'
                            continue
                        create_column += f'`{csv_reader[0][i]}`,'

                    create_column += ') values ('
            
                    i = 0
                    for column in row:
                
                        if(i == no_of_column - 1):
                            create_column += f'"{column}"'
                            i = i + 1
                            continue
                        create_column += f'"{column}",'
                        i = i + 1
                    create_column += '); \n'
                    file_object.write(create_column)
                    line_count += 1
        file_object.close()
        downloadData = UploadCSV.objects.get(csv_file_name = file_name)
        downloadData.sql_file_name = downloadName
        downloadData.save()
        return render(request, 'convertToCSV.html',{
            "downloadFile": downloadName
        })
    return render(request, 'convertToCSV.html')