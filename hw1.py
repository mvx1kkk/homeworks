def polindrome():
    string = str(input())
    if string == string[::-1]:
        print("True")
    else:
        print("False")

polindrome()

