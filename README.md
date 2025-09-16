# 🖥️ My Arch Linux Rice

[![Arch Linux](https://img.shields.io/badge/OS-Arch%20Linux-%231793d1?logo=arch-linux&logoColor=white)](https://archlinux.org)
[![Qtile](https://img.shields.io/badge/WM-Qtile-%234477AA?logo=qtile&logoColor=white)](https://qtile.org)
[![Gruvbox](https://img.shields.io/badge/Theme-Gruvbox%20Dark-%23b57614)](https://github.com/morhetz/gruvbox)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


A clean, minimal and cohesive desktop setup built on **Qtile** with a **Gruvbox Dark** color scheme.  
This configuration is tuned for a smooth workflow, minimal distractions, and consistent aesthetics.

---

## ⚙️ System Overview

| Component            | Details                          |
|-----------------------|--------------------------------|
| **OS**               | Arch Linux                       |
| **Display Server**   | X11                              |
| **Window Manager**   | Qtile (powerline bar, gaps, rounded corners) |
| **Compositor**       | Picom (blur, transparency, rounded corners) |
| **Display Manager**  | LightDM (Slick-greeter)           |
| **Lockscreen**        | Betterlockscreen (Gruvbox wallpapers) |
| **Shell**             | Nushell (primary) + Bash         |
| **Prompt**             | Starship                         |

---

## 🎨 Theming

| Type           | Choice                     |
|----------------|------------------------------|
| **Color Scheme** | Gruvbox Dark                |
| **Font**           | JetBrainsMono Nerd Font       |
| **GTK Theme**      | Orchis-Dark-Compact            |
| **Icon Theme**     | Tela Circle Dark               |
| **Terminal**       | Alacritty                      |
| **Application Launcher** | Rofi (apps, file search, power menu, pass) |
| **Notifications**  | Dunst (Gruvbox styled, transparent) |

---

## 🛠 Core Tools

| Category            | Tool                        |
|----------------------|----------------------------|
| **Audio**            | PipeWire + `wpctl`          |
| **Network**           | iwgtk                       |
| **Screenshots**       | Flameshot                   |
| **File Managers**      | Yazi (CLI) + Thunar (GUI)     |
| **Password Management** | pass (with Rofi integration) |
| **Email** | neomutt |
| **Package Management** | pacman + yay + flatpak |

---

## 📸 Screenshots

| Desktop | Rofi | Dunst | Yazi |
|---------|------|-------|------|
| ![](Pictures/Screenshots/desktop.png) | ![](Pictures/Screenshots/rofi.png) | ![](Pictures/Screenshots/dunst.png) | ![](Pictures/Screenshots/yazi.png) |

---

## 💡 Notes

- Configs are modular and easy to extend.
- Gruvbox Dark is applied universally for consistency.
- Power menu, scratchpads, and more are integrated via Rofi and Qtile.
- All fonts and icons are patched and themed for Nerd Font compatibility.

---

## 📥 Installation (Optional)

> ⚠️ Not automated yet — configs are meant to be referenced manually.

```bash
git clone https://github.com/<your-username>/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
# Copy configs manually or with a script
```

## 📝 License
MIT — feel free to reuse or adapt.
