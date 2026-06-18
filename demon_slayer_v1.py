import random

print("🐉 ДОБРО ПОЖАЛОВАТЬ В DEMON SLAYER v3.0!")
print("Ты — воин. Сражайся, качайся, побеждай боссов!")

player = {
    "hp": 100,
    "max_hp": 100,
    "mana": 50,
    "max_mana": 50,
    "attack": 12,
    "defense": 2,
    "gold": 20,
    "potions": 2,
    "kills": 0,
    "lvl": 1,
    "xp": 0,
    "xp_next": 30,
    "weapon": "Меч",
    "weapon_atk": 0,
    "armor": "Кожа",
    "armor_def": 0,
    "skills": {"strength": 1, "agility": 1, "intelligence": 1},
    "skill_points": 0,
    "inventory": []
}

enemies = [
    {"name": "Гоблин", "hp": 25, "attack": 6, "defense": 1, "gold": 10, "xp": 15},
    {"name": "Скелет", "hp": 35, "attack": 9, "defense": 3, "gold": 15, "xp": 20},
    {"name": "Орк", "hp": 50, "attack": 14, "defense": 4, "gold": 25, "xp": 30},
    {"name": "Тролль", "hp": 65, "attack": 12, "defense": 6, "gold": 30, "xp": 40},
    {"name": "Демон", "hp": 80, "attack": 18, "defense": 5, "gold": 50, "xp": 60}
]

bosses = [
    {"name": "🐉 Ледяной Дракон", "hp": 150, "attack": 25, "defense": 8, "gold": 200, "xp": 150},
    {"name": "👹 Князь Тьмы", "hp": 200, "attack": 30, "defense": 10, "gold": 300, "xp": 200}
]

def bar(current, maximum, length=20):
    percent = current / maximum
    filled = int(percent * length)
    return f"[{'█' * filled}{'░' * (length - filled)}] {current}/{maximum}"

def level_up():
    while player["xp"] >= player["xp_next"]:
        player["lvl"] += 1
        player["xp"] -= player["xp_next"]
        player["xp_next"] = int(player["xp_next"] * 1.4) + 10
        player["skill_points"] += 3
        player["max_hp"] += 15
        player["hp"] = player["max_hp"]
        player["max_mana"] += 10
        player["mana"] = player["max_mana"]
        print(f"🎉 УРОВЕНЬ {player['lvl']}! +15 HP, +10 маны, +3 очка навыков!")

def battle(enemy_data):
    global player
    enemy = enemy_data.copy()
    enemy_hp = enemy["hp"]
    enemy_max_hp = enemy["hp"]
    is_boss = "phase" in enemy

    print(f"\n⚔️ Ты встретил {enemy['name']}!")
    if is_boss:
        print("🐉 ВОЗДУХ ДРОЖИТ! ЭТО БОСС!")

    while enemy_hp > 0 and player["hp"] > 0:
        print(f"\n❤️ Ты: {bar(player['hp'], player['max_hp'])}")
        print(f"💢 {enemy['name']}: {bar(enemy_hp, enemy_max_hp)}")
        print(f"💙 Мана: {bar(player['mana'], player['max_mana'])}")
        print("\n1. ⚔️ Атаковать")
        print("2. 🩸 Использовать зелье")
        print("3. 🔥 Огненный шар (мана 20)")
        print("4. 🛡️ Защититься")
        print("5. 🏃 Убежать")

        choice = input("Твой выбор: ")
        def_bonus = 0

        if choice == "1":
            dmg = random.randint(5, player["attack"] + player["weapon_atk"]) + player["skills"]["strength"] * 2
            dmg = max(1, dmg - enemy["defense"])
            enemy_hp -= dmg
            print(f"💥 Ты нанёс {dmg} урона!")

        elif choice == "2":
            if player["potions"] > 0:
                heal = random.randint(20, 40)
                player["hp"] = min(player["hp"] + heal, player["max_hp"])
                player["potions"] -= 1
                print(f"💚 Ты вылечил {heal} HP. Осталось зелий: {player['potions']}")
            else:
                print("❌ Нет зелий!")
                continue

        elif choice == "3":
            if player["mana"] >= 20:
                dmg = random.randint(25, 50) + player["skills"]["intelligence"] * 3
                enemy_hp -= dmg
                player["mana"] -= 20
                print(f"🔥 Огненный шар нанёс {dmg} урона!")
            else:
                print("❌ Недостаточно маны!")
                continue

        elif choice == "4":
            def_bonus = 5
            print("🛡️ Ты защищаешься!")

        elif choice == "5":
            if random.random() < 0.5:
                print("🏃 Ты сбежал!")
                return "fled"
            else:
                print("❌ Побег не удался!")
        else:
            print("⚠️ Неверный выбор.")
            continue

        if enemy_hp > 0:
            total_def = player["defense"] + player["armor_def"] + def_bonus
            enemy_dmg = max(1, random.randint(3, enemy["attack"]) - total_def)
            player["hp"] -= enemy_dmg
            print(f"💢 {enemy['name']} нанёс {enemy_dmg} урона.")

            if player["hp"] <= 0:
                print("💀 Ты погиб.")
                return "lose"

        player["mana"] = min(player["mana"] + 3, player["max_mana"])

    if enemy_hp <= 0:
        gold_reward = random.randint(5, enemy["gold"])
        xp_reward = random.randint(10, enemy["xp"])
        player["gold"] += gold_reward
        player["xp"] += xp_reward
        player["kills"] += 1
        print(f"✅ Ты победил {enemy['name']}!")
        print(f"💰 +{gold_reward} золота, +{xp_reward} опыта.")
        level_up()
        return "win"
    return "lose"

print("🐉 ДОБРО ПОЖАЛОВАТЬ В DEMON SLAYER 3.0!")

while player["hp"] > 0:
    print("\n" + "=" * 50)
    print(f"❤️ HP: {bar(player['hp'], player['max_hp'])}")
    print(f"💙 Мана: {bar(player['mana'], player['max_mana'])}")
    print(f"⚔️ Атака: {player['attack'] + player['weapon_atk']} (оружие: {player['weapon']})")
    print(f"🛡️ Защита: {player['defense'] + player['armor_def']} (броня: {player['armor']})")
    print(f"💰 Золото: {player['gold']} | 🧪 Зелья: {player['potions']} | ☠️ Убито: {player['kills']}")
    print(f"📈 Уровень: {player['lvl']} | Опыт: {player['xp']}/{player['xp_next']}")
    print("=" * 50)
    print("1. 🌲 Искать врага")
    print("2. 🏙️ Город (магазин)")
    print("3. 🏔️ Босс (200 золота)")
    print("4. 🧳 Инвентарь")
    print("5. 📈 Навыки")
    print("6. 💾 Сохранить и выйти")

    choice = input("Твой выбор: ")

    if choice == "1":
        enemy = random.choice(enemies)
        battle(enemy)

    elif choice == "2":
        print("\n🏙️ Ты в городе:")
        print("1. Купить зелье (20 золота)")
        print("2. Улучшить оружие (50 золота, +3 атаки)")
        print("3. Улучшить броню (50 золота, +3 защиты)")
        shop = input("Что делаешь? ")
        if shop == "1" and player["gold"] >= 20:
            player["gold"] -= 20
            player["potions"] += 1
            print("🧪 Ты купил зелье.")
        elif shop == "2" and player["gold"] >= 50:
            player["gold"] -= 50
            player["weapon_atk"] += 3
            player["weapon"] = "Стальной меч" if player["weapon_atk"] >= 6 else "Улучшенный меч"
            print("⚔️ Оружие улучшено!")
        elif shop == "3" and player["gold"] >= 50:
            player["gold"] -= 50
            player["armor_def"] += 3
            player["armor"] = "Кольчуга" if player["armor_def"] >= 6 else "Улучшенная броня"
            print("🛡️ Броня улучшена!")

    elif choice == "3":
        if player["gold"] >= 200:
            player["gold"] -= 200
            boss = random.choice(bosses)
            battle(boss)
        else:
            print("❌ Недостаточно золота!")

    elif choice == "4":
        print(f"🧳 Инвентарь: {', '.join(player['inventory']) if player['inventory'] else 'пусто'}")

    elif choice == "5":
        print(f"📈 Очки навыков: {player['skill_points']}")
        print("1. + Сила (+2 атаки)")
        print("2. + Ловкость (+2 защиты)")
        print("3. + Интеллект (+3 магии)")
        if player["skill_points"] > 0:
            sk = input("Выбери навык: ")
            if sk == "1":
                player["skills"]["strength"] += 1
                player["skill_points"] -= 1
                print("💪 Сила увеличена!")
            elif sk == "2":
                player["skills"]["agility"] += 1
                player["skill_points"] -= 1
                print("🏃 Ловкость увеличена!")
            elif sk == "3":
                player["skills"]["intelligence"] += 1
                player["skill_points"] -= 1
                print("🧠 Интеллект увеличен!")

    elif choice == "6":
        print("💾 Выход...")
        break

print("👋 Спасибо за игру!")
