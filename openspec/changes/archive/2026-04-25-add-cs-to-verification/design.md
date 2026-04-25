## Context
現有的 CS 計算機制主要應用於一般指令。使用者現在要求在傳送「驗證資料」時，同樣需要提供啟用 CS 的選項，以保持通訊協議的一致性。

## Goals / Non-Goals

**Goals:**
- 在驗證資料區塊增加 CS 啟用選項。
- 確保發送驗證資料的流程能正確呼叫已實作的 Checksum 計算邏輯。

**Non-Goals:**
- 不需重新發明 Checksum 計算演算法，沿用現有邏輯。

## Decisions

- **UI 調整**: 在 `main_gui.py` 的驗證資料設定區中，新增一個 `tk.Checkbutton` 用於啟用 CS。
- **邏輯重用**: 修改驗證資料的發送函數，傳入 CS 狀態，並在其發送序列中加入 CS byte 計算與 ASCII 轉換邏輯。

## Risks / Trade-offs

- [Risk] 驗證資料長度可能與一般指令不同 ➔ Mitigation: 確保 `calculate_checksum` 函數能處理通用長度的輸入陣列。
