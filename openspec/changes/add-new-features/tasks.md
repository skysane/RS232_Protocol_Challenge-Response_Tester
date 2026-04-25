## 1. GUI 與日誌介面更新

- [x] 1.1 在 `main_gui.py` 新增日誌顯示框 (ScrolledText)
- [x] 1.2 在 UI 加入 CS 選項 Checkbox 與 Timeout 設定輸入框
- [x] 1.3 在 UI 加入驗證資料設定區 (4筆 XOR/Offset 設定) 與 預處理字串輸入框

## 2. 核心邏輯實作

- [x] 2.1 在 `challenge_response_logic.py` 新增 Checksum 計算功能
- [x] 2.2 在 `challenge_response_logic.py` 實作 XOR 與 Offset 的驗證邏輯
- [x] 2.3 修改 `serial_handler.py` 在寫入前執行 `reset_output_buffer()`

## 3. 整合與驗證

- [x] 3.1 整合所有功能至主程式與 GUI 事件綁定
- [x] 3.2 驗證 CS 計算 ASCII 輸出格式正確性
- [x] 3.3 執行測試腳本確認新功能正常運作
