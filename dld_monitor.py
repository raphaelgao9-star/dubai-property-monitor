import requests
import pandas as pd
import json
from datetime import datetime

def fetch_dubai_data():
    """抓取迪拜 DLD 数据 (Mudon, Damac Lagoons, AR3)"""
    # 实际场景：调用 Dubai Pulse API
    # 模拟数据处理逻辑：
    return [
        {"id": "arabella", "name": "Mudon Arabella", "sale": 2850000, "rent": 165000},
        {"id": "lagoons", "name": "Damac Lagoons", "sale": 2600000, "rent": 145000},
        {"id": "ar3", "name": "Arabian Ranches 3", "sale": 2800000, "rent": 160000}
    ]

def fetch_abudhabi_data():
    """抓取阿布扎比 DARI / DMT 数据 (Saadiyat Island)"""
    # 实际场景：调用 DARI.ae 开放接口或抓取 Property Finder 挂牌中位数
    # 模拟数据处理逻辑：
    return [
        {"id": "nouran", "name": "Nouran Living", "sale": 1950000, "rent": 115000},
        {"id": "soho", "name": "Soho Square", "sale": 1450000, "rent": 85000},
        {"id": "parkview", "name": "Park View", "sale": 1550000, "rent": 90000},
        {"id": "louvre", "name": "Louvre Residences", "sale": 3200000, "rent": 170000}
    ]

def run_pipeline():
    print("🔄 开始抓取迪拜 DLD 房产数据...")
    dubai_list = fetch_dubai_data()
    
    print("🔄 开始抓取阿布扎比 DMT/DARI 房产数据...")
    abudhabi_list = fetch_abudhabi_data()
    
    # 整合为统一输出格式
    combined_payload = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dubai": dubai_list,
        "abudhabi": abudhabi_list
    }
    
    # 保存为唯一的 JSON 文件
    with open('market_data.json', 'w', encoding='utf-8') as f:
        json.dump(combined_payload, f, ensure_ascii=False, indent=4)
        
    print("✅ 迪拜 & 阿布扎比双城数据已更新并写入 market_data.json")

if __name__ == "__main__":
    run_pipeline()
