def get_processed_time(time):
    hour, minute = map(int, time.split(':'))
    return hour*60 + minute


def calculate_playtime(start_time, end_time):
    start, end = get_processed_time(start_time), get_processed_time(end_time)
    return end - start


def get_processed_notes(music_notes):        
    return music_notes.replace('C#', 'c').replace('D#', 'd').replace('E#', 'e').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b')


def solution(m, musicinfos):
    answer = ''
    answer_candidates = []
    
    # 기억하는 음 데이터 전처리
    processed_m = get_processed_notes(m)
    
    # 음악 정보 순회
    for idx in range(len(musicinfos)):
        musicinfo = musicinfos[idx]
        start_time, end_time, title, music_notes = musicinfo.split(',')
        
        # 곡 재생시간(playtime) 계산
        playtime = calculate_playtime(start_time, end_time)

        # 음악 음 데이터 전처리
        processed_music_notes = get_processed_notes(music_notes)
        length = len(processed_music_notes)
        
        # 음악 재생
        played_music = ''
        for t in range(playtime):
            music_note = processed_music_notes[t%length]
            played_music += music_note
        
        if processed_m in played_music:
            answer_candidates.append([playtime, idx, title])

    if answer_candidates:
        answer_candidates.sort(key=lambda x:(-x[0], x[1]))
        answer = answer_candidates[0][2]
    else:
        answer = '(None)'

    return answer