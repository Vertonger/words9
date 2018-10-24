import io
import os

def rate():
    f = io.open('word/rating/players.txt', 'r', encoding='utf-8')
    text = f.read()
    f.close()
#   a = len(text)
    i = 0
    c = text.count('=')
    e = 0
    player_ID = []
    while i < c:
        number1 = text.find('=', e+1)
        number2 = text.find('\n', e+1)
        rate_ID = [text[number1+2:number2]]
        player_ID+=rate_ID
        i+=1
        e = number2
        #player_ID.sort()
    player_name = []
    i = 0
    e = 0
    while i < c:
        number1 = text.find('=', e+1)
        number2 = text.find('\n', e+1)
        rate_name=[text[e+1:number1]]
        player_name+=rate_name
        i+=1
        e = number2
    i = 0
    #player_copy = player_name.copy()
    rate_count = 0
    score = []
    zero_players = []
    players0 = 0
    while i < c:
        if os.path.exists('log/' + player_ID[i] + '.R.word.txt'):
            f = io.open('log/' + player_ID[i] + '.R.word.txt', 'r', encoding='utf-8')
            S = int(f.read())
            f.close()
            score+=[S]
            rate_count+=1
        else:
            zero_players+=[player_name[i]]
            players0+=1
        i+=1
    i = 0
    while i < rate_count - 1:
        j = 0
        while j < rate_count - 1 - i:
            if score[j] < score [j+1]:
                number1 = score[j+1]
                score[j+1] = score[j]
                score [j] = number1
                number2 = player_name[j+1]
                player_name[j+1] = player_name[j]
                player_name[j] = number2
            j+=1
        i+=1
    i = 0
    q = io.open('word/rating/rating.txt', 'w', encoding='utf-8')
    q.write("Рейтинг игроков по количеству правильных ответов:\n")
    q.close()
    q1 = io.open('word/rating/rating.txt', 'a', encoding='utf-8')
    while i < rate_count:
        q1.write(str(i+1) + ") " + str(player_name[i]) + " -  " + str(score[i]) + "\n")
        i+=1
#        players = i
    j = 0
    while j < players0:
        q1.write(str(j+i+1) + ") " + str(zero_players[j]) + " -  0\n")
        j+=1
    q1.close()
