from xml.dom import NO_DATA_ALLOWED_ERR


ex_d=int(input("enter number"))
ex_m=int(input("enter number"))
ex_y=int(input("enter number"))
return_d=int(input("enter number"))
return_m=int(input("enter number"))
return_y=int(input("enter number"))
if ex_m==return_m and ex_y==return_y:
    if return_d<=ex_d:
        print("no find")
    elif return_d>ex_d:
        n_d_l = ex_d-return_d
        fine=15*n_d_l
        print("fine")
elif return_m>ex_m and return_y==ex_y:
    if return_d==ex_d:
        n_d_l = ex_m-return_m
        fine=500*n_d_l
        print("fine")
    else:
        print("finr charge")
elif return_m==ex_m and return_y>ex_y:
    if return_d==ex_d:
        fixed=fine=10000
        print("fixed fine")
else:
    print("no fixed fine")
