import requests
import json

API_KEY = "" # contact t.me/scrapguru for test key

def sign(url, headers):
    if API_KEY == "":
        raise Exception("API key is required")

    payload = json.dumps({
        "url": url,
        "headers": headers,
        "aid": 3019,
        "license_id": 1611921764,
        "sdk_version_str": "v04.04.05-ov-android",
        "sdk_version": 134744640,
        "sec_device_id": "AnPPIveUCQlIiFroHGG17nXK6",
        "platform": 0
    })
    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
    }
    r = requests.post("https://tiktokapi.dev/sign", headers=headers, data=payload)
    return r.json()

url = "https://api16-normal-useast5.us.tiktokv.com/aweme/v1/user/profile/other/?user_id=6868565347890299906&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230703&version_name=23.7.3&device_platform=android&ab_version=23.7.3&ssmix=a&device_type=POT-LX17&device_brand=HUAWEI&device_model=POT-LX17&language=en&os_api=29&os_version=10&manifest_version_code=2022307030&resolution=1080%2A2340&dpi=480&update_version_code=2022307030&app_skin=white&app_type=normal&sys_region=US&pass-route=1&mcc_mnc=31050&pass-region=1&timezone_name=America%252FNew_York&carrier_region_v2=310&cpu_support64=true&host_abi=arm64-v8a&app_language=en&carrier_region=US&ac2=wifi&uoo=0&op_region=US&timezone_offset=-14400&build_number=23.7.3&locale=en&region=US&openudid=bab65b3c159a4542&cdid=1856ed1e-b818-44b1-8bf1-136ff95e429a&device_id=7187122281045952042&iid=7187123175168165678&_rticket=1674146527532&ts=1674146588"
headers = {
    "sdk-version": "2",
    "user-agent": "com.zhiliaoapp.musically/2022307030 (Linux; U; Android 10.0.0; en; Samsung; Build/OPR6.1674146527.017;tt-ok/3.10.0.2)",
    "x-ss-req-ticket": "1674146527532",
    "passport-sdk-version": "19",
    "x-vc-bdturing-sdk-version": "2.2.1.i18n",
    "x-tt-dm-status": "login=0;ct=1;rt=7",
    "x-tt-store-idc": "useast5",
    "x-tt-store-region": "us",
    "x-tt-store-region-src": "uid",
    "cookie": "install_id=7187123175168165678; store-country-code=us; store-country-code-src=did; store-idc=useast5; ttreq=1$1b75e317092d0c7549eb4cc58df50fae2a7a8664",
    "accept-encoding": "gzip"
}

xaxl = sign(url, headers)
for x in xaxl:
    headers[x] = str(xaxl[x])

r = requests.get(url, headers=headers)
print(r.text)
