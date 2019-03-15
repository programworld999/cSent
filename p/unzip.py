import zipfile as zipf

fantasy_zip = zipf.ZipFile('./p.zip')

fantasy_zip.extractall('./p')

fantasy_zip.close()