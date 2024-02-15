def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object,type(object))
    elif isinstance(object, float) and object != object:
        print("NaN:", object,type(object))
    elif isinstance(object, int) and object == 0:
        print("Zero:", object,type(object))
    elif isinstance(object, str) and not object:
        print("Empty:", object,type(object))
    elif isinstance(object, bool) and not object:
        print("False:", object,type(object))
    else:
        print("Type not found")
        return 1
    return 0 