# Задача №2 "Аудиоколлекция". Продолжение
class Track:
    def __init__(self, title, duration: int):
        self.title = title
        self.duration = duration

    def __str__(self):
        return str(f'{self.title}-'
                   f'{self.duration}min')

    def __lt__(self, other):
        if not isinstance(self, Track) and not isinstance(other, Track):
            return "Not a Track!"
        return self.duration < other.duration

    def __eq__(self, other):
        if not isinstance(self, Track) and not isinstance(other, Track):
            return "Not a Track!"
        return self.duration == other.duration


class Album:
    def __init__(self, title, group, list_tracks: list):
        self.title = title
        self.group = group
        self.list_tracks = list_tracks

    def get_tracks(self):
        list_track_info = []
        for track in self.list_tracks:
            list_track_info.append(track)
        return list_track_info

    def add_track(self, track: Track):
        if not isinstance(track, Track):
            return
        self.list_tracks.append(track)

    def get_duration(self):
        duration_all_tracks = 0
        for track in self.list_tracks:
            duration_all_tracks = duration_all_tracks + track.duration
        return duration_all_tracks

    def __str__(self):
        list_out = ''
        for track in self.list_tracks:
            list_out = list_out + ('        ' +
                                   track.title + '-' +
                                   str(track.duration) +
                                   'min\n')
        return str(f'Name group: {self.group}\n'
                   f'Name album: {self.title}\n'
                   f'Tracks:\n' + list_out)


def main():
    kino_1 = Track('Группа крови', 5)
    kino_2 = Track('Спокойная ночь', 6)
    kino_3 = Track('В наших глазах', 4)
    kino_4 = Track('Легенда', 4)
    kino_list = [kino_1, kino_2, kino_3]

    ariya_1 = Track('Раскачаем этот мир', 6)
    ariya_2 = Track('Раб страха', 5)
    ariya_3 = Track('Бой продолжается', 6)
    ariya_4 = Track('Искушение', 4)
    ariya_list = [ariya_1, ariya_2, ariya_3]

    album_kino = Album('Группа крови', 'Кино', kino_list)
    album_ariya = Album('Игра с огнём', 'Ария', ariya_list)

    album_kino.add_track(kino_4)
    album_ariya.add_track(ariya_4)

    print(kino_3)
    print(ariya_2)
    print()
    print(album_kino)
    print(album_ariya)
    print(kino_2 == ariya_3)


if __name__ == '__main__':
    main()
