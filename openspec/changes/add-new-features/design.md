## Context
目前 RS232 測試工具具備基礎串口通訊與挑戰-響應功能。本次變更旨在增強通訊彈性、增加驗證邏輯複雜度（Checksum/XOR/Offset）以及提升除錯能力（日誌功能）。

## Goals / Non-Goals

**Goals:**
- 提供完整的 CS 計算與傳輸機制。
- 增加串口操作的精細控制（清空 Buffer, 可調 Timeout）。
- 導入自定義驗證協議擴充功能。
- 實作資料傳輸日誌。

**Non-Goals:**
- 不涉及硬體端的通訊協定重新定義，僅針對測試軟體端。

## Decisions

- **CS/Checksum 處理**: 在 `challenge_response_logic.py` 中新增 `calculate_checksum` 函式，並在發送邏輯前呼叫。
- **串口清理**: 使用 `pyserial` 的 `reset_output_buffer()` 方法在傳輸前確保 TX 狀態乾淨。
- **Timeout 設定**: 在 `main_gui.py` 的串口開啟設定中加入 `timeout` 參數輸入框。
- **自定義驗證**: 在 `challenge_response_logic.py` 引入參數對映表，儲存 XOR 規則與 Offset。
- **日誌記錄**: 使用 Python `logging` 或簡單的文字框 UI 更新，將 TX/RX 數據同步輸出至 `main_gui.py` 新增的 `ScrolledText` 控件。

## Risks / Trade-offs

- [Risk] 新增功能可能導致舊設定檔不相容 ➔ Mitigation: 實作預設值填充邏輯。
- [Risk] 即時日誌紀錄可能造成 UI 負擔 ➔ Mitigation: 使用執行緒或適當的刷新頻率控制。
