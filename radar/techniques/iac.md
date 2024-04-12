---
byor:
    "name": "Infrastructure as code"
    "ring": "adopt"
    "quadrant": "techniques"
    "isNew": "FALSE"
    "description": "\
    インフラをコード化。ansible や terraform など。\
    <br />see: <a href='https://github.com/officel/byor/blob/main/radar/techniques/iac.md'>note</a>\
    "
---

# Infrastructure as code

- 個人的には terraform と ansible

## history

### 2024-04

- 強い要望があれば別のツールも使うけど、インフラのコード化は宣言型がもっとも適していると信じている
- プログラマブルにしてメンテナンス性を失うのはナンセンス
- 破壊的変更を容易に実現せず、最短で動確が可能である状態こそが望ましいと考える
