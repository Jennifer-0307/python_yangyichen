while True:
    月份=int(input('你輸入的月份'))
    日期=int(input('你輸入的日期'))
    if 月份==1 or 月份==2 or 月份==3 or 月份==4 or 月份==5 or 月份==6 or 月份==7 or 月份==8 or 月份==9 or 月份==10 or 月份==11 or 月份==12: 
        if 月份==1: 
            if 日期>=21:
                print('你是水瓶座')
            else:
                print('你是摩羯座') 
        if 月份==2: 
            if 日期>=19:
                print('你是雙魚座')
            else:
                print('你是水瓶座') 
        if 月份==3: 
            if 日期>=21:
                print('你是牡羊座')
            else:
                print('你是雙魚座') 
        if 月份==4: 
            if 日期>=21:
                print('你是金牛座')
            else:
                print('你是牡羊座') 
        if 月份==5: 
            if 日期>=22:
                print('你是雙子座')
            else:
                print('你是金牛座')
        if 月份==6:
            if 日期>=22:
                print('你是巨蟹座')
            else:
                print('你是雙子座')
        if 月份==7: 
            if 日期>=21:
                print('你是獅子座')
            else:
                print('你是巨蟹座') 
        if 月份==8: 
            if 日期>=24:
                print('你是處女座')
            else:
                print('你是獅子座')
        if 月份==9: 
            if 日期>=24:
                print('你是天秤座')
            else:
                print('你是處女座')
        if 月份==10: 
            if 日期>=24:
                print('你是天蠍座')
            else:
                print('你是天秤座')         
        if 月份==11: 
            if 日期>=23:
                print('你是射手座')
            else:
                print('你是天蠍座') 
        if 月份==12: 
            if 日期>=22:
                print('你是魔羯座')
            else:
                print('你是射手座')
    else:
        print('你輸入錯了喔')
        break
        

