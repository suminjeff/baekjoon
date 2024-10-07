def get_processed_music(music):
    result = []
    for note in music:
        if note == '#':
            last_note = result.pop()
            result.append(last_note.lower())
        else:
            result.append(note)
    return ''.join(result)

def get_processed_time(time):
    hour, minute = map(int, time.split(':'))
    return hour*60 + minute

def get_played_music(music, playtime):
    played_music = ''
    for t in range(playtime):
        played_music += music[t%len(music)]
    return played_music

def rabin_karp(string, substring):
    n, m = len(string), len(substring)
    # 찾고자 하는 substring의 길이가 string보다 길다면 False
    if n < m:
        return False
    
    target = hash(substring)
    print(string)
    for i in range(n-m+1):
        tmp = hash(string[i:i+m])
        if tmp == target:
            return True
    return False

def solution(m, musicinfos):
    answer = ''
    m = get_processed_music(m)
    result = []
    for idx in range(len(musicinfos)):
        musicinfo = musicinfos[idx]
        start_time, end_time, title, music = musicinfo.split(',')
        music = get_processed_music(music)
        playtime = get_processed_time(end_time) - get_processed_time(start_time)
        played_music = get_played_music(music, playtime)
        is_match = rabin_karp(played_music, m)
        if is_match:
            result.append([playtime, idx, title])
    if result:
        result.sort(key=lambda x:(-x[0], x[1]))
        answer = result[0][2]
    else:
        answer = '(None)'
    return answer