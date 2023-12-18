#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for idx in range(list_length):
        try:
            my_list.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            my_list.append(0)
            print("division by 0")
            continue
        except IndexError:
            my_list.append(0)
            print("out of range")
            continue
        except TypeError:
            my_list.append(0)
            print("wrong type")
            continue
        finally:
            pass
    return my_list
