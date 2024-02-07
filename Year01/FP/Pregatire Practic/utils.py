def generate_id(tractors_list):
    ids = []
    for obj in tractors_list:
        ids.append(obj.getId())

    if len(ids) == 0:
        return 1
    else:
        return max(ids) + 1
