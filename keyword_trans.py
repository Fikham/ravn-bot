from urllib.parse import quote
import requests

def keyword_trans(Input):
    # contoh Input = "en id TEKS YANG MAU DIUBAH"
    # dapatkan kode bahasa, dan atur agar sesuari query
    lang_id = Input[:5].replace(' ','|')
    query   = "http://api.mymemory.translated.net/get?q="+quote(Input[6:])+"&langpair="+lang_id
    temp    = requests.get(query)
    temp    = temp.json()

    # outputkan hasil pertama
    return(temp['matches'][0]['translation'])
