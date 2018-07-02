# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # LPL-pandatv签到领竹子
    # GET https://pharah.gate.panda.tv/checkin/user

    try:
        response = requests.get(
            url="https://pharah.gate.panda.tv/checkin/user",
            params={
                "token": "6e3ac96ab6df9b0ba799f0dc08de6ca5",
                "app": "lpl2018summer",
            },
            headers={
                "Cookie": "pdftv1=ce1e6|163f854d141|7289|72ff2c8f|10; __guid=96554777.1165847274713262000.1528879699145.4216; Hm_lvt_204071a8b1d0b2a04c782c44b88eb996=1528879700; pdft=201806131648200dc0c13da8f153396a3394ed19af57e300a7dd8bf88dc7b0; smidV9=201806131648200dc0c13da8f153396a3394ed19af57e300a7dd8bf88dc7b0; SESSCYPHP=98c6773f8c046f4c55e32edeffe5e5e5; R=r%3D3238368%26u%3DCnaqnGi3238368%26n%3D%25R5%25O7%25O4%25R9%25OO%258R%25R5%25N4%259P%25R9%259O%25N8mm%26le%3DrJRyZxRyZxRyZxRyZxR2AFH0ZUSkYzAioD%3D%3D%26m%3DZGtmAwH4Zmp4BQR%3D%26im%3DnUE0pPHmDFHlEvHlEzx1YaOxnJ0hM3ZyZxMzZGD3AQt1ZQMwAmNkLJLkMQAwLmWyMQquAzR2LmL4BP5dpTIa%26p%3D%26i%3D; M=t%3D1528879772%26v%3D1.0%26mt%3D1528879772%26s%3D229b6bccbb4c96b7ec2f1723067416b2%26ps%3Da8c2d43c5f61372c602aca0a74b2e679; Hm_lpvt_204071a8b1d0b2a04c782c44b88eb996=1528879776; I=r%3D3238368%26t%3D6e3ac96ab6df9b0ba799f0dc08de6ca5",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
