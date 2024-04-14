---
byor:
    "name": "Provision monitors and alerts by IaC"
    "ring": "trial"
    "quadrant": "techniques"
    "isNew": "FALSE"
    "description": "\
    監視も IaC で定義しておけという教え。terraform で実現可能な部分は多いが、実際にはドリフトについて要検討。 \
    <br />see: <a href='https://github.com/officel/byor/blob/main/radar/techniques/monitoring.md'>note</a>\
    "
---

# Provision monitors and alerts by IaC

- 要はシステムを IaC する際に一緒にモニタリングを準備しておくところから始まって、同期をとっておけということ

## history

### 2024-04

- 本家の枠内から持ってきた
- DataDog や PagerDuty の IaC を推進することに等しいけど、当然時間経過で進化して変化するので、簡単ではない
- 手作業によるドリフトや IaC 未対応部分への対処など課題も多い
- 管理するべきところとそうでないところを見極める目が必要
