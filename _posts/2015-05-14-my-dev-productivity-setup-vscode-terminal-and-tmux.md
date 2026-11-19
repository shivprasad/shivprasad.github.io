---
title: "My Dev Productivity Setup: VSCode, Terminal, and tmux"
date: 2015-05-14 03:00:00 -0700
categories:
  - Blog
  - General
tags:
  - developer-tools
  - tmux
  - vscode
authors:
  - shiv
---

This quarter, I revamped my dev setup:
- Switched to [VSCode](https://code.visualstudio.com/)
- Using iTerm2 + zsh + tmux for sessions
- Aliased common git commands and builds

My `.tmux.conf` now includes:

```
set -g mouse on
bind r source-file ~/.tmux.conf \; display "Reloaded!"

```

Productivity is environment + habit. This gave me both.
