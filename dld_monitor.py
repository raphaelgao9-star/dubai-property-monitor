import json
from datetime import datetime

# --- 静态配置：社区总套数估算 (Total Units) ---
# 实际运营中，这些是固定的物理常数
COMMUNITY_TOTAL_UNITS = {
    "arabella": 1500,  # Mudon Arabella 
    "lagoons": 8000,   # Damac Lagoons (体量巨大)
    "ar3": 4000        # Arabian Ranches 3
}

def fetch_dubai_data():
    """抓取迪拜 DLD 数据及房产平台挂牌量"""
    
    # 模拟从 Property Finder/Bayut 抓取的当前【在租房源数】
    # 实际场景：调用 API 获取 Active Listings for Rent
    active_listings = {
        "arabella": 52,    # 成熟社区，挂牌少
        "lagoons": 1000,   # 集中交房期，挂牌天量
        "ar3": 320         # 持续交付中
    }
    
    # 基础行情数据 (已锚定 Arabella 17万租金)
    market_data = [
        {"id": "arabella", "name": "Mudon Arabella", "sale": 2850000, "rent": 170000},
        {"id": "lagoons", "name": "Damac Lagoons", "sale": 2600000, "rent": 145000},
        {"id": "ar3", "name": "Arabian Ranches 3", "sale": 2800000, "rent": 160000}
    ]
    
    # 动态计算空置率并合并到数据字典中
    for item in market_data:
        cid = item["id"]
        # 空置率 = 在租房源数 / 社区总套数
        vacancy = active_listings[cid] / COMMUNITY_TOTAL_UNITS[cid]
        item["vacancy"] = round(vacancy, 3) # 保留三位小数，如 0.035
        
    return market_data

def fetch_abudhabi_data():
    """抓取阿布扎比 DARI / DMT 数据 (Saadiyat Island)"""
    return [
        {"id": "nouran", "name": "Nouran Living", "sale": 1950000, "rent": 115000},
        {"id": "soho", "name": "Soho Square", "sale": 1450000, "rent": 85000},
        {"id": "parkview", "name": "Park View", "sale": 1550000, "rent": 90000},
        {"id": "louvre", "name": "Louvre Residences", "sale": 3200000, "rent": 170000}
    ]

def run_pipeline():
    print("🔄 开始抓取迪拜 DLD 房产数据及市场挂牌量...")
    dubai_list = fetch_dubai_data()
    
    print("🔄 开始抓取阿布扎比 DMT/DARI 房产数据...")
    abudhabi_list = fetch_abudhabi_data()
    
    combined_payload = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dubai": dubai_list,
        "abudhabi": abudhabi_list
    }
    
    with open('market_data.json', 'w', encoding='utf-8') as f:
        json.dump(combined_payload, f, ensure_ascii=False, indent=4)
        
    print("✅ 双城数据 (含动态空置率) 已更新并写入 market_data.json")

if __name__ == "__main__":
    run_pipeline()
