---
byor:
    "name": "validate"
    "ring": "adopt"
    "quadrant": "techniques"
    "isNew": "FALSE"
    "description": "\
    各種言語や設定等を validate する教え。lint との違いに難儀する点もあるがツールに任せる。\
    <br />see: <a href='https://github.com/officel/byor/blob/main/radar/techniques/validate.md'>note</a>\
    "
---

# validate

- pre-commit 等でコミット前後に対象のファイルについて validate する

## history

### 2024-04

- terraform などは lint サブコマンドはなく validate があるだけ（ TFLint というツールはある）
- 特定の要件に従っているか、などが validate のチェック項目
- pre-commit の conventional-pre-commit などは validate だと思う
