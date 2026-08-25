# research-scope

**研究テーマを練り切るまでの工程**を Claude Code のプラグインにしたもの。

外部の Deep Research を入力に使い、独立した 2 経路の調査を突き合わせ、
**空白を壊しにいって、残ったものだけを主張にする。**

---

## なぜこの形なのか

設計は好みではなく、実証研究と実運用の実測に基づく。詳細は
[`reference/evidence.md`](reference/evidence.md)。要点だけ:

- **凝ったハーネスを作らない。** 分散のうち足場の寄与は **1.5%**、ベースモデルが 41.4%
  （arXiv:2604.18805、8 分野 25,000 超の実行）。複雑さは**機械的照合**に集中させる
- **LLM に品質を判定させない。** 実験ゼロの捏造論文が LLM レビューで採択率 52〜82%（ACL 2026）
- **新規性を聞かない。** 自動新規性判定は 12 案すべてを誤判定した実例がある。
  文献発見率は最高性能モデルでも 9.39%
- **「面白い」は逆指標。** 着想時の excitement は実行後評価と**負の相関**（r=−0.321）
- **空白は壊れてよい。** 壊れるたびに根拠が自分の判断から他人の引用に移る

## 使い方

```
/research-scope:init <研究テーマの説明>
   → projects/YYYY-MM-DD-{slug}/ と context.md を作る

/research-scope:dr-prompt
   → deep-research-prompt.md を生成
   ✋ 外部 Deep Research に貼る → Markdown でダウンロード
   → deep-research-output.md に無編集で保存

/research-scope:sweep          （DR の完了を待たずに並行して開始できる）
   → cc-research/  こちら側の独立調査

/research-scope:synthesize
   → synthesis.md  現在地の表 + 被覆行列

/research-scope:verify
   → verify/  空白を壊しにいく
   ✋ 人間が判断する
```

技術的な争点が出たら、いつでも:

```
/research-scope:spike <決着させたい争点>
```

### 段階を分けている理由

Claude Code の dynamic workflow は**実行中のユーザー入力を受け付けない**。
公式ドキュメントいわく「段階間で承認を挟むなら、各段階を個別に実行すること」。
好みではなく制約。

## インストール

### 試す

```
claude --plugin-dir /path/to/research-scope
```

### 常用する

```
claude plugin marketplace add <your-org>/<your-marketplace-repo>
```

または `~/.claude/skills/` 配下に置くと自動で読まれる（`claude plugin init` が作る形）。

変更を反映するには `/reload-plugins`。

## 中身

```
research-scope/
├── .claude-plugin/plugin.json
├── skills/
│   ├── init/          プロジェクト作成
│   ├── dr-prompt/     Stage 0: 外部 DR 用プロンプト生成
│   ├── sweep/         Stage 2: こちら側の独立調査
│   ├── synthesize/    Stage 3: 突き合わせ
│   ├── verify/        Stage 4: 空白を壊す
│   └── spike/         実行で決着させる
├── reference/
│   ├── principles.md  ★ 全 skill が従う 11 条
│   └── evidence.md      各条の根拠（出典と実測）
└── templates/
    ├── context.md
    └── synthesis.md
```

**中心は [`reference/principles.md`](reference/principles.md) の 11 条。**
skill は薄い。原則が本体。

## 原則（要約）

1. **新規性をモデルに聞かない** — 「最も近い既存研究は何で、どこがどう違うか」を出させる
2. **空白は必ず探索範囲とセット** — クエリ実文字列 / DB / 日付 / 最も近かったもの
3. **抄録から構造的な主張を組み立てない** — 最も高くつく誤り
4. **LLM に品質を判定させない** — 照合可能なものだけ
5. **検証手段を生成側の外に置く**
6. **2 経路を独立に走らせ、片方の結論を確定として扱わない**
7. **語彙より経路を変える**
8. **数値は必ず「素性」とセット** — 合成か実データか
9. **excitement を選定基準にしない** — `cost-to-test` を使う
10. **歩留まりは 1 割前後を前提に数を決める**
11. **空白が壊れるのは成功**

## 適用実績

1 回目: 「2D 機械図面と 3D CAD の密な対応付け」（2026-08）。
エージェント 14 体 + spike 4 版、成果物 9,623 行。

- 空白の主張が **3 回書き換わり**、最終的に**最も近い先行研究の著者自身の引用**で裏づいた
- spike が**自分の誤りを 5 件**炙り出した（議論では 1 件も出なかった）
- 独立 2 経路の重なりは**論文 1 本だけ**。単独では大半を取り逃していた
- **自分の誤りを 10 件記録**。うち 2 件は原則 3 の違反（抄録から構造を作った）

## ライセンス

MIT
