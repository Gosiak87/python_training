def song_generator():
    song ="""Wlazł kotek na płotek
                i mruga,
                ładna to piosenka,
                nie długa.
                Nie długa, nie krótka,
                lecz w sam raz,
                zaśpiewaj koteczku,
                jeszcze raz."""

    lines = song.splitlines()    #
    for word in lines:
            yield word


for word in song_generator():
    print(word)
