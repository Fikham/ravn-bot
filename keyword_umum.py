# pemrosesan keyword umum (file dari datacsv)

import csv
umum = {}

with open('datacsv/umum.csv',newline='') as csvfile:            # delimiternya '|', karena ini jarang dipakai
    baris  = csv.reader(csvfile,delimiter='|')                  # kalau ','... bisa jadi hancur.
    temp   = []
    for x in baris:                                             # intinya, sekarang isi ultah_csv
        temp.append(x)              				# ada di variabel temp

umum = {temp[i][0]:temp[i][1].replace('\\n','\n')
        for i in range(len(temp))}                              # ubah temp (tipe list) jadi umum (tipe dict)

def cek_umum(Input,umum=umum):
    if Input in Input in umum:
        return(True)                                            # Inputnya ada di umum kategori umum, alias disini
    else:
        return(False)
def keyword_umum(Input, umum=umum):
    return(umum[Input])
