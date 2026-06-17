import random

print("🐉 ДОБРО ПОЖАЛОВАТЬ В DEMON SLAYER v1.0!")
print("Ты — воин. Твоя цель — побеждать демонов.")

player_hp = 100
gold = 0
kills = 0

while player_hp > 0:
    enemy_hp = random.randint(20, 50)
    enemy_name = random.choice(["Гоблин", "Скелет", "Орк", "Тролль", "Демон"])

    print(f"\n⚔️ Ты встретил {enemy_name} (HP: {enemy_hp})")
    print(f"❤️ Твоё здоровье: {player_hp}")
    print("1. Атаковать")
    print("2. Убежать")

    choice = input("Твой выбор: ")

    if choice == "1":
        dmg = random.randint(10, 25)
        enemy_hp -= dmg
        print(f"💥 Ты нанёс {dmg} урона!")

        if enemy_hp <= 0:
            print(f"✅ Ты победил {enemy_name}!")
            gold += random.randint(10, 30)
            kills += 1
            print(f"💰 +{gold} золота, убито: {kills}")
        else:
            enemy_dmg = random.randint(5, 15)
            player_hp -= enemy_dmg
            print(f"💢 {enemy_name} нанёс {enemy_dmg} урона. У тебя осталось {player_hp} HP")

    elif choice == "2":
        if random.random() < 0.5:
            print("🏃 Ты сбежал!")
        else:
            print("❌ Побег не удался!")
            enemy_dmg = random.randint(5, 15)
            player_hp -= enemy_dmg
            print(f"💢 {enemy_name} нанёс {enemy_dmg} урона.")

    if player_hp <= 0:
        print("💀 Ты погиб. Игра окончена.")

print(f"📊 Статистика: убито: {kills}, собрано золота: {gold}")

