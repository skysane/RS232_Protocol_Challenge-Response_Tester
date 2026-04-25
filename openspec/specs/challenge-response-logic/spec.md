# challenge-response-logic Specification

## Purpose
TBD - created by archiving change rs232-challenge-response-python. Update Purpose after archive.
## Requirements
### Requirement: 挑戰-響應運算邏輯
系統 SHALL 針對接收到的 16 bytes 回應資料中的第 5 到第 12 個位元組（索引從 0 開始則為 4~11 或 5~12，此處假設為 user 所指的 5~12 byte）進行 XOR 與 Offset 運算。

#### Scenario: 計算正確答案
- **WHEN** 接收到 16 bytes 資料，提取第 5~12 byte
- **THEN** 系統 MUST 正確執行 XOR 運算與加上 Offset 值，並產生最終答案

### Requirement: 回傳協議組合
系統 SHALL 將計算出的答案依照特定協議格式重新組裝，並傳送回設備端。

#### Scenario: 完成答辯流程
- **WHEN** 答案計算完成
- **THEN** 系統 SHALL 將答案封裝成協議格式並透過序列埠傳送，完成一次完整的挑戰-響應流程

