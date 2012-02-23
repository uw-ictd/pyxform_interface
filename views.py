# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms

import datetime
import tempfile
import os

import pyxform
from pyxform import xls2json

SERVER_TMP_DIR = '/tmp'

class UploadFileForm(forms.Form):
    file  = forms.FileField()

def handle_uploaded_file(f, temp_dir):
    xls_path = os.path.join(temp_dir, f.name)
    destination = open(xls_path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return xls_path

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UploadFileForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            error = None
            warnings = None
            
            filename, ext = os.path.splitext(request.FILES['file'].name)
            
            #Make a randomly generated directory to prevent name collisions
            temp_dir = tempfile.mkdtemp(dir=SERVER_TMP_DIR)
            xml_path = os.path.join(temp_dir, filename + '.xml')
            
            #Init the output xml file.
            fo = open(xml_path, "wb+")
            fo.close()
            
            try:
                #TODO: use the file object directly
                xls_path = handle_uploaded_file(request.FILES['file'], temp_dir)
                warnings = []
                json_survey = xls2json.parse_file_to_json(xls_path, warnings=warnings)
                survey = pyxform.create_survey_element_from_dict(json_survey)
                survey.print_xform_to_file(xml_path)
                
            except Exception as e:
                error = 'Error: ' + str(e)
            
            return render_to_response('result.html', {
                'xml_path' : '.' + xml_path,
                'error': error,
                'warnings': warnings
            })
    else:
        form = UploadFileForm() # An unbound form
        
    return render_to_response('upload.html', {
        'form': form,
    })
    
def serve_xform(request, path):
    fo = open(os.path.join(SERVER_TMP_DIR,path))
    data = fo.read()
    fo.close()
    response = HttpResponse(mimetype='application/octet-stream')
    #response['Content-Disposition'] = 'attachment; filename=somefilename.xml'
    response.write(data)
    return response