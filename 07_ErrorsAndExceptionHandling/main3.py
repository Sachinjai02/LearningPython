def ask_for_int():
    while True:
        try:
            result = int(input("Provide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            break
        finally:
            print("End of try except finally")

    return result

ask_for_int()
