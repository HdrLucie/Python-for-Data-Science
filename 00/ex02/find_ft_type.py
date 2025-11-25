def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    if obj_type is str :
        print(object, "is in the kitchen")
    else :
        print(obj_type)
    return 42
