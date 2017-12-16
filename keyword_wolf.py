from urllib.parse import quote
import requests

def keyword_wolf(Input):
    # dapatkan hasil dari WolframAlpha
    query= "https://api.wolframalpha.com/v2/query?input="+quote(Input)+"&format=image,plaintext&output=JSON&appid=APP-ID"
    temp = requests.get(query)
    temp = temp.json()
    temp = temp['queryresult']

    # jawaban terletak pada key pods, cek apakah key tersebut ada
    if 'pods' not in temp:
        if 'didyoumeans' in temp:
            return('Did you means:\n' + temp['didyoumeans'][0]['val'] + '?')
        else:
            return('Check your spelling, and use English')
    else:
        temp = temp['pods']

        # ngegabungkan jawaban-jawaban dalam satu string
        text= ''
        for x in temp:
            title = x['title']+':\n'
            value = ''
            for y in range(len(x['subpods'])):
                if x['subpods'][y]['plaintext'] != '':
                    value += x['subpods'][y]['plaintext']+'\n'
            if value=='':
                pass
            else:
                text+= title+value+'\n'
        return(text[:-2])
