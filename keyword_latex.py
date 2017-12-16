from urllib.parse import quote

def keyword_latex(Input):
    query = "https://latex.codecogs.com/gif.latex?%5Cdpi%7B300%7D%5Cbg_white&space;"+quote(Input)

    # outputkan link gambar LaTeX
    return(query)    
