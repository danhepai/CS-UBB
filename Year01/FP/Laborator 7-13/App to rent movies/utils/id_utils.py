def generate_id(data):
    """
    Generates a new id for a movie or a client
    :param data: the repository of movies or clients -> list
    :return: a new id
    """
    ids = []
    for obj in data:
        ids.append(int(obj.getId()))
    if len(ids) == 0:
        return 1
    return str(max(ids) + 1)
