## Why
為了提升 RS232 測試工具的靈活性與專業度，使用者需要更精確的驗證機制（CS 計算）、傳輸控制（TX Buffer 清空、Timeout 設定）以及自定義驗證協議（XOR 計算、Offset 設定）。此外，增加日誌記錄功能有助於調試與分析。

## What Changes
1. **CS 計算選項**: 新增 CS (Checksum) 計算與自動轉 ASCII 傳送功能。
2. **傳輸優化**: 增加傳輸前 TX buffer 清空功能。
3. **Timeout 設定**: 增加接收 Timeout 設定（毫秒）。
4. **自定義預處理字串**: 允許定義傳送驗證資料前的字串。
5. **進階驗證機制**: 支援 4 筆自定義驗證資料，包含 XOR 計算與 Offset 設定。
6. **日誌記錄**: 新增 TX/RX 資料紀錄顯示框。

## Capabilities

### New Capabilities
- `cs-checksum-engine`: 計算指令欄位 SUM 並將結果轉換為 2 位 ASCII (Hex) 格式。
- `tx-buffer-management`: 發送前強制清空串口 TX buffer。
- `adjustable-timeout`: 支援接收端動態設定 Timeout 數值 (ms)。
- `pre-verification-string`: 定義並在驗證傳輸前發送特定字串。
- `xor-validation-logic`: 基於使用者定義的 byte 對與 Offset 進行 XOR 驗證計算。
- `transfer-log-interface`: 即時監控並顯示傳送與接收的完整數據流。

### Modified Capabilities
- `rs232-comm`: 修改傳輸協議層，增加 CS 計算與預處理字串功能。
- `challenge-response-logic`: 擴展原有的驗證邏輯，加入 XOR 與 Offset 參數處理。

## Impact
- `main_gui.py`: 需要調整 UI 介面，增加新設定選項與 log 顯示區。
- `serial_handler.py`: 修改串口寫入邏輯以包含 buffer 清空與預處理字串。
- `challenge_response_logic.py`: 增加 CS 與 XOR 驗證計算邏輯。
