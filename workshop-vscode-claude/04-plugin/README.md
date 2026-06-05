# 04 — 打包你的工具組合

## 你會學到什麼

把自己的 CLAUDE.md、Skills、MCP 設定打包成可以複製、分享給別人的工具組合。

---

## 概念：你的「Claude 工作包」

你已經學了三個東西：
- **CLAUDE.md** — 設定 Claude 的背景知識
- **Skills** — 存下常用指令
- **MCP** — 接上外部工具

這三樣合在一起，就是你的「Claude 工作包」——**一個資料夾，裡面包含你客製化 Claude 所需的所有設定。**

```
my-workspace/
├── CLAUDE.md                    ← 你的設定
└── .claude/
    └── commands/                ← 你的 Skills
        ├── daily-summary.md
        └── translate-formal.md
```

把這個資料夾分享給同事，他們放進自己的專案就能用了。換電腦時也只需要複製這個資料夾，設定立刻恢復。

---

## 為什麼這很有用？

### 對個人來說
你把自己的 CLAUDE.md + Skills 整理好，可以在換電腦、換專案時一鍵恢復你的整套設定。

### 對團隊來說
主管或技術人員做好一個工作包，全團隊複製後大家都有相同的工具和規範，不用每個人自己摸索。

---

## 怎麼取得別人做好的工具包？

### 方法一：從 GitHub 複製

許多開放原始碼的設定包放在 GitHub 上，把整個 `.claude/` 資料夾複製到你的專案裡就能用。

搜尋方向：

| 用途 | 搜尋關鍵字 |
|------|-----------|
| 專案管理 | `claude code mcp jira` / `claude code mcp linear` |
| 筆記整理 | `claude code mcp notion` / `claude code mcp obsidian` |
| 開發輔助 | `claude code mcp github` / `claude code mcp supabase` |
| 通訊整合 | `claude code mcp slack` / `claude code mcp gmail` |

> **提示：** 取得前確認來源可信賴。官方或知名開發者維護的比較安全，MCP 設定會有存取你工具的權限。

### 方法二：安裝 VS Code Extension

VS Code 的擴充功能市集裡有一些工具可以強化 Claude Code 的功能，例如改善介面、增加快捷鍵。

搜尋方式：在 VS Code 按 `Cmd+Shift+X` / `Ctrl+Shift+X` → 搜尋 `claude code`。

> **注意：** VS Code Extension（VS Code 擴充功能）和前面學的 MCP / Skills 是**不同層級**的東西。Extension 是改 VS Code 本身的功能；MCP 和 Skills 是在 Claude Code 裡客製化 Claude 的行為。搜尋時容易混淆，多看一下描述確認你要的是哪種。

---

## 現在可以做的事

花 5 分鐘整理自己的工作包：

1. 確認 CLAUDE.md 裡的內容是最新的
2. 看看這幾天建的 Skills，把用不到的刪掉，常用的保留
3. 把整個 `.claude/` 資料夾存一份備份，換電腦時直接複製過去

---

## 你現在已經知道的事

學到這裡，你已經了解 Claude Code 的四個核心概念：

- ✅ **CLAUDE.md** — Claude 的說明書，讓它了解你
- ✅ **Skills** — 你的個人快捷工具庫
- ✅ **MCP** — 橋接外部工具的管道
- ✅ **工具包** — 把以上三者打包分享的方式

這四個東西組合在一起，就是「客製化 AI 工作流程」的基礎。

---

時間夠的話，試試加碼挑戰 → [05 - Git + Firebase ⚡](../05-bonus-git-firebase/README.md)

時間不夠也沒關係，把這個資料夾帶回家，隨時可以繼續。
