import csv
# maaf, saya tidak yakin dapat mengupload kode yang terbaru.
# buat dict kosong yang akan terisi kata dan definisinya
kamus = {}

with open('data/kamus.csv',newline='') as csvfile:
    # delimiternya '|', karena ini jarang dipakai
    # kecil kemungkinannya untuk error dalam pemprosesan
    baris  = csv.reader(csvfile,delimiter='|')
    temp   = []
    for x in baris:
        temp.append(x)

for i in range(len(temp)):
    # jika kata belum ada dikamus, buat key baru
    if temp[i][0] not in kamus:
        kamus[temp[i][0]] = temp[i][1] + '.'

    # jika sudah ada (misal, ini definisi keduanya)
    # tambahkan ke data yang sudah ada
    else:
        kamus[temp[i][0]]+= '\n\n' + temp[i][1] + '.'

def keyword_kbbi(Input, kamus=kamus):
    # outputkan definisi KBBI dari Input
    if Input in kamus:
        return(kamus[Input])
    else:
        return("Definisi untuk "+Input+" tidak ditemukan")
