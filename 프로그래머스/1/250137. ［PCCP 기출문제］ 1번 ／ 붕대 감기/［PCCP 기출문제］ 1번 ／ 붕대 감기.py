def solution(bandage, health, attacks):
    time = 0
    band_time = 0
    hp = health
    
    attack = {}
    for i,j in attacks:
        attack[i] = j
        
    while True:
        time += 1
        if attacks[-1][0] < time:
            break
        if time in attack:
            hp -= attack[time]
            band_time = 0
        else:
            band_time += 1
            hp += bandage[1]
            if band_time == bandage[0]:
                hp += bandage[2]
                band_time = 0
        if hp > health:
            hp = health
        if hp <= 0:
            return -1
    return hp