print("Please input all letters in lowercase form")
fo = open("wordleans.txt","r")
b1 = "z"
as1 = 0
x = True
if x:
    z1 = input("Input your first green letter")
    z11 = int(input("Place"))
    z11 = z11 - 1 
    x1 = input("Do you have any more letters y/n")
    as1 += 1
    if x1 == "n":
        x = False
if x:
    z2 = input("Input your second green letter")
    z21 = int(input("Place"))
    z21 = z21 - 1
    x2 = input("Do you have any more letters y/n")
    as1 += 1
    if x2 == "n":
        x = False
if x:
    z3 = input("Input your third green letter")
    z31 = int(input("Place"))
    z31 = z31 - 1
    x3 = input("Do you have any more letters y/n")
    as1 += 1
    if x3 == "n":
        x = False
if x:
    z4 = input("Input your fourth green letter")
    z41 = int(input("Place"))
    z41 = z41 - 1 
    as1 += 1
sad = False
sad1 = False
sad2 = False
sad3 = False
sad4 = False
x23 = True
ques = input("Do you have any yellow letters y/n")
if ques == "y":
    uncon = input("What is your first yellow letter")
    sad = True
    ques2 = input("Do you have any more yellow letters y/n")
    if ques2 != "y":
        x23 = False
if x23 and ques == "y":
    uncon1 = input("What is your second yellow letter")
    sad1 = True
    ques3 = input("Do you have any more yellow letters y/n")
    if ques3 != "y":
        x23 = False
if x23 and ques == "y":
    uncon2 = input("What is your third yellow letter")
    sad2 = True
    ques4 = input("Do you have any more yellow letters y/n")
    if ques4 != "y":
        x23 = False
if x23 and ques == "y":
    uncon3 = input("What is your fourth yellow letter")
    sad3 = True


if sad and sad1 and sad2 and sad3:
    numbre1 = 4
elif sad and sad1 and sad2:
    numbre1 = 3
elif sad and sad1:
    numbre1 = 2
elif sad:
    numbre1 = 1
elif sad == False:
    numbre1 = 0
    
if as1 == 1:
    for a in fo:
        if a[z11] == z1[0]:
            if numbre1 == 1:
                if uncon in a:
                    print(a)
            if numbre1 == 2:
                if uncon in a and uncon1 in a:
                    print(a)
            if numbre1 == 3:
                if uncon in a and uncon1 in a and uncon2 in a:
                    print(a)
            if numbre1 == 4:
                if uncon in a and uncon1 in a and uncon2 in a and uncon3 in a:
                    print(a)
            if numbre1 == 0:
                print(a)
if as1 == 2:
    for a1 in fo:
        if a1[z11] == z1[0] and a1[z21] == z2[0]:
            if numbre1 == 1:
                if uncon in a1:
                    print(a1)
            if numbre1 == 2:
                if uncon in a1 and uncon1 in a1:
                    print(a1)
            if numbre1 == 3:
                if uncon in a1 and uncon1 in a1 and uncon2 in a1:
                    print(a1)
            if numbre1 == 4:
                if uncon in a1 and uncon1 in a1 and uncon2 in a1 and uncon3 in a1:
                    print(a1)
            if numbre1 == 0:
                print(a1)
if as1 == 3:
    for a2 in fo:
        if a2[z11] == z1[0] and a2[z21] == z2[0] and a2[z31] == z3[0]:
            if numbre1 == 1:
                if uncon in a2:
                    print(a2)
            if numbre1 == 2:
                if uncon in a2 and uncon1 in a2:
                    print(a2)
            if numbre1 == 3:
                if uncon in a2 and uncon1 in a2 and uncon2 in a2:
                    print(a2)
            if numbre1 == 4:
                if uncon in a2 and uncon1 in a2 and uncon2 in a2 and uncon3 in a2:
                    print(a2)
            if numbre1 == 0:
                print(a2)
if as1 == 4:
    for a3 in fo:
        if a3[z11] == z1[0] and a3[z21] == z2[0] and a3[z31] == z3[0] and a3[z41] == z4[0]:
            if numbre1 == 1:
                if uncon in a3:
                    print(a3)
            if numbre1 == 2:
                if uncon in a3 and uncon1 in a3:
                    print(a3)
            if numbre1 == 3:
                if uncon in a3 and uncon1 in a3 and uncon2 in a3:
                    print(a)
            if numbre1 == 4:
                if uncon in a3 and uncon1 in a3 and uncon2 in a3 and uncon3 in a3:
                    print(a3)
            if numbre1 == 0:
                print(a3)
print("The above letters are all possibilitys")