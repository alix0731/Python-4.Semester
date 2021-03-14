
dict = {"jan" : 1, "feb" : 2, "mar" : 3, "apr" : 4, "maj" : 5, "juni" : 6, "juli" : 7, "aug" : 8, "sep" : 9, "okt" : 10, "nov" : 11, "dec" : 12}


#   1.Jeg starter med at gør variablen til string da funktionen ikke ved hvilken data type det er samt deler ordet op i en list hvor der er -
#   2.Derefter udskifter jeg det der er i liste[1] med value fra dictionary
def date(date):
    list = str(date).split("-")
    list[1] = dict[list[1]]
    result = list[0] + "-" + str(list[1]) + "-" +  list[2]
    return result
    

print(date(input("enter a date 'dd-mmm-yy': ")))