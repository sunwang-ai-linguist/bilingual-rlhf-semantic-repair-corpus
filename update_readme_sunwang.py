import os
from datetime import datetime

# 路徑設定
output_path = "README_sunwang.md"

# 當天日期
today = datetime.now().strftime("%Y-%m-%d")

# 自動更新內容（你可未來替換成自動整理語義資料）
daily_entry = f"""
### 📅 語義貢獻日誌：{today}

- 例行情境：Uber Eats 外送紅燈等待中
- 當日觀察：Bloomberg 語音輸入、Sam Altman 缺席語義推論
- 心得反饋：台灣作為 geopolitics 下的 AI 生態觀察者
"""

# 檢查是否已有舊檔案
if os.path.exists(output_path):
    with open(output_path, "r", encoding="utf-8") as f:
        existing = f.read()
else:
    existing = "# sunwang 的語義貢獻日誌

這是每日自動更新的語義觀察紀錄。
"

# 避免重複寫入同一天
if today not in existing:
    updated = existing + "\n" + daily_entry
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"✅ 已更新 {output_path}，新增日期 {today}")
else:
    print(f"⚠️ 今日 {today} 的紀錄已存在，無需重複寫入。")
