import wikipedia

def keyword_wiki(Input):
    # ngecek apakah ingin wikipedia berbahasa lain
    if Input[0] == '-':
        wikipedia.set_lang(Input[1:3])
        Input=Input[4:]

    # jika ngga ada, set ke bahasa inggris
    else:
        wikipedia.set_lang('en')

    # coba dapatkan rangkuman halaman wikipedia
    try:
        page = wikipedia.page(Input)
        text = page.summary.split('\n')[0]
        text+= '\n\n' + page.url
        return(text)

    # jika error karena Input-nya ambigu, outputkan.
    except wikipedia.exceptions.DisambiguationError as e:
        text = '"'+Input+'" may refer to:\n'
        for x in e.options:
            text += x+'\n'
        return(text[:-1])
