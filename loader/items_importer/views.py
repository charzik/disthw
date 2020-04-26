from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import UploadFileForm
from . import tasks

import csv

class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, format=None):
        file = request.FILES['file']
        with open(file.temporary_file_path()) as fin:
            csv_reader = csv.DictReader(fin, delimiter=',')
            chunk_size = 1000
            chunk = list()
            unique_ids = set()
            for line in csv_reader:
                if line['uniq_id'] not in unique_ids:
                    unique_ids.add(line['uniq_id'])
                    if len(chunk) == chunk_size:
                        tasks.insert_items.delay(chunk)
                        chunk = list()
                    
                    new_item = {
                        'name': line['product_name'],
                        'category': 'imported item',
                        'price': line['price']
                    }
                    chunk.append(new_item)
            if len(chunk) > 0:
                tasks.insert_items.delay(chunk)

        return Response(status=200)