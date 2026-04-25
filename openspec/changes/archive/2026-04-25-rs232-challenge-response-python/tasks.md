## 1. 專案初始化與環境設定

- [ ] 1.1 建立 Python 專案目錄與虛擬環境。
- [ ] 1.2 安裝 `pyserial` 函式庫 (`pip install pyserial`)。
- [ ] 1.3 安裝 `pyinstaller` 函式庫 (`pip install pyinstaller`)。

## 2. RS232 通訊模組開發

- [ ] 2.1 建立 `serial_handler.py` 模組，包含序列埠開啟、關閉功能。
- [ ] 2.2 實作 `send_command(port, data)` 函數，用於傳送 5 bytes 指令。
- [ ] 2.3 實作 `receive_response(port, length)` 函數，用於接收 16 bytes 資料，並處理逾時。
- [ ] 2.4 實作錯誤處理機制，如序列埠無法開啟、讀寫錯誤等。

## 3. 挑戰-響應邏輯實作

- [ ] 3.1 建立 `challenge_response_logic.py` 模組。
- [ ] 3.2 實作 `decode_challenge(response_bytes)` 函數，從 16 bytes 中提取第 5~12 bytes。
- [ ] 3.3 實作 `calculate_answer(challenge_data)` 函數，執行 XOR 與 Offset 運算。
- [ ] 3.4 實作 `assemble_protocol(answer_bytes)` 函數，將答案組合成協議格式。

## 4. 使用者介面 (GUI) 開發

- [ ] 4.1 建立 `main_gui.py` 模組，使用 Tkinter 設計基本介面。
- [ ] 4.2 介面應包含：序列埠選擇、傳輸速率輸入、連線/斷開按鈕、傳送指令按鈕、顯示接收資料區塊、顯示計算結果區塊。
- [ ] 4.3 連結 GUI 元素與後端通訊及邏輯函數。

## 5. 執行檔打包

- [ ] 5.1 撰寫 `build.py` 腳本，使用 `PyInstaller` 指令來打包 `main_gui.py` 或主要執行文件。
- [ ] 5.2 測試生成的 .exe 執行檔是否能正常運作。

## 6. 測試與驗證

- [ ] 6.1 針對 RS232 通訊模組進行單元測試。
- [ ] 6.2 針對挑戰-響應邏輯進行單元測試。
- [ ] 6.3 進行整合測試，驗證整個挑戰-響應流程的正確性。
- [ ] 6.4 進行使用者驗收測試 (UAT)，確認功能符合預期。
