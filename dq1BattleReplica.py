import sqlite3, random, os
os.system('cls' if os.name=='nt' else 'clear')  
# Initialze database
connection = sqlite3.connect(r'stats.db')
# Get player stats
print('Input four numbers, representing your Strength, Agility, HP and MP respectively:')
class Player:
    while True:
        try:
            strength = int(input('Strength: '))
            agility = int(input('Agility: '))
            HP = int(input('HP: '))
            MP = int(input('MP: '))
            break
        except:
            print('Please input an integer.')
            continue
    print('Enter your character name:')
    name = input()
    print("Input three ids representing your armor, shield and weapon respectively:")
    with connection:
        cursor = connection.cursor()
        while True:
            try:
                armorId = int(input('Armor: '))
                if armorId > 7 or armorId < 0:
                    print('Please input an exisiting id.')
                    continue
                cursor.execute('SELECT Name, Modifier FROM DQ1NFEQ WHERE Id=?', (armorId,))
                armorFetchall = cursor.fetchall()
                armorName = armorFetchall[0][0]
                armorModifier = armorFetchall[0][1]
                shieldId = int(input('Shield: '))
                if shieldId > 10 or shieldId < 8:
                    print('Please input an exisiting id.')
                    continue
                cursor.execute('SELECT Name, Modifier FROM DQ1NFEQ WHERE Id=?', (shieldId,))
                shieldFetchall = cursor.fetchall()
                shieldName = shieldFetchall[0][0]
                shieldModifier = shieldFetchall[0][1]
                weaponId = int(input('Weapon: '))
                if weaponId > 17 or weaponId < 11:
                    print('Please input an exisiting id.')
                    continue
                cursor.execute('SELECT Name, Modifier FROM DQ1NFEQ WHERE Id=?', (weaponId,))
                weaponFetchall = cursor.fetchall()
                weaponName = weaponFetchall[0][0]
                weaponModifier = weaponFetchall[0][1]
                totalModifier = armorModifier + shieldModifier
                break
            except:
                print('Please input an existing id.')
                continue
    defenese = int(agility / 2 // 1 + totalModifier)
    # Function for player fleeing
    def flee():
        groupFactor = {1: 0.25, 2: 0.375, 3: 0.5, 4: 1}
        if int(Enemy.id) <= 20:
            groupFactorValue = groupFactor.get(1)
        elif 21 <= int(Enemy.id) <= 30:
            groupFactorValue = groupFactor.get(2)
        elif 31 <= int(Enemy.id) <= 35:
            groupFactorValue = groupFactor.get(3)
        else:
            groupFactorValue = groupFactor.get(4)
        if Enemy.eSleep == True:
            print(Player.name, 'started to run away.')
            Player.fleeCheck = True
        elif Player.agility * random.randint(0, 255) > Enemy.agility * random.randint(0, 255) * groupFactorValue:
            print(Player.name, 'started to run away.')
            Player.fleeCheck = True
        else:
            print(Player.name, 'started to run away.\nBut was blocked in front.')
            Player.fleeCheck = False
    playerAttack = strength + weaponModifier
    # Function for attacking
    def attack():
        print(f'{Player.name} attacks!')
        if random.uniform(0, 1) <= Enemy.dodge:
            print('A miss! No damage hath been scored!')
        else:
            global eHP
            try:
                if random.randint(0, 31) == 0 and Enemy.name != 'Dragonlord' and Enemy.name != 'Dragonlord (Dragon form)':
                    print('Excellent move!')
                    toEAttackDamage = random.randint((int(Player.playerAttack / 2 // 1), int((Player.playerAttack // 1))))
                    print(f"The {Enemy.name}'s Hit Points has been reduced by {toEAttackDamage}.")
                    eHP -= toEAttackDamage
                else:
                    toEAttackDamage = random.randint(int((Player.playerAttack - Enemy.agility / 2) / 4 // 1), (int((Player.playerAttack - Enemy.agility / 2) / 2 // 1)))
                    if toEAttackDamage < 1:
                        if random.randint(0, 1) == 0:
                            toEAttackDamage = 0
                            print(f"The {Enemy.name}'s Hit Points has been reduced by {toEAttackDamage}.")
                            eHP -= toEAttackDamage
                        else:
                            toEAttackDamage = 1
                            print(f"The {Enemy.name}'s Hit Points has been reduced by {toEAttackDamage}.")
                            eHP -= toEAttackDamage
                    eHP -= toEAttackDamage
                    print(f"The {Enemy.name}'s Hit Points has been reduced by {toEAttackDamage}.")
            except:
                if random.randint(0, 1) == 0:
                    toEAttackDamage = 0
                    print(f"The {Enemy.name}'s Hit Points has been reduced by {toEAttackDamage}.")
                    eHP -= toEAttackDamage
                else:
                    toEAttackDamage = 1
                    print(f"The {Enemy.name}'s Hit Points has been reduced by {toEAttackDamage}.")
                    eHP -= toEAttackDamage
    # Function for player using the Herb
    def herb():
        global pHP
        print(f'{Player.name} used the Herb.')
        pHP += random.randint(23, 30)   
        if pHP > Player.HP:
            pHP = Player.HP 
    # Function for player using the Fairy Flute
    def fairyFlute():
        print(f"{Player.name} blew the Fairie's Flute.")
        if Enemy.name == 'Golem':
            print('Quietly Golem closes his eyes and settles into sleep.')
            Enemy.eSleep = True
        elif Enemy.sleepResist == None:
            Enemy.eSleep = True
            print(f'Thou hast put the {Enemy.name} to sleep.')
        elif random.uniform(0, 1) >= Enemy.sleepResist:
            Enemy.eSleep = True
            print(f'Thou hast put the {Enemy.name} to sleep.')
        else:
            print('But nothing happened.') 
    # Function for player version of HEAL
    def heal():
        global pHP
        global MP
        print(f'{Player.name} chanted the spell of HEAL.')
        MP -= 4
        if MP <= 3:
            print('Thy MP is too low.')
            if MP < 0:
                MP = 0
        elif Player.pStopSpell:
            print(f"{Player.name}'s spell is blocked.")
        else:
            pHP += random.randint(10, 17)
            if pHP > Player.HP:
                pHP = Player.HP
    # Function for player version of HEALMORE
    def healmore():
        global pHP
        global MP
        print(f'{Player.name} chanted the spell of HEALMORE.')
        MP -= 10
        if MP <= 0:
            print('Thy MP is too low.')
            if MP < 0:
                MP = 0
        elif Player.pStopSpell:
            print(f"{Player.name}'s spell is blocked.")
        else:
            pHP += random.randint(85, 100)
            if pHP > Player.HP:
                pHP = Player.HP
    # Function for player version of HURT
    def hurt():
        global eHP
        global MP
        print(f'{Player.name} chanted the spell of HURT.')
        MP -= 2
        if MP <= 1:
            print('Thy MP is too low.')
            if MP < 0:
                MP = 0
        elif Player.pStopSpell:
            print(f"{Player.name}'s spell is blocked.")
        elif random.uniform(0, 1) >= Enemy.hurtResist:
            toEAttackDamage = random.randint(5, 12)
            eHP -= toEAttackDamage
        else:
            print('The spell will not work.')
    # Function for player version of HURTMORE
    def hurtmore():
        global eHP
        global MP
        print(f'{Player.name} chanted the spell of HURTMORE.')
        MP -= 5
        if MP <= 4:
            print('Thy MP is too low.')
            if MP < 0:
                MP = 0
        elif Player.pStopSpell:
            print(f"{Player.name}'s spell is blocked.")
        elif random.uniform(0, 1) >= Enemy.hurtResist:
            toEAttackDamage = random.randint(5, 12)
            eHP -= toEAttackDamage
        else:
            print('The spell will not work.')
    # Function for player version of SLEEP
    def sleep():
        global MP
        print(f'{Player.name} chanted the spell of SLEEP.')
        MP -= 2
        if MP <= 1:
            print('Thy MP is too low.')
            if MP < 0:
                MP = 0
        elif Player.pStopSpell:
            print(f"{Player.name}'s spell is blocked.")
        elif Enemy.eSleep:
            print('The spell will not work.')
        elif Enemy.sleepResist == None:
            Enemy.eSleep = True
            print(f'Thou hast put the {Enemy.name} to sleep.')
        elif random.uniform(0, 1) >= Enemy.sleepResist:
            Enemy.eSleep = True
            print(f'Thou hast put the {Enemy.name} to sleep.')
        else:
            print('The spell will not work.')
    # Function for player version of STOPSPELL
    def stopspell():
        global MP
        print(f'{Player.name} chanted the spell of STOPSPELL.')
        MP -= 2
        if MP <= 1:
            print('Thy MP is too low.')
            if MP < 0:
                MP = 0
        elif Player.pStopSpell:
            print(f"{Player.name}'s spell is blocked.")
        elif Enemy.eStopSpell:
            print('The spell will not work.')
        elif Enemy.stopSpellResist == None:
            Enemy.eStopSpell = True
            print(f"The {Enemy.name}'s spell hath been blocked.")
        elif random.uniform(0, 1) >= Enemy.stopSpellResist:
            Enemy.eStopSpell = True
            print(f"The {Enemy.name}'s spell hath been blocked.")
        else:
            print('The spell will not work.')
    # Function for choosing player actions
    def act():
        while True:
            print('FIGHT SPELL\nRUN   ITEM')
            choice = input().strip().upper()
            if choice == 'FIGHT':
                Player.attack()
                break
            if choice == 'SPELL':
                print('HEAL\nHEALMORE\nHURT\nHURTMORE\nSLEEP\nSTOPSPELL')
                spell = input().strip().upper()
                if spell == 'HEAL':
                    Player.heal()
                    break
                if spell == 'HEALMORE':
                    Player.healmore()
                    break
                if spell == 'HURT':
                    Player.hurt()
                    break
                if spell == 'HURTMORE':
                    Player.hurtmore()
                    break
                if spell == 'SLEEP':
                    Player.sleep()
                    break
                if spell == 'STOPSPELL':
                    Player.stopspell()
                    break
                else:
                    print('Please enter a valid action.')
                    continue 
            if choice == 'RUN':
                Player.flee()
                break
            if choice == 'ITEM':
                print('Herb\nFairy Flute')
                item = input().strip().upper()
                if item == 'HERB':
                    Player.herb()
                if item == 'FAIRY FLUTE':
                    Player.fairyFlute()
                break  
            else:
                print('Please enter a valid action.')
                continue 
    pSleep = False
    pStopSpell = False        
# Get enemy stats
print('Select enemy to fight by id:')
while True:
    try:
        id = input().strip()
        if int(id) > 40 or int(id) < 0:
            print('Please enter a valid id.')
            continue
        break
    except:
        print('Please enter a valid id.')
        continue
with connection:
    cursor = connection.cursor()
    class Enemy:
        id = id
        eStopSpell = False
        cursor.execute('SELECT Name FROM DQ1NFE WHERE Id=?', (id,))
        name = cursor.fetchall()[0][0]
        cursor.execute('SELECT Hp FROM DQ1NFE WHERE Id=?', (id,))
        HPRange = cursor.fetchall()[0][0]
        if HPRange == 130:
            HP = int(HPRange)
        elif len(str(HPRange)) > 1:
            HP = random.randint(int(HPRange.split(' ')[0]), int(HPRange.split(' ')[1]))
        else:
            HP = int(HPRange)
        cursor.execute('SELECT Xp FROM DQ1NFE WHERE Id=?', (id,))
        XP = cursor.fetchall()[0][0]
        cursor.execute('SELECT Locations FROM DQ1NFE WHERE Id=?', (id,))
        locations = cursor.fetchall()[0][0]
        cursor.execute('SELECT Family FROM DQ1NFE WHERE Id=?', (id,))
        family = cursor.fetchall()[0][0]
        cursor.execute('SELECT Strength FROM DQ1NFE WHERE Id=?', (id,))
        strength = cursor.fetchall()[0][0]
        cursor.execute('SELECT Agility FROM DQ1NFE WHERE Id=?', (id,))
        agility = cursor.fetchall()[0][0]
        cursor.execute('SELECT SleepResist FROM DQ1NFE WHERE Id=?', (id,))
        sleepResist = cursor.fetchall()[0][0]
        cursor.execute('SELECT StopSpellResist FROM DQ1NFE WHERE Id=?', (id,))
        stopSpellResist = cursor.fetchall()[0][0]
        cursor.execute('SELECT HurtResist FROM DQ1NFE WHERE Id=?', (id,))
        hurtResist = cursor.fetchall()[0][0]
        cursor.execute('SELECT Dodge FROM DQ1NFE WHERE Id=?', (id,))
        dodge = cursor.fetchall()[0][0]
        if dodge == None:
            dodge = 0
        cursor.execute('SELECT Gold FROM DQ1NFE WHERE Id=?', (id,))
        goldRange = cursor.fetchall()[0][0]
        try:
            if len(str(goldRange)) > 1:
                gold = random.randint(int(goldRange.split(' ')[0]), int(goldRange.split(' ')[1]))
            else:
                gold = int(goldRange)
        except:
            gold = 0
        cursor.execute('SELECT Pattern FROM DQ1NFE WHERE Id=?', (id,))
        pattern = cursor.fetchall()[0][0]
        # Function for enemy fleeing
        def flee():
            if Enemy.eSleep:
                pass
            elif Player.strength > (Enemy.strength * 2):
                if random.randint(0, 3) == 0:
                    print('The', Enemy.name, 'is running away.')
                    Enemy.fleeCheck = True
                    return True
                else:
                    Enemy.fleeCheck = False
                    return False
        # Function for basic attack
        def attack():
            global pHP
            print(f'The {Enemy.name} attacks!')
            if Player.defenese >= Enemy.strength:
                toPAttackDamage = random.randint(0, int((Enemy.strength + 4) // 6))
                pHP -= toPAttackDamage
                print(f'Thy Hits decreased by {toPAttackDamage}.')
            else:
                toPAttackDamage = random.randint(int((Enemy.strength - Player.defenese / 2) / 4 // 1), 
                int((Enemy.strength - Player.defenese / 2) / 2 // 1))
                pHP -= toPAttackDamage
                print(f'Thy Hits decreased by {toPAttackDamage}.')
        # Function for enemy version of HURT
        def hurt():
            global pHP
            print(f'{Enemy.name} chants the spell of HURT.')
            if Enemy.eStopSpell:
                print('But that spell hath been blocked.')     
            elif Player.armorName == "Erdrick's Armor" or Player.armorName == 'Magic Armor':
                toPAttackDamage = random.randint(2, 6)
                pHP -= toPAttackDamage
                print(f'Thy Hits decreased by {toPAttackDamage}.')
            else:   
                toPAttackDamage = random.randint(3, 10)
                pHP -= toPAttackDamage
                print(f'Thy Hits decreased by {toPAttackDamage}.')
        # Function for enemy version of HURTMORE
        def hurtmore():
            global pHP
            print(f'{Enemy.name} chants the spell of HURTMORE.')
            if Enemy.eStopSpell:
                print('But that spell hath been blocked.')
            elif Player.armorName == "Erdrick's Armor" or Player.armorName == 'Magic Armor':
                toPAttackDamage = random.randint(20, 30)
                pHP -= toPAttackDamage
                print(f'Thy Hits have decreased by {toPAttackDamage}.')
            else:   
                toPAttackDamage = random.randint(30, 45)
                pHP -= toPAttackDamage
                print(f'Thy Hits have decreased by {toPAttackDamage}.')
        # Function for enemy version of SLEEP
        def sleep():
            if not Player.pSleep:     
                print(f'{Enemy.name} chants the spell of SLEEP.')
                if Enemy.eStopSpell:
                    print('But that spell hath been blocked.')
                else:
                    Player.pSleep = True
            else:
                Enemy.chooseAttack()      
        # Function for enemy version of STOPSPELL
        def stopspell():
            if not Player.pStopSpell:
                print(f'{Enemy.name} chants the spell of STOPSPELL.')
                if Enemy.eStopSpell:
                    print('But that spell hath been blocked.')
                elif Player.armorName == "Erdrick's Armor":
                    print('But that spell hath been blocked.')
                else:
                    if random.randint(0, 1) == 0:
                        Player.pStopSpell = True
                    else:
                        print('But that spell hath been blocked.')
            else:
                Enemy.chooseAttack()
        # Function for normal fire breath
        def normalFireBreath():
            global pHP
            print(f'The {Enemy.name} is breathing fire.')
            if Player.armorName == "Erdrick's Armor":
                toPAttackDamage = random.randint(10, 14)
                pHP -= toPAttackDamage
                print(f'Thy Hits have decreased by {toPAttackDamage}.')
            else:   
                toPAttackDamage = random.randint(16, 23)
                pHP -= toPAttackDamage
                print(f'Thy Hits have decreased by {toPAttackDamage}.')
        # Function for stronger fire breath
        def dragonlordFireBreath():
            print(f'The {Enemy.name} is breathing fire.')
            global pHP
            if Player.armorName == "Erdrick's Armor":
                toPAttackDamage = random.randint(42, 48)
                pHP -= toPAttackDamage
                print(f'Thy Hits have decreased by {toPAttackDamage}.')
            else:   
                toPAttackDamage = random.randint(65, 72)
                pHP -= toPAttackDamage
                print(f'Thy Hits have decreased by {toPAttackDamage}.')
        # Function for enemy version of HEAL
        def heal():
            global eHP
            print(f'{Enemy.name} chants the spell of HEAL.')
            if Enemy.eStopSpell:
                print('But that spell hath been blocked.')
            else:
                eHP += random.randint(20, 27)
                if eHP > Enemy.HP:
                    eHP = Enemy.HP
        # Function for enemy version of HURTMORE
        def healmore():
            global eHP
            print(f'{Enemy.name} chants the spell of HEALMORE.')
            if Enemy.eStopSpell:
                print('But that spell hath been blocked.')
            else:
                eHP += random.randint(85, 100)
                if eHP > Enemy.HP:
                    eHP = Enemy.HP
        # Function for selecting which attack pattern to follow
        def chooseAttack():
            global eHP
            pattern = {1: 1, 2: 1, 3: 1, 4: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 14: 1, 15: 1, 19: 1, 24: 1, 26: 1, 
            29: 1, 33: 1, 36: 1, 37: 2, 30: 3, 31: 3, 38: 4, 40: 5, 5: 6, 6: 6, 32: 7, 39: 8, 12: 9, 18: 10, 28: 10, 
            21: 11, 13: 12, 20: 13, 17: 14, 22: 14, 25: 14, 23: 15, 34: 16, 16: 17, 35: 18, 27: 19}
            patternType = pattern[int(Enemy.id)]
            # Attack only
            if patternType == 1:
                Enemy.attack()
            # 3/4 cast HealMore if HP less than 1/4 max
            # Else 1/4 cast HurtMore else attack
            if patternType == 2:
                if eHP < Enemy.HP / 4:
                    if random.randint(0, 3) in (0, 1, 2):
                        Enemy.healmore()
                    else:
                        if random.randint(0, 3) == 0:
                            Enemy.hurtmore()
                        else:
                            Enemy.attack()
                else:
                    if random.randint(0, 3) == 0:
                        Enemy.hurtmore()
                    else:
                        Enemy.attack()
            # 3/4 cast HealMore if HP less than 1/4 max
            # Else 1/4 breathe fire else attack
            if patternType == 3:
                if eHP < Enemy.HP / 4:
                    if random.randint(0, 3) in (0, 1, 2):
                        Enemy.healmore()
                    else:
                        if random.randint(0, 3) == 0:
                            Enemy.normalFireBreath()
                        else:
                            Enemy.attack()
                else:
                    if random.randint(0, 3) == 0:
                        Enemy.normalFireBreath()
                    else:
                        Enemy.attack()
            # 1/4 cast Sleep if player not asleep
            # Else 1/4 breathe fire else attack            
            if patternType == 4:
                if not Player.pSleep:
                    if random.randint(0, 3) == 0:
                        Enemy.sleep()
                    else:
                        if random.randint(0, 3) == 0:
                            Enemy.normalFireBreath()
                        else:
                            Enemy.attack()
                else:
                    if random.randint(0, 3) == 0:
                        Enemy.normalFireBreath()
                    else:
                        Enemy.attack()
            # 1/2 breathe strong fire
            # Else attack
            if patternType == 5:
                if random.randint(0, 1) == 0:
                    Enemy.dragonlordFireBreath()
                else:
                    Enemy.attack()
            # 1/2 cast Hurt
            # Else attack
            if patternType == 6:
                if random.randint(0, 1) == 0:
                    Enemy.hurt()
                else:
                    Enemy.attack()
            # 1/2 cast HurtMore
            # Else attack
            if patternType == 7:
                if random.randint(0, 1) == 0:
                    Enemy.hurtmore()
                else:
                    Enemy.attack()
            # 1/4 cast StopSpell if spell is not blocked
            # Else 3/4 cast HurtMore else attack
            if patternType == 8:
                if not Player.pStopSpell:
                    if random.randint(0, 3) == 0:
                        Enemy.stopspell()
                    else:
                        if random.randint(0, 3) in (0, 1, 2):
                            Enemy.hurtmore()
                        else:
                            Enemy.attack()
                else:
                    if random.randint(0, 3) in (0, 1, 2):
                        Enemy.hurtmore()
                    else:
                        Enemy.attack()
            # 1/4 cast Heal if under 1/4 of max HP
            # Else 1/2 cast Hurt else attack
            if patternType == 9:
                if eHP < Enemy.HP / 4:
                    if random.randint(0, 3) == 0:
                        Enemy.heal()
                    else:
                        if random.randint(0, 1) == 0:
                            Enemy.hurt()
                        else:
                            Enemy.attack()
                else:
                    if random.randint(0, 1) == 0:
                        Enemy.hurt()
                    else:
                        Enemy.attack()
            # 3/4 cast Hurt
            # Else attack
            if patternType == 10:
                if random.randint(0, 3) in (0, 1, 2):
                    Enemy.hurt()
                else:
                    Enemy.attack()
            # 3/4 cast Heal if HP less than 1/4 of max
            # Else 1/4 cast Hurt else attack
            if patternType == 11:
                if eHP < Enemy.HP / 4:
                    if random.randint(0, 3) in (0, 1, 2):
                        Enemy.heal()
                    else:
                        if random.randint(0, 3) == 0:
                            Enemy.hurt()
                        else:
                            Enemy.attack()
                else:
                    if random.randint(0, 3) == 0:
                        Enemy.hurt()
                    else:
                        Enemy.attack()
            # 1/4 cast Sleep if player not asleep
            # Else 1/2 cast hurt else attack
            if patternType == 12:
                if not Player.pSleep:
                    if random.randint(0, 3) == 0:
                        Enemy.sleep()
                    else:
                        if random.randint(0, 1) == 0:
                            Enemy.hurt()
                        else:
                            Enemy.attack()
                else:
                    if random.randint(0, 1) == 0:
                        Enemy.hurt()
                    else:
                        Enemy.attack()
            # 1/4 cast Sleep if player not asleep
            # Else 3/4 cast Hurt else attack
            if patternType == 13:
                if not Player.pSleep:
                    if random.randint(0, 3) == 0:
                        Enemy.sleep()
                    else:
                        if random.randint(0, 3) in (0, 1, 2):
                            Enemy.hurt()
                        else:
                            Enemy.attack()
                else:
                    if random.randint(0, 3) in (0, 1, 2):
                        Enemy.hurt()
                    else:
                        Enemy.attack()
            # 1/2 cast StopSpell if spell is not blocked
            # Else attack
            if patternType == 14:
                if not Player.pStopSpell:
                    if random.randint(0, 1) == 0:
                        Enemy.stopspell()
                    else:
                        Enemy.attack()
                else:
                    Enemy.attack()
            # 3/4 cast Heal if HP 1/4 of max
            # Else attack
            if patternType == 15:
                if eHP < Enemy.HP / 4:
                    if random.randint(0, 3) in (0, 1, 2):
                        Enemy.heal()
                    else:
                        Enemy.attack()
                else:
                    Enemy.attack()
            # 1/4 cast Sleep if player not asleep
            # Else attack
            if patternType == 16:
                if not Player.pSleep:
                    if random.randint(0, 3) == 0:
                        Enemy.sleep()
                    else:
                        Enemy.attack()
                else:
                    Enemy.attack()
            # 1/4 cast Heal if HP less than 1/4 of max
            # Else attack
            if patternType == 17:
                if eHP < Enemy.HP / 4:
                    if random.randint(0, 3) == 0:
                        Enemy.heal()
                    else:
                        Enemy.attack()
                else:
                    Enemy.attack()
            # 1/4 breathe fire
            # Else attack
            if patternType == 18:
                if random.randint(0, 3) == 0:
                    Enemy.normalFireBreath()
                else:
                    Enemy.attack()
            # 1/2 cast Sleep if player not asleep
            # Else attack
            if patternType == 19:
                if not Player.pSleep:
                    if random.randint(0, 1) == 0:
                        Enemy.sleep()
                    else:
                        Enemy.attack()
                else:
                    Enemy.attack()
        eSleep = False
# Function for determining initiative
def initiative():
    groupFactor = {1: 0.25, 2: 0.375, 3: 0.5, 4: 1}
    if int(id) <= 20:
        groupFactorValue = groupFactor.get(1)
    elif 21 <= int(id) <= 30:
        groupFactorValue = groupFactor.get(2)
    elif 31 <= int(id) <= 35:
        groupFactorValue = groupFactor.get(3)
    else:
        groupFactorValue = groupFactor.get(4)
    if Player.agility * random.randint(0, 255) > Enemy.agility * random.randint(0, 255) * groupFactorValue:
        return True
    else:
        return False
pHP, eHP, MP, enemySleepTurn, playerSleepTurn, initiativeOccurred = Player.HP, Enemy.HP, Player.MP, 0, 0, False
skipFlee = False
os.system('cls' if os.name=='nt' else 'clear') 
# Battle begins
print('A', Enemy.name, 'draws near!')
if Enemy.flee():
    pass
while True:
    # Checks for initiative
    if not initiative() and initiativeOccurred == False:
        if Enemy.flee():
            break
        print(f'The {Enemy.name} attacked before {Player.name} was ready.')
        Enemy.chooseAttack()
        if pHP <= 0:
            print('Thou art dead.')
            break
        initiativeOccurred = True
    else:
        initiativeOccurred = True
        if Player.pSleep:
            if random.randint(0, 1) == 0 and playerSleepTurn >= 1:
                print(f'{Player.name} awakes.')
                Player.pSleep = False
                playerSleepTurn = 0
            elif playerSleepTurn >= 1:
                print(f'HP: {pHP} MP: {MP}')
                print('Thou art still asleep.')
                playerSleepTurn += 1
            else:
                print(f'HP: {pHP} MP: {MP}')
                print('Thou art asleep.')
                playerSleepTurn += 1
        if not Player.pSleep:
            print(f'HP: {pHP} MP: {MP}')
            print('Command?')
            Player.act()
            if hasattr(Player, 'fleeCheck'):
                if Player.fleeCheck:
                    break
            if eHP <= 0:
                print(f'''Thou hast done well in defeating the {Enemy.name}.\nThy Experience increases by {Enemy.XP}. \
                \nThy GOLD increases by {Enemy.gold}.''')
                break
        if not Enemy.eSleep:
            if Enemy.flee():
                break
            Enemy.chooseAttack()
        else:
            if enemySleepTurn >= 1 and random.randint(0, 2) == 0:
                print(f'The {Enemy.name} hath recovered.')
                enemySleepTurn = 0
                if Enemy.flee():
                    break
                Enemy.chooseAttack()
            else:
                print(f'The {Enemy.name} is asleep.')
                enemySleepTurn += 1
        if pHP <= 0:
            print('Thou art dead.')
            break