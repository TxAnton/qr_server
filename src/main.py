import requests
import notion
import yaml
from notion.client import NotionClient
import pandas as pd


print(notion)
print(notion)

def main():
    # token_v2 = "ab2915fdd9ebae1de2933e483cfa153e437cd4d9be38ae05bb41a2d0ab5d78171d110fd52a1b2ddb01aca5ae8aaa99a3d0f4abc2546caa58a5f1cab9f8269695df11d01d055da7aec3eba87816cb"
    token = "secret_ASaG0rlzlH5XI8dUQbgy0mfGztVnyPm5VAplJLew5SJ"

    # database_id = "b503333bc8294c16a0d7f88dddda347f"
    database_id = "8945bff673dd47e3adae56ec2957825a"

    # uri = "https://www.notion.so/SCi-b503333bc8294c16a0d7f88dddda347f"
    url = f'https://api.notion.com/v1/databases/{database_id}/query'

    r = requests.post(url, headers={
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28"
    })
    result_dict = r.json()
    list_result = result_dict['results']
    yaml.dump(list_result)
    print(list_result)
    print(yaml.dump(list_result))
    # print(vars(r))






if __name__ == '__main__':
    main()

