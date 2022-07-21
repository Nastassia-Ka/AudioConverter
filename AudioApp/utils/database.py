from ..models import TrackData

def write_database(data_dict : dict) ->bool :
    """Сохраняет данные о треке в базу данных"""

    login :str = data_dict.get('user_name', '')
    trek_name :str = data_dict.get('trek_name', '')
    original_format  :str = data_dict.get('original_format', '')
    original_tracks :str = data_dict.get('path_original', '')
    convertable_tracks :str = data_dict.get('path_convert', '')
    convertable_format :str= data_dict.get('format', '')
    date :str = data_dict.get('date', '')

    try:
        database :TrackData = TrackData(login=login, trek_name=trek_name, original_format=original_format,
                          original_tracks=original_tracks, convertable_tracks=convertable_tracks,
                          convertable_format=convertable_format, date=date)
        database.save()
    except:
        raise Exception('Error writing to database')
    return True