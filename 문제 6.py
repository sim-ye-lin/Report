engkor_dict=dict()
while True:
    eng=str(input("영어 단어:"))
    kor=str(input("한글 단어:"))


    if eng!="" and kor!="":
        engkor_dict[eng]=kor
    

    else:
        print(engkor_dict)
        break


