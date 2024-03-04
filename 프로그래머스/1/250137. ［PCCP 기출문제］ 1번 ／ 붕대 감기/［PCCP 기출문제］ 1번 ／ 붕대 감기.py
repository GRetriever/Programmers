def solution(bandage, health, attacks):
    time = 0
    band_time = 0
    hp = health
    
    attack = {key:value for key,value in attacks}
    
    while attacks[-1][0] > time:
        time += 1
        
        if time in attack:
            hp -= attack[time]
            band_time = 0
        else:
            hp += bandage[1]
            band_time += 1
            if band_time == bandage[0]:
                hp += bandage[2]
                band_time = 0
        if hp > health:
            hp = health
        elif hp <= 0:
            return -1
    
    return hp