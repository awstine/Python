#Cryting engine for a message



def crypt(statement):
    translation = ""
    for element in statement:
        if element in "Aa":
            translation = translation + "1"
        elif element in "Bb":
            translation = translation + "2"
        elif element in "Cc":
            translation = translation + "3"
        elif element in "Dd":
            translation = translation + "4"
        elif element in "Ee":
            translation = translation + "5"
        elif element in "Ff":
            translation = translation + "6"
        elif element in "Gg":
            translation = translation + "7"
        elif element in "Hh":
            translation = translation + "8"
        elif element in "Ii":
            translation = translation + "9"
        elif element in "Jj":
            translation = translation + "10"
        elif element in "Kk":
            translation = translation + "11"
        elif element in "Ll":
            translation = translation + "12"
        elif element in "Mm":
            translation = translation + "13"
        elif element in "Nn":
            translation = translation + "14"
        elif element in "Oo":
            translation = translation + "15"
        elif element in "Pp":
            translation = translation + "16"
        elif element in "Qq":
            translation = translation + "17"
        elif element in "Rr":
            translation = translation + "18"
        elif element in "Ss":
            translation = translation + "19"
        elif element in "Tt":
            translation = translation + "20"
        elif element in "Uu":
            translation = translation + "21"
        elif element in "Vv":
            translation = translation + "22"
        elif element in "Ww":
            translation = translation + "23"
        elif element in "Xx":
            translation = translation + "24"
        elif element in "Yy":
            translation = translation + "25"
        elif element in "Zz":
            translation = translation + "26"
        else:
            translation = translation + element
    return translation


print(crypt(input("What do you want to crypt: ")))
