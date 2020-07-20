import requests, zipfile
from io import StringIO

import io

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00356/student.zip'

r = requests.get(url=url, stream=True)

z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
