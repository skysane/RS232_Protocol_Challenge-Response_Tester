## Why
在先前的功能擴充中，我們新增了針對一般指令的 CS (Checksum) 計算與自動轉換 ASCII 傳送功能。然而，對於「驗證資料」的傳送，同樣需要具備 CS 計算選項，以確保驗證過程中的數據完整性與格式一致性，讓使用者能針對不同協議需求靈活調整。

## What Changes
1. **驗證資料 CS 選項**: 在驗證資料發送設定區新增「使用 CS」Checkbox。
2. **邏輯整合**: 將現有的 CS 計算邏輯擴充應用於驗證資料的發送流程。

## Capabilities

### New Capabilities
- `verification-cs-option`: 在驗證資料發送介面中加入 CS 啟用選項，並在發送邏輯中調用 Checksum 計算。

### Modified Capabilities
- `rs232-comm`: 更新發送驗證資料的邏輯，使其在啟用 CS 選項時，能對驗證資料進行與一般指令相同的 Checksum 計算與轉換。

## Impact
- `main_gui.py`: 更新驗證資料設定區的 UI。
- `challenge_response_logic.py`: 確保發送驗證資料的函數可以接受並處理 CS 啟用標誌。
