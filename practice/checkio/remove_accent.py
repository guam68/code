import unicodedata
def checkio(in_string):
    accented = {ord("à"): "a", ord("é"): "e", ord("è"): "e", ord("ớ"): "o"}

    print(in_string.translate(str.maketrans(accented)))
    print(len(in_string))
    # return in_string.translate(str.maketrans(acented, output)) 

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
