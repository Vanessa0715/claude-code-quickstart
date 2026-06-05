# 01 — 安裝設定

在開始之前，你需要準備三樣東西：VS Code、Claude 帳號、Claude Code extension。

> **已經用過 claude.ai 網頁版？** 想知道 VS Code 的 Claude Code 和網頁版差在哪裡，先看這份比較圖再回來：[Claude.ai vs VS Code Claude Code](./claude-ai-vs-vscode.html)（在瀏覽器開啟）

---

## Step 1：安裝 VS Code

VS Code 是一個免費的程式編輯器，也是我們要用 Claude 的地方。

1. 前往 [code.visualstudio.com](https://code.visualstudio.com)
2. 點「Download」，選你的作業系統（Mac / Windows）
3. 安裝完成後打開 VS Code

---

## Step 2：切換成中文介面（選做，但推薦）

VS Code 預設是英文，如果你比較習慣中文，可以安裝語言包。

1. 在 VS Code 裡，點左側欄的「擴充功能」圖示，或按 `Cmd+Shift+X`（Mac）/ `Ctrl+Shift+X`（Windows）
2. 搜尋 `Chinese Traditional`
3. 找到「Chinese (Traditional) Language Pack for Visual Studio Code」，點「Install」
4. 安裝完成後，右下角會跳出提示，點「Change Language and Restart」
5. VS Code 重新啟動後，介面就會變成繁體中文

> 已經習慣英文介面？跳過這步也完全沒問題。

---

## Step 3：準備 Claude 帳號

1. 前往 [claude.ai](https://claude.ai)
2. 點右上角「Sign up」，用 Google 帳號或 email 註冊

> **關於費用：Claude Code 需要付費方案才能使用。**
>
> 有兩種選擇：
> - **Claude Pro**（推薦）：每月約 $20 美元（約 NT$650），訂閱後直接用帳號登入，最省事。
> - **API Key**：Anthropic 另外申請，按用量計費，適合開發者或用量大的人。
>
> 免費帳號無法使用 Claude Code Extension，裝好後登入會看到升級提示。

---

## Step 4：安裝 Claude Code extension

1. 打開 VS Code
2. 點左側欄的「擴充功能」圖示（四個方塊的樣子），或按 `Cmd+Shift+X`（Mac）/ `Ctrl+Shift+X`（Windows）
3. 搜尋 `Claude Code`
4. 找到 Anthropic 出品的那個，點「安裝」
5. 安裝完成後，左側欄會出現 Claude 的圖示

---

## Step 5：登入

1. 點左側欄的 Claude 圖示
2. 它會要求你登入，點「Sign in with claude.ai」
3. 瀏覽器會開啟，允許授權即可
4. 回到 VS Code，看到對話框出現就代表成功了

---

## 確認完成

你應該可以看到：
- VS Code 左側有 Claude 的圖示
- 點開後有一個可以輸入文字的對話框

完成了嗎？前往 [下一章 →](../02-hello-claude/README.md)
