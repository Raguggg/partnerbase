import requests

def get_data(ip_d):
    slug = ip_d['slug']

    base_url = f"https://www.partnerbase.com/{slug}"
    company_name = ip_d['name']
    tmp = {
        "company_name": company_name,
        "url": base_url,
    }
    return tmp


headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ta;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'https://www.partnerbase.com/app/search/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}
data = []

for i in range(1,12):
    try:
        response = requests.get(
            f'https://www.partnerbase.com/v0.1/companies?page={i}&limit=5000&sort=partnerbaseScore|desc&sort=name|asc',
            # cookies=cookies,
            headers=headers,
        )
        print(response.status_code)
    except Exception as e:
        break

    tmps_data = [
        get_data(ip_d) for ip_d in response.json()['items']
    ]
    print(len(tmps_data))
    data.extend(tmps_data)
    print(len(data))
    if response.json()['pagination']['nextHref']:
        continue
    else:
        break

# convet list of dic data to pandas
import pandas as pd
df = pd.DataFrame(data)
# save to csv

df.to_csv('data.csv', index=False)


