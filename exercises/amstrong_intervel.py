lolmt=100
uprlmt=200
sum=0
for num in range(lolmt,uprlmt+1):
    main=num
    while num>0:
        num1=num%10
        sum=sum+num1**3
        num=num//10
        if main==sum:
            print('amstrong')



