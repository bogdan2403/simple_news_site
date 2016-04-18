page = 1


def pages(list_obj, count_on_page=5):
    list_obj = list(reversed(list_obj))
    global page
    page = int(page)
    start = (page - 1) * count_on_page
    end = start + count_on_page
    obj_on_page = list_obj[start:end]
    return list(obj_on_page)
