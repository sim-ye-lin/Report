s=0
while True:
    name=input("제품명:")
    items={"라면":650,"우유":1100,"콜라":1200,"캔커피":500,"과자":700}
    

    if name in items:
        s=s+items[name]
        print("[%s:%d]>%d"%(name,items[name],s))
        

    else:
        if name!="":
            print(name,"는 미등록 제품입니다.")

        else:
            print("총 금액:",s)
            break
            
    
   




