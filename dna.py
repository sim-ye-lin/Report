def comp(seq):
    comp_dict={'A':'T','T':'A','C':'G','G':'C'}
    seq_comp=""
    for char in seq:
        seq_comp=seq_comp+comp_dict[char]
    return seq_comp

def rev(seq):
    seq_rev="".join(reversed(seq))
    return seq_rev

def rev_comp(seq):
    tmp=comp(seq)
    return rev(tmp)

while True:
    a=input("DNA sequence:")
    if a!="stop":
        if a=="":
            print("서열을 입력하세요.")
            continue
        

        else:
            if a!=str:#여기에 and 써서 A T C G 입력 안했을때도 밑의 문구 나오도록
                print("서열을 정확하게 입력하세요.")
                continue


            else:
                if len(a)!=6:
                    print("6자리의 서열을 정확하게 입력하세요.")#이부분 출력안됨
                    
                    continue

                else:
                    b=int(input("1(comp), 2(rev), 3(rev_comp):"))

                    if b>=1 and b<=3:
                        if b==1:
                            print(comp(a))
                        elif b==2:
                            print(rev(a))
                        elif b==3:
                            print(rev_comp(a))

                    else:
                        print("1에서 3중에 고르시오!")

        

    else:
        print("끝")
        break
