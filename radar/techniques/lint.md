---
byor:
    "name": "lint"
    "ring": "adopt"
    "quadrant": "techniques"
    "isNew": "FALSE"
    "description": "\
    各種言語や設定等を lint する教え。validate との違いに難儀する点もあるがツールに任せる。\
    <br />see: <a href='https://github.com/officel/byor/blob/main/radar/techniques/lint.md'>note</a>\
    "
---

# lint

- pre-commit 等でコミット前後に対象のファイルやディレクトリ、その成果について lint する

## history

### 2024-04

- yamllint や pymarkdown など、言語毎の linting tool に気を配る
- 同じようなことをするツールが当然複数あるので、精度、性能、人気、使いやすさなどを見て、取捨選択する
- デフォルトの設定にこだわらず、そのチェックの意味、内容を吟味して、現実に即したチェックを行う（yamllintの行の長さなど）
