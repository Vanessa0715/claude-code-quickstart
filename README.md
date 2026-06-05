# Claude Code 教學資源庫

這個資料夾包含兩套教材，可以按順序學，也可以跳到你感興趣的部分。

---

## 教材一：快速入門（給第一次使用的人）

📁 [quickstart/](./quickstart/README.md)

從安裝到第一次讓 Claude 幫你做東西，約 60 分鐘跑完。

---

## 教材二：進階工作坊（了解四大核心工具）

📁 [workshop-vscode-claude/](./workshop-vscode-claude/README.md)

認識 CLAUDE.md、Skills、MCP、Plugin，學會客製化你自己的 Claude 工具包，約 60–70 分鐘。

---

> 不知道從哪開始？從 `quickstart/` 的第一章走一遍，再回來看工作坊。

---

## 專案結構

```
claude-code-quickstart/
│
├── index.html                          # 教材入口頁（在瀏覽器開啟）
│
├── quickstart/                         # 教材一：快速入門
│   ├── 01-install/
│   │   ├── README.md
│   │   └── claude-ai-vs-vscode.html   # 附錄：Claude.ai vs VS Code 整體差異
│   ├── 02-hello-claude/
│   │   ├── README.md
│   │   └── sample.txt                 # 練習用的文字檔
│   ├── 03-fix-my-code/
│   │   ├── README.md
│   │   └── broken.py                  # 練習用的有 bug 的程式
│   ├── 04-build-something/
│   │   ├── README.md
│   │   └── prompt-examples.md         # 可直接使用的任務範本
│   └── 05-tips/
│       └── README.md
│
└── workshop-vscode-claude/             # 教材二：進階工作坊
    ├── 01-claude-md/
    │   ├── README.md
    │   └── my-claude-md/CLAUDE.md     # 學員填寫的 CLAUDE.md 模板
    ├── 02-skills/
    │   ├── README.md
    │   ├── .claude/commands/
    │   │   └── daily-summary.md       # 示範用的 Skill
    │   └── architecture_comparison.html  # 附錄：Skills 架構比較
    ├── 03-mcp/
    │   ├── README.md
    │   └── examples/mcp-config.json   # MCP 設定範例
    ├── 04-plugin/
    │   └── README.md
    └── 05-bonus-git-firebase/
        └── README.md
```
