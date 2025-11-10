import random
def mesclar_equipos(equipos):
    """
    Mezcla aleatoriamente la lista de equipos.
    :param equipos: Lista de nombres de equipos.
    :return: Lista de equipos mezclada.
    """
    random.shuffle(equipos)
    return(equipos)
    