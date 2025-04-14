
# ⚔️ Valhalla Rising – TROOPS OF DOOM

---

## 🧭 Overview | Vue d'ensemble | Visão Geral

This repository defines the code, behavior and classification of all **standard, support and superminion troops** in *Valhalla Rising – The Parchment*. Each troop type plays a unique role in the lane and jungle progression system.

Ce dépôt contient les fichiers liés aux troupes standards, de support et super-minions.

---

## 🛡️ Standard Troops (Path Clearers)

### 👻 Ghost_S_4 – Viking Ghosts
- Type: Mid-range
- Quantity: 4 per wave
- Damage: Magical
- Traits: Pass through obstacles, fast, ethereal

### 💀 Squeleton_S_4 – Warrior Skeletons
- Type: Melee
- Quantity: 4 per wave
- Damage: Physical (raw)
- Traits: Brutal melee attackers

---

## 🌀 Support & Defense Troops

### 🦀 Crab_S_2 – Rune Crabs
- Type: Tank
- Quantity: 2 per wave
- Role: Absorb damage slowly
- Traits: High HP, slow advance

### 🐌 Snail_S_2 – Mystic Snails
- Type: Support
- Quantity: 2 per wave
- Role: Heals nearby allied troops
- Traits: Linger behind, magical healing aura

---

## 🔥 Superminions (Endgame Spawn – After Last Obelisk Destroyed)

### 🕷️ Aracno_SS – Elite Aracnoid
- Type: Superminion
- Quantity: 1 per wave
- Damage: Piercing
- Traits: Agile, fast, technological appearance

### 🧟 Zoombie_SS – Armored Viking Zombie
- Type: Superminion
- Quantity: 1 per wave
- Damage: Area
- Traits: Very high resistance, brutal, siege specialist

---

## 🧩 Code Structure (Suggested)

```
/standard
  - ghost_s_4.py / .java
  - squeleton_s_4.py / .java
/support
  - crab_s_2.py / .java
  - snail_s_2.py / .java
/superminions
  - aracno_ss.py / .java
  - zoombie_ss.py / .java
```

---

## 🧾 Status

✅ Lore and mechanics defined  
🔜 Code logic in progress (Python and Java)  
🌐 Future: Integrated behavior in match simulation

---

© 2025. All rights reserved to Marcelo dos Santos Prado.
