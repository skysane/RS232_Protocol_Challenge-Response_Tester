## Why

目前缺乏一個自動化的 RS232 挑戰-響應（Challenge-Response）測試工具，用於驗證設備的協議一致性。手動執行此類測試既耗時又容易出錯，因此需要一個專用的 Python 應用程式來自動化此流程並提供可執行檔供使用者直接使用。

## What Changes

- 開發一個 Python 腳本來處理 RS232 通訊。
- 實作特定的挑戰-響應流程（5 bytes 指令 -> 16 bytes 回應 -> XOR/Offset 運算 -> 回傳答案）。
- 整合 PyInstaller 或類似工具以產生 Windows 執行檔 (.exe)。
- 提供簡單的使用者介面或命令列介面供操作。

## Capabilities

### New Capabilities
- `rs232-comm`: 系統 MUST 處理基礎的 RS232 序列埠開啟、關閉及資料收發。
- `challenge-response-logic`: 系統 MUST 實作特定的挑戰-響應演算法（XOR 與 offset 運算）。
- `distributable-package`: 系統 SHALL 提供將 Python 程式封裝為獨立執行檔的功能。

### Modified Capabilities
<!-- 無 -->

## Impact

- 影響：建立新的程式碼庫，無需修改現有系統。
- 依賴：需要 `pyserial` 進行通訊，`pyinstaller` 進行打包。
