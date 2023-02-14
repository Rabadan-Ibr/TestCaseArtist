from datetime import date

from rest_framework.exceptions import ValidationError


def max_year(data):
    message = 'the year cannot be longer than the current one'
    if data.get('year') > date.today().year:
        raise ValidationError({'year': message})
    return True


def songs_validator(data):
    songs_data = data.get('songs_m2m')
    songs_set, positions_set = set(), set()
    for song_data in songs_data:
        songs_set.add(song_data.get('song').get('id').id)
        positions_set.add(song_data.get('position'))
    if len(songs_set) < len(songs_data):
        raise ValidationError({'songs': 'songs must be unique'})
    if len(positions_set) < len(songs_data):
        raise ValidationError({'position': 'position must be unique'})
