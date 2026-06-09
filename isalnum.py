i=1
while(i<=5):
    usr=input("enter user name.....:")
    x=usr.isalnum()
    if x==True:
        flag=1
        break
    i+=1
else:
        print("sorry try again ")
        