import requests
import json
import csv

doi = '10.5281/zenodo.7686433' # The metadata for the NEST building data points, https://zenodo.org/record/7686433#.ZAbwuHaZMUF
#doi = '10.5281/zenodo.5651108'  # Convocatorias Públicas de la Junta de Andalucía, https://zenodo.org/record/5651108#.ZAYobXaZMUE


def getfile(doi):
    url = 'https://doi.org/' + doi
    r = requests.get(url, timeout=12345)
    record_id = r.url.split('/')[-1]
    record_id = record_id.strip()
    url = 'https://zenodo.org/api/records/'
    r = requests.get(url + record_id, timeout=12345)

    if r.ok:
        js = json.loads(r.text)
        files = js['files']

        for f in files:
            fname = f['key']
            link = 'https://zenodo.org/record/{}/files/{}'.format(
                record_id, fname
            )
            data = requests.get(link)
            ftype = fname.split('.')[1]
            if ftype == 'json':
                jsonf = data.json()
                print(jsonf)
                # print(json[0]['_NUMERICID'])

            elif ftype == 'h5':
                print('We will support this')
            elif ftype == 'p':
                print('We will support this')
            elif ftype == 'csv':
                print('We will support this')
                #reader = csv.DictReader(data.text)
                #print(reader.fieldnames)
            elif ftype == 'zip':
                print('We will support this')


getfile(doi)
