# 🎮 Super Pac-Man (3D)

![OpenGL](https://img.shields.io/badge/OpenGL-Graphics-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Course](https://img.shields.io/badge/Course-CSE423-orange)
![Project](https://img.shields.io/badge/Project-Academic-success)
![Status](https://img.shields.io/badge/Status-Constructing-orange)

---

## 📌 Course Information
**Course:** CSE423 – Computer Graphics  
**Project Title:** Super Pac-Man  
**Technology:** Python + OpenGL  
**Graphics Mode:** 3D  
**Template Used:** `3D_OpenGL_Intro.py` (Provided by course instructor)

---

## 👥 Team Members
| Name | Student ID |
|------|------------|
| Shah Mohammad Zarif Abrar Ansari | 22201494 |
| Shafin Ahmed | 22201469 |
| Samiya Hossain Shabnam | 22201700 |

---

## 🧠 Project Overview
**Super Pac-Man** is a 3D game inspired by the classic Pac-Man, developed using OpenGL concepts taught in the **CSE423 Computer Graphics** course.  
The game is played on a restricted checker-grid floor where the player collects rewards, avoids enemies, and progresses through increasingly difficult levels.

The project strictly follows the provided OpenGL template and scales up significantly compared to previous assignments.

---

## 🎮 Game Features

### 🟡 Core Gameplay
- Pac-Man moves on a **restricted checker-grid**
- Movement is limited to **specific tiles**
- Player collects **small rewards** placed on the floor

### 👾 Enemy Mechanics
- Enemies continuously **chase Pac-Man**
- Enemies move **directly towards Pac-Man**
- With each level:
  - Enemy **speed increases**
  - Enemy **spawn delay decreases**

### ⭐ Super Mode
- Activated after collecting several rewards
- In Super Mode:
  - Enemies **freeze for 5–10 seconds**
  - Enemies **change color**
  - Pac-Man can **consume enemies**

### 🏆 Level Progression
- After collecting all small rewards:
  - A **big reward** appears
- Collecting the big reward:
  - Advances to the **next level**
  - Increases difficulty and reward value

### ❤️ Lives & Scoring
- Player starts with **10 lives**
- Losing a life occurs on enemy collision (outside Super Mode)
- Score increases with rewards and level progression

---

## 🖥️ HUD Information
The following labels are displayed on screen:
- **Lives**
- **Level**
- **Current Score**
- **Rewards Left**
- **High Score**

---

## 📈 Difficulty Scaling
Each new level introduces:
- Faster enemies
- Higher reward values
- Earlier enemy appearance
- Increased challenge

---

## 🎯 Controls
- **Arrow Keys / WASD** – Move Pac-Man
- Movement restricted to valid floor tiles

---

## ⚙️ Technical Constraints
- Implemented using **only course-taught OpenGL concepts**
- No external game engines used
- Built strictly on the provided 3D OpenGL template

---



## ✅ Conclusion
**Super Pac-Man** demonstrates the effective use of 3D OpenGL concepts including transformations, object movement, collision logic, and real-time interaction, fulfilling all **CSE423 project requirements**.

---

⭐ *Academic project created for learning and demonstration purposes.*
