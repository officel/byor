---
byor:
    "name": "OIDC for GitHub Actions"
    "ring": "adopt"
    "quadrant": "techniques"
    "isNew": "FALSE"
    "description": "\
    GitHub Actions ではセキュリティ強化のために OIDC を使用しろという教え。まったくそのとおり。\
    <br />see: <a href='https://github.com/officel/byor/blob/main/radar/techniques/oidc4github.md'>note</a>\
    "
---

# OIDC for GitHub Actions

- [アマゾン ウェブ サービスでの OpenID Connect の構成 - GitHub Docs](https://docs.github.com/ja/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)

## history

### 2024-03

- クラウドサービス等への接続など、クレデンシャルが必要なケースで OIDC を使用すると安全
