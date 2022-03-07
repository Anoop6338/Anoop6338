email = input("Enter your email id: ")
# eg of shortest email g@g.in
k,j,p=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if (email[-4]==".") ^( email[-3]=="."):
            if ("@" in email) and (email.count("@")==1):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                        else:
                            continue
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==2 or p==1:
                    print("wrong email.... may have used space or upper alphabets or any other symbol")
                else:
                    print("Your email is correct!!")
            else:
                print(" wrong email.... not used @ symbol or used more than 1 time")
        else:
            print(" wrong email.... (.) dot is not used on its place")
    else:
        print(" wrong email.... 1st letter is a number")
else:
    print(" wrong email.... lenght is short")