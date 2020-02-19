
def doctor_visit(jon_ah, doc_ah):
    if len(doc_ah) < len(jon_ah):
        print("go")
    else:
        print("no")


while True:
    #0-999 a's and h at the end

    jon = input("Jon: ")
    doc = input("Doc: ")

    if jon[-1] == 'h' or doc[-1] == 'h':
        if len(jon[0: len(jon) - 1]) <= 999 and len(doc[0:len(doc) - 1]) <= 999:
            if set(jon) == {'a', 'h'} or set(jon) == {'h'} and set(doc) == {'a', 'h'} or set(doc) == {'h'}:
                doctor_visit(jon, doc)
                break
    else:
        continue




# if "a" in set(doc[:]):
#     print("yes")
#
# ssl = doc[0:len(doc)]
# sst = set(doc[0:len(doc)])
# ss = list(set(doc[0:len(doc)]))assddddd
# print(len(ssl))
# print(ssl)
#
# if len(set(doc[0:len(doc)])) and len(set(jon[0:len(jon)])) <= 2:
#     if doc[0] == 'h' or 'a' and jon[0] == 'h' or 'a':
#         print("YYYY")


# print(len(doc))
# print({'a', 'h'}=={'h','a'})
# s1 = set(doc)
# print(s1 == {'h', 'a'})
# print(s1)
# print("length of a's: ", len(doc[0: len(doc) - 1]))

