# 🖥️ My Arch Linux Rice (Wayland Edition)

[![Arch Linux](https://img.shields.io/badge/OS-Arch%20Linux-%231793d1?logo=arch-linux&logoColor=white)](https://archlinux.org)
[![Sway](https://img.shields.io/badge/WM-Sway-%232da44e?logo=sway&logoColor=white)](https://swaywm.org)
[![Gruvbox](https://img.shields.io/badge/Theme-Gruvbox%20Dark-%23b57614)](https://github.com/morhetz/gruvbox)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A clean, minimal, and keyboard-centric desktop setup built on **Sway** (Wayland).  
This configuration focuses on performance, smooth workflows, and a cohesive **Gruvbox Dark** aesthetic.

---

## ✨ Gallery

| Clean Desktop | Application Launcher (Wofi) |
| :---: | :---: |
| ![](Pictures/Screenshots/rice/clean.png) | ![](Pictures/Screenshots/rice/wofi.png) |

| Notifications (Dunst) | Lock Screen |
| :---: | :---: |
| ![](Pictures/Screenshots/rice/dunst.png) | ![](Pictures/Screenshots/rice/lock.png) |

---

## 🔧 The Stack

This setup runs on a pure Wayland environment, utilizing lightweight and modern replacements for the traditional X11 stack.

### ⚙️ Core System
* **OS** → **Arch Linux**
* **Compositor/WM** → **Sway**
* **Display Manager** → **Ly** (TUI-based, extremely fast startup)
* **Shell** → **Nushell**
* **Terminal** → **Alacritty** (Main) + **Kitty** (Secondary)

### 🎨 Theming & UI
* **Color Scheme** → **Gruvbox Dark**
* **Status Bar** → **swaybar** (configured with **i3status-rust**)
* **Launcher** → **Wofi** (with custom power menu script)
* **Notifications** → **Dunst**
* **GTK Theme** → **Gruvbox-Dark-Medium**
* **Icons** → **Tela-circle-dark** (Used specifically for Wofi/Menus)

### 🛠️ Key Utilities
* **Idle Daemon** → **swayidle** (Handles sleep/lock logic safely)
* **Wallpaper** → **swaybg** (Managed by custom `random_wallpaper.sh` script)
* **Screenshots** → **Grim** (capture) + **Slurp** (select) + **Satty** (annotate)
* **Clipboard** → **wl-clipboard**
* **Audio** → **PipeWire**

---

## 📂 Custom Scripts

### `random_wallpaper.sh`
A custom Bash script that manages wallpaper rotation.
- **Logic:** Shuffles images from `/usr/share/backgrounds` and rotates them every 10 minutes.
- **Engine:** Spawns a new `swaybg` process and cleanly kills the old one to ensure seamless transitions without flickering.

### Power Menu
A Wofi-based power menu that safely handles Wayland session locking.
- **Features:** Dynamic icon detection and race-condition-free sleep locking.

---

## 💡 Workflow & Keybinds

- **Super + Enter**: Open Terminal
- **Super + Space**: Open Wofi Launcher
- **Super + X**: Power Menu
- **Shift + Print Screen**: Screenshot (Grim + Slurp → Satty)

---

## 📥 Installation

> ⚠️ **Warning:** This config is for Wayland. Ensure your GPU drivers are configured for Sway.

```bash
git clone https://github.com/penzulo/dotfiles.git ~/.dotfiles
cd ~/.dotfiles

# Required packages (Arch Linux):
# sudo pacman -S sway swaybg swayidle swaylock-effects waybar i3status-rust wofi grim slurp satty ly dunst wl-clipboard
```

## 📝 License
MIT — feel free to reuse or adapt.
