#清單與定義的用法
def add_add():#定義add_add

    print('購物清單',shopping_list)
    add=input()
    shopping_list.append(add)#在清單尾部添加新項目
    print('購物清單',shopping_list)
    return shopping_list
def remove_remove():#定義remove_remove
    
    print('購物清單',shopping_list)
    remove=input()
    shopping_list.remove(remove)#移除shopping_list裡面的事物
    print('購物清單',shopping_list)
shopping_list=[]


shop=['add_add','remove_remove']
number=1
for i in shop:
    print(number,i)
    number=number+1 #等同於number+=1
while True:
    a=int(input('你要加入購物物清單還是移除購物清單'))
    if a==(1):
       add_add()       
    elif a==(2):
        lengh=len(shopping_list)#定義shopping_list字彙長度的方法
        if lengh>=1:#判斷清單裡面是否有東西以免沒東西#也可以放在def remove_remove裡面#放在remove_remove()前面且在while True迴圈裡
            remove_remove()
        else:
            print("沒東西囉")
            break

#駝峰命名法-EX:以first second等兩字或兩字以上當名字，通常寫法是:firstSecond         