---
byor:
    "name": "test first"
    "ring": "trial"
    "quadrant": "techniques"
    "isNew": "FALSE"
    "description": "\
    先にテストを書いて後からコードを書く教え。バックエンドの頃はそうしていたけどインフラではちょっと難しい。\
    <br />see: <a href='https://github.com/officel/byor/blob/main/radar/techniques/test1st.md'>note</a>\
    "
---

# test first

- 作るものに対してテストを先に書いて、パスするようにコードを書く
- インフラだとリソース別にテスト方法が異なる
- 最終的にリクエストに対するレスポンス（要は synthetics ）で積み上げる

## history

### 2024-04

- JS だと [Jasmine](https://jasmine.github.io/)
- php だと [PHPUnit](https://phpunit.de/index.html) か [Selenium](https://www.selenium.dev/) で外から
- インフラでは [Serverspec](https://serverspec.org/) や [goss](https://github.com/goss-org/goss)
