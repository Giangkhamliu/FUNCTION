def validate_usr(username):
    if len(username)>=4 and len(username)<=16:
        check="abcdefghijklmnopqrstuvwxyz0123456789_"
        i=0
        a=[]
        while i<len(username):
            if username[i] in check:
                a.append("true")
            else:
                a.append("false")
            i+=1
        if "false" in a:
            return False
        else:
            return True
    else:
        return False
print(validate_usr("asddsa"))
print(validate_usr("____"))
print(validate_usr("Hasd_12assssssasasasasasaasasasasas"))
print(validate_usr("wqert"))
print(validate_usr("'asd43 34'"))
print(validate_usr("p1p2"))
print(validate_usr("qr3th5yty"))