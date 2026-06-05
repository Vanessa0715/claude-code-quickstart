# 02 — Skills：存下你的常用指令

## 你會學到什麼

建立一個「Skill」，以後只要打 `/` 就能一鍵觸發，不用每次重新輸入一長串 prompt。

**為什麼這很重要？**
> 沒有 Skills：每次要請 Claude 整理今日工作清單，都要打一整段說明。
>
> 有了 Skills：輸入 `/daily-summary`，三秒鐘拿到清單。

---

## Skills 是什麼？

Skills 就是**存好的 prompt 快捷鍵**。

- 每個 Skill 是一個 `.md` 檔案，放在 `.claude/commands/` 資料夾裡
- 檔名就是指令名稱（例如檔名 `daily-summary.md` → 指令 `/daily-summary`）
- 在 Claude 對話框輸入 `/` 就可以看到所有可用的 Skills

> **你可能注意到：** Claude.ai 網頁版的設定裡也有「Skills」，和這裡的 `.claude/commands/` 是不同層的東西——執行效果相同，但管理方式、作用範圍、能不能存取本地檔案都不一樣。想弄清楚差在哪裡，打開 [architecture_comparison.html](./architecture_comparison.html)（在瀏覽器開啟）。

### Skills 有兩種層級

| 層級 | 存放位置 | 使用範圍 |
|------|---------|---------|
| 個人全域 | `~/.claude/commands/` | 你所有的專案都能用 |
| 專案專屬 | `你的專案/.claude/commands/` | 只在這個專案裡出現 |

---

## 動手做：執行現有的 Skill

這個資料夾裡已經有一個示範用的 Skill。

### Step 1：看看 Skill 長什麼樣

打開 `.claude/commands/daily-summary.md`，看一下裡面寫了什麼。

（它就是一段中文 prompt，沒有什麼神奇的語法。）

### Step 2：執行它

在 Claude 對話框輸入：

```
/daily-summary
```

按 Enter，看看 Claude 怎麼回應。

### Step 3：試著回答 Claude 的問題

Claude 可能會問你今天有哪些事，照實回答就好。

---

## 動手做：建立你自己的 Skill

### Step 1：想一個你很常用的 prompt

例如：
- 「幫我把這段文字翻譯成正式繁體中文」
- 「幫我寫一封道歉信，語氣要真誠但不要太肉麻」
- 「幫我整理這份會議記錄的重點和待辦事項」

### Step 2：在 `.claude/commands/` 裡建立新檔案

1. 在左側檔案欄，找到 `.claude/commands/` 資料夾

   > **找不到 `.claude` 資料夾？** 它是隱藏資料夾（名稱以 `.` 開頭），VS Code 預設可能不顯示。
   > 解法：在 VS Code 上方搜尋列輸入 `.claude/commands`，就能找到。
   > 或者：打開任何 `.claude/commands/` 裡的現有檔案後，右鍵點它 → 「Reveal in Explorer」也能定位到位置。

2. 右鍵 → 新增檔案
3. 檔名用英文，例如 `translate-formal.md`

### Step 3：把你的 prompt 貼進去

直接把你想要的指令說明寫進去，存檔。

### Step 4：測試

在 Claude 對話框輸入 `/translate-formal`（或你取的名字），確認出現了。

---

## 小提示

Skill 裡面可以用 `$ARGUMENTS` 這個特殊符號，讓你在執行時傳入補充內容。

例如：
```
幫我把以下文字翻譯成正式繁體中文：

$ARGUMENTS
```

執行時輸入：`/translate-formal 你要翻譯的文字`，Claude 就會把你輸入的文字填到 `$ARGUMENTS` 的位置。

---

完成了嗎？前往 [03 - MCP →](../03-mcp/README.md)
