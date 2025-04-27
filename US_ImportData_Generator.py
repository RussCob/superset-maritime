import pandas as pd
import random
import os
from faker import Faker
from datetime import datetime, timedelta
from tqdm import tqdm

fake = Faker()

# Real VOCCs and SCAC codes
vocc_data = [
    {"CarrierName": "MSC", "CarrierCode": "MEDU"},
    {"CarrierName": "CMA CGM", "CarrierCode": "CMDU"},
    {"CarrierName": "COSCO", "CarrierCode": "COSU"},
    {"CarrierName": "MAERSK", "CarrierCode": "MAEU"},
    {"CarrierName": "EVERGREEN", "CarrierCode": "EGLV"},
    {"CarrierName": "HAPAG-LLOYD", "CarrierCode": "HLCU"},
    {"CarrierName": "ZIM", "CarrierCode": "ZIMU"},
    {"CarrierName": "ONE", "CarrierCode": "ONEY"},
    {"CarrierName": "Yang Ming", "CarrierCode": "YMLU"},
    {"CarrierName": "HMM", "CarrierCode": "HDMU"},
    {"CarrierName": "PIL", "CarrierCode": "PABV"},
    {"CarrierName": "OOCL", "CarrierCode": "OOLU"}
]

# Realistic NVOCC names
nvocc_list = [
    "Zhongshan Logistics", "Global Freight Forwarders", "Hong Kong Express",
    "Cargo Movers Ltd", "Singapore Shipping Co", "TransAsia Logistics",
    "Atlantic Ocean Shipping", "Pacific Star Freight", "Logistics International Ltd",
    "WorldBridge Transport", "Everfast Logistics", "Skyline Shipping",
    "Seabridge Forwarding", "Neptune Freight"
]

# HTS Codes + Descriptions
hts_data = [
    {"HTSCode": "610910", "HTSDescription": "Cotton T-shirts"},
    {"HTSCode": "620462", "HTSDescription": "Women's cotton trousers"},
    {"HTSCode": "940360", "HTSDescription": "Wooden furniture"},
    {"HTSCode": "852872", "HTSDescription": "Flat panel TVs"},
    {"HTSCode": "640399", "HTSDescription": "Footwear, rubber/plastic"},
    {"HTSCode": "870899", "HTSDescription": "Auto parts"},
    {"HTSCode": "420222", "HTSDescription": "Leather handbags"},
    {"HTSCode": "850440", "HTSDescription": "Power supplies/adapters"},
    {"HTSCode": "841451", "HTSDescription": "Fans (air conditioning)"},
    {"HTSCode": "730890", "HTSDescription": "Steel structures"},
    {"HTSCode": "392690", "HTSDescription": "Plastic articles"},
    {"HTSCode": "854442", "HTSDescription": "Electric cables"},
    {"HTSCode": "950300", "HTSDescription": "Toys"},
    {"HTSCode": "940171", "HTSDescription": "Armchairs, upholstered"},
    {"HTSCode": "392310", "HTSDescription": "Plastic boxes, cases"},
    {"HTSCode": "850760", "HTSDescription": "Lithium-ion batteries"},
    {"HTSCode": "847130", "HTSDescription": "Laptop computers"},
    {"HTSCode": "841810", "HTSDescription": "Refrigerators/freezers"},
    {"HTSCode": "940350", "HTSDescription": "Wooden kitchen furniture"},
    {"HTSCode": "853710", "HTSDescription": "Electrical control boards"}
]

# US Ports
us_ports = [
    "Newark, NJ", "Los Angeles, CA", "Long Beach, CA", "Houston, TX", "Savannah, GA",
    "Miami, FL", "Seattle, WA", "Oakland, CA", "Charleston, SC", "Baltimore, MD",
    "Norfolk, VA", "Jacksonville, FL", "New Orleans, LA"
]

# World Ports
world_ports = {
    "CN": ["Shanghai", "Shenzhen", "Ningbo", "Qingdao", "Tianjin", "Xiamen", "Dalian"],
    "TR": ["Ambarli", "Mersin", "Izmir", "Gebze", "Gemlik"],
    "DE": ["Hamburg", "Bremerhaven"],
    "IN": ["Nhava Sheva", "Chennai", "Mumbai", "Kolkata"],
    "VN": ["Hai Phong", "Ho Chi Minh", "Da Nang"],
    "KR": ["Busan", "Incheon"],
    "BR": ["Santos", "Rio de Janeiro", "Paranagua"],
    "MX": ["Manzanillo", "Veracruz", "Altamira"],
    "ES": ["Valencia", "Barcelona", "Algeciras"],
    "GB": ["Felixstowe", "Southampton", "London Gateway"],
    "ID": ["Jakarta", "Surabaya"],
    "TH": ["Laem Chabang", "Bangkok"],
    "MY": ["Port Klang", "Penang"]
}

# Country full names
country_full_names = {
    "CN": "CHINA",
    "TR": "TURKIYE",
    "DE": "GERMANY",
    "IN": "INDIA",
    "VN": "VIETNAM",
    "KR": "SOUTH KOREA",
    "BR": "BRAZIL",
    "MX": "MEXICO",
    "ES": "SPAIN",
    "GB": "UNITED KINGDOM",
    "ID": "INDONESIA",
    "TH": "THAILAND",
    "MY": "MALAYSIA"
}

# Mapping for World Region by Country
world_regions = {
    "CN": "Asia",
    "TR": "Europe",
    "DE": "Europe",
    "IN": "Asia",
    "VN": "Asia",
    "KR": "Asia",
    "BR": "South America",
    "MX": "North America",
    "ES": "Europe",
    "GB": "Europe",
    "ID": "Asia",
    "TH": "Asia",
    "MY": "Asia"
}

# Consignee cities and correct states
us_cities_states = [
    ("Los Angeles", "CA"), ("New York", "NY"), ("Houston", "TX"), ("Miami", "FL"),
    ("Seattle", "WA"), ("Chicago", "IL"), ("Savannah", "GA"), ("Baltimore", "MD"),
    ("Charleston", "SC"), ("Oakland", "CA"), ("Norfolk", "VA"),
    ("New Orleans", "LA"), ("Atlanta", "GA")
]

# Generate one row
def generate_row(date_value):
    is_master = random.choice(["M", "H"])
    vocc = random.choice(vocc_data)
    nvocc_name = random.choice(nvocc_list)
    hts = random.choice(hts_data)
    
    shipper_country_code = random.choice(list(world_ports.keys()))
    shipper_country = country_full_names[shipper_country_code]
    shipper_city = random.choice(world_ports[shipper_country_code])
    consignee_city, consignee_state = random.choice(us_cities_states)

    shipper_name = fake.company() if is_master == "M" else nvocc_name
    consignee_name = fake.company()
    carrier_code = vocc["CarrierCode"]
    bill_number = (carrier_code if is_master == "M" else nvocc_name[:4].upper()) + str(random.randint(1000000, 9999999))
    port_of_departure = random.choice(world_ports[shipper_country_code])
    port_of_arrival = random.choice(us_ports)

    container_20 = random.randint(0, 100) if random.choice([True, False]) else 0
    container_40 = random.randint(0, 100) if container_20 == 0 else 0

    total_containers = container_20 + container_40
    metric_tons = round(random.uniform(1, 30), 2)
    kilograms = round(metric_tons * 1000, 2)
    teus = container_20 * 1 + container_40 * 2
    nvocc_field = nvocc_name if random.choice([True, False]) or is_master == "H" else ""

    return {
        "Date": date_value.strftime("%#m/%#d/%Y"),
        "Shipper": shipper_name,
        "Shipper City": shipper_city,
        "Shipper Country": shipper_country,
        "Consignee": consignee_name,
        "Consignee City": consignee_city,
        "Consignee State": consignee_state,
        "Carrier Code": carrier_code,
        "NVOCC": nvocc_field,
        "VOCC": vocc["CarrierName"],
        "Bill of Lading Nbr.": bill_number,
        "Master/House": is_master,
        "HTS Code": hts["HTSCode"],
        "HTS Description": hts["HTSDescription"],
        "Container Quantity 20'": container_20,
        "Container Quantity 40'": container_40,
        "Port of Arrival": port_of_arrival,
        "World Region by Port of Departure": world_regions[shipper_country_code],
        "Country by Port of Departure": shipper_country,
        "Port of Departure": port_of_departure,
        "Country of Origin": shipper_country,
        "Container Quantity": total_containers,
        "Metric Tons": metric_tons,
        "Kilograms": kilograms,
        "Teus Quantity": teus,
        "FCL/LCL": "FCL" if total_containers > 0 else "LCL"
    }

# Main Generator
def generate_data(start_date, end_date, start_rows=100, increment_per_day=1):
    current_date = start_date
    all_data = []
    rows_today = start_rows

    total_days = (end_date - start_date).days + 1

    for _ in tqdm(range(total_days), desc="Generating Data", unit="day"):
        for _ in range(rows_today):
            row = generate_row(current_date)
            all_data.append(row)
        rows_today += increment_per_day
        current_date += timedelta(days=1)

    return pd.DataFrame(all_data)

# Export Data
def export_data(df, output_folder, filename):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, filename)
    df.to_csv(output_path, index=False)
    print(f"Data exported successfully to {output_path}")

# --- MAIN SCRIPT ---

# Generate full dataset
start = datetime(2025, 1, 1)
end = datetime(2025, 4, 30)

df = generate_data(start, end)

# Exporting
export_folder = "exported_csv_files"
export_filename = "generated_data.csv"
export_data(df, export_folder, export_filename)
