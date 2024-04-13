---
byor:
    "name": "Git Hook"
    "ring": "adopt"
    "quadrant": "techniques"
    "isNew": "FALSE"
    "description": "\
    git hook で処理を追加。具体的には pre-commit を使って lint, validate, その他チェックを行う。\
    <br />see: <a href='https://github.com/officel/byor/blob/main/radar/techniques/githook.md'>note</a>\
    "
---

# Git Hook

- hook 自体は git の機能
- [pre-commit](https://github.com/officel/byor/blob/main/radar/tools/pre-commit.md) で一元管理

## history

### 2024-04

- pre-commit をインストールしていなければ動かないので、CI でも処理すること
- ローカルでちゃんと実行するようにチームに呼びかける
- 各種 lint 類の設定のネゴもとる
