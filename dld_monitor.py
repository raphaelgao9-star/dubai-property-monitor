import requests
import pandas as pd
import json
from datetime import datetime, timedelta

# 1. 配置基础参数
# 实际使用时，请将 URL 替换为 Dubai Pulse (CKAN API) 的真实资源链接
DLD_SALES_API_URL = "https://www.dubaipulse.gov.ae/api/action/datastore_search"
DLD_RENT_API_URL = "https://www.dubaipulse.gov.ae/api/action/datastore_search"

COMMUNITIES = {
    'Arabella': 'Mudon', 
    'Lagoons': 'Damac Lagoons', 
    'AR3': 'Arabian Ranches 3'
}

def fetch_and_clean_data(api_url, property_type="Townhouse", bedrooms=3):
    """
    模拟从 Dubai Pulse 获取数据并进行清洗的函数
    """
    # 实际场景下的请求代码：
    # response = requests.get(api_url, params={"resource_id": "...", "limit": 1000})
    # data = response.json()['result']['records']
    # df = pd.DataFrame(data)
    
    # 这里用结构化的 DataFrame 模拟获取到的近30天原始数据
    mock_raw_data = pd.DataFrame([
        {'area': 'Mudon', 'type': 'Townhouse', 'rooms': 3, 'price': 2850000, 'category': 'Sale'},
        {'area': 'Mudon', 'type': 'Townhouse', 'rooms': 3, 'price': 100, 'category': 'Sale'}, # 异常值：亲友过户
        {'area': 'Mudon', 'type': 'Townhouse', 'rooms': 3, 'price': 165000, 'category': 'Rent'}, # Ejari 租金数据
        {'area': 'Damac Lagoons', 'type': 'Townhouse', 'rooms': 3, 'price': 2600000, 'category': 'Sale'},
        {'area': 'Damac Lagoons', 'type': 'Townhouse', 'rooms': 3, 'price': 145000, 'category': 'Rent'},
        {'area': 'Arabian Ranches 3', 'type': 'Townhouse', 'rooms': 3, 'price': 2800000, 'category': 'Sale'},
        {'area': 'Arabian Ranches 3', 'type': 'Townhouse', 'rooms': 3, 'price': 160000, 'category': 'Rent'},
    ])
    
    return mock_raw_data

def process_market_data():
    df = fetch_and_clean_data("mock_url")
    
    # 2. 过滤异常值 (剔除售价低于 150 万迪拉姆的非正常交易，剔除过低租金)
    df_sales = df[(df['category'] == 'Sale') & (df['price'] > 1500000)]
    df_rents = df[(df['category'] == 'Rent') & (df['price'] > 80000)]
    
    market_data = []
    
    # 3. 计算各社区均价并打包
    for id_key, area_name in COMMUNITIES.items():
        sale_avg = df_sales[df_sales['area'] == area_name]['price'].mean()
        rent_avg = df_rents[df_rents['area'] == area_name]['price'].mean()
        
        market_data.append({
            "id": id_key.lower(),
            "name": area_name,
            "sale": int(sale_avg) if pd.notna(sale_avg) else 0,
            "rent": int(rent_avg) if pd.notna(rent_avg) else 0,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    # 输出 JSON 文件，供前端仪表盘读取
    with open('market_data.json', 'w', encoding='utf-8') as f:
        json.dump(market_data, f, ensure_ascii=False, indent=4)
    print("✅ 市场数据已更新并保存至 market_data.json")

if __name__ == "__main__":
    process_market_data()
