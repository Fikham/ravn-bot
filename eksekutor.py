# bisa dikatakan ini 'bagian utama' bot LINE ini.
# perlu ditekankan implementasi yang saya lakukan masih sederhana.

# keyword yang bertipe text.Message
from keyword_umum  import keyword_umum, cek_umum, umum
from keyword_kbbi  import keyword_kbbi
from keyword_trans import keyword_trans
from keyword_wiki  import keyword_wiki
from keyword_wolf  import keyword_wolf

# keyword yang bertipe Image.Message
from keyword_latex import keyword_latex

# fungsi ini akan memproses Input, dan mengoutputkan cara LINE
# menjawab (dikirim sebagai Text atau Image) dan jawabannya
def Process(Input):
    if cek_umum(Input):
        return(keyword_umum(Input.lower()))
    elif Input[ :5] == '!kbbi':
        return ['Text', keyword_kbbi(Input[6:].lower())]
    elif Input[ :5] == '!wolf':
        return ['Text', keyword_wolf(Input[6:].lower())]
    elif Input[ :5] == '!wiki':
        return ['Text', keyword_wiki(Input[5:])]
    elif Input[ :6] == '!trans':
        return ['Text', keyword_trans(Input[7:])]
    elif Input[ :6] == '!latex':
        return ['Image', keyword_latex(Input[7:])]
    else:
        return [None,None]

# ini dipakai hanya untuk debug
#while True:
#    a = input()
#    print(Result(a))
