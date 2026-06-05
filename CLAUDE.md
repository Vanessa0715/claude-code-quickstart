# 專案說明

這是一份 Claude Code 教學資源庫，設計給完全沒有程式背景的朋友，帶他們從零開始學會在 VS Code 裡使用 Claude Code。

## 目標受眾

非技術背景的人（行銷、設計、業務等），第一次接觸 Claude Code，可能已經用過 claude.ai 網頁版但不了解 VS Code Extension 的差異。

## 教材結構

兩套教材，建議順序學習：

**教材一：quickstart/**（約 60 分鐘）
1. `01-install` — 安裝 VS Code、帳號、Extension；費用說明
2. `02-hello-claude` — 第一次對話、@ 引用檔案
3. `03-fix-my-code` — 找 bug、代理模式（Claude 直接改檔案）
4. `04-build-something` — 從零建一個小工具、迭代溝通
5. `05-tips` — 好問法、注意事項

**教材二：workshop-vscode-claude/**（約 60–70 分鐘）
1. `01-claude-md` — 寫 CLAUDE.md 設定檔
2. `02-skills` — 建立 .claude/commands/ 快捷指令
3. `03-mcp` — 接上 Notion、Google Calendar
4. `04-plugin` — 打包工具組合（可分享的 .claude/ 資料夾）
5. `05-bonus-git-firebase` — Firebase + GitHub Pages（加碼自習）

## 視覺化參考頁（HTML）

| 檔案 | 用途 | 適合放在 |
|------|------|---------|
| `index.html` | 整份教材的入口頁與課程地圖 | 根目錄 |
| `quickstart/01-install/claude-ai-vs-vscode.html` | Claude.ai vs VS Code 整體差異比較 | 教材一第一章 |
| `workshop-vscode-claude/02-skills/architecture_comparison.html` | Claude.ai Skills vs Claude Code Commands 架構比較 | 教材二第二章 |

## 修改這份教材時要注意

- 語氣設定為**非技術友善**，避免技術術語；有必要時加白話說明
- 每個 README 都以動手練習為主，說明文字保持精簡
- 付費說明放在 `01-install` 和 `index.html`，其他章節不重複
- `workshop-vscode-claude` 的 Skills 功能，學員必須「只開 workshop-vscode-claude/ 這個資料夾」才能正確觸發 /指令，每次提到這件事都要強調
- HTML 視覺頁的設計風格：暖米色系（`#f5f0eb` 背景），Georgia 字型，與 architecture_comparison.html 同一套設計語言
- 「Plugin」這個詞在官方文件裡不存在，改用「工具組合」或「工作包」描述打包 CLAUDE.md + Skills 的概念
