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

def get_prefix_pointer(string):
    prefix_pointer = [0]*len(string)
    j = 0  # 접두사 포인터
    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = prefix_pointer[j-1]
        if string[i] == string[j]:
            j += 1
            prefix_pointer[i] = j
    return prefix_pointer

def kmp(string, substring):
    if len(substring) > len(string):
        return False
    
    # KMP 알고리즘에 필요한 접두사 포인터 배열
    prefix_pointer = get_prefix_pointer(substring)
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != substring[j]:
            j = prefix_pointer[j-1]
    
        # 문자가 일치하면 j를 증가시켜 계속 탐색
        if string[i] == substring[j]:
            j += 1
            # 패턴 전체가 일치했으면 True 반환
            if j == len(substring):
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
        is_match = kmp(played_music, m)
        print(is_match)
        if is_match:
            result.append([playtime, idx, title])
    if result:
        result.sort(key=lambda x:(-x[0], x[1]))
        answer = result[0][2]
    else:
        answer = '(None)'
    return answer