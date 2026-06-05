# 03 — MCP：讓 Claude 直接操作你的工具

## 你會學到什麼

把 Claude 接上 Notion 和 Google Calendar，讓它能直接讀取、新增、修改你的內容，不需要複製貼上。

**為什麼這很重要？**
> 沒有 MCP：「Claude，這是我 Notion 的會議記錄，請幫我整理…」（手動複製貼上）
>
> 有了 MCP：「幫我找上週四的會議記錄，整理出待辦事項」——Claude 自己去 Notion 找。

---

## MCP 是什麼？

MCP 全名是 **Model Context Protocol**，聽起來很技術，但概念很簡單：

> **MCP = Claude 伸手拿東西的管道**

平常 Claude 只能看你貼給它的文字。透過 MCP，Claude 可以主動連接其他應用程式，直接存取裡面的資料或執行操作。

```
你說：「幫我整理 Notion 的會議記錄」
         ↓
Claude 透過 MCP 連進 Notion
         ↓
Claude 找到相關頁面，整理後回傳給你
```

---

## 兩種連接方式

### 方式一：Claude.ai 內建整合（比較簡單）

如果你在用 [claude.ai](https://claude.ai) 的網頁版或 Claude Code，可以直接在設定裡連接：

1. 打開 Claude.ai → 點右上角頭像 → **Settings**
2. 點選 **Integrations**（整合）
3. 找到 **Notion** 或 **Google Calendar**，點「Connect」
4. 授權登入即可

連接後，直接在對話框告訴 Claude 你要它做什麼，它就能存取了。

**試試看這些指令：**
```
幫我在 Notion 裡搜尋包含「行銷」關鍵字的頁面
```
```
我的 Google Calendar 今天有哪些行程？
```
```
幫我在 Google Calendar 新增一個明天下午三點、持續一小時的會議，名稱是「週報」
```

---

### 方式二：Claude Code 專案設定（進階）

如果你想在特定專案裡使用 MCP，可以在專案的 `.claude/settings.json` 裡設定。

打開 `examples/mcp-config.json` 看一下範例格式。

> **注意：** 這個方式需要申請 API 金鑰，步驟比較多。建議先用方式一確認概念，之後有需要再研究這個。

---

## 現在可以試什麼？

如果你已經用方式一連上了 Notion 或 Google Calendar，試試這些：

**Notion：**
- `在 Notion 裡找「[你的某個頁面關鍵字]」並幫我摘要重點`
- `幫我在 Notion 新增一個頁面，標題是「2026年下半年目標」，內容先留空`

**Google Calendar：**
- `幫我看看這週有哪些行程`
- `幫我在週五上午十點加一個「覆盤」的提醒，30分鐘`

---

## 常見問題

**Q：MCP 安全嗎？Claude 看得到我所有 Notion 內容嗎？**
你授權哪個工作區，Claude 就只能存取那個範圍。建議用專門的「工作」帳號，不要連個人隱私資料。

**Q：連上後我不想用了怎麼辦？**
到 Claude.ai → Settings → Integrations，點「Disconnect」就斷開了。

**Q：支援哪些工具？**
目前 Claude.ai 內建支援：Notion、Google Drive、Google Calendar。透過第三方 MCP，還可以接 GitHub、Jira、Slack 等。

---

完成了嗎？前往 [04 - Plugin →](../04-plugin/README.md)
