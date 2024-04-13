---
byor:
    "name": "pre-commit"
    "ring": "adopt"
    "quadrant": "tools"
    "isNew": "FALSE"
    "description": "\
    git hook を一元管理するツールの１つ。\
    <br />see: <a href='https://github.com/officel/byor/blob/main/radar/tools/pre-commit.md'>note</a>\
    "
---

# pre-commit

- [pre-commit](https://pre-commit.com/)

## history

### 2024-04

- git hook の１つ pre commit hook と紛らわしいが pre-commit というツール
- 実行環境をマネジメントのCIサーバに移行するように呼びかけられているがそのまま使える
- 言語毎の lint や validate を行う
- ステージ（hookのエントリー）別に分けられるので必要なところにいれる
- .pre-commit.yaml を参照
