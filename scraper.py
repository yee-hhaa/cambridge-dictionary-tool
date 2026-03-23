import requests
from bs4 import BeautifulSoup

def lookup_cambridge(word):
    # 這是你指定的英英字典網址結構
    url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
    
    # 模擬瀏覽器，否則會被網站阻擋
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 抓取定義 (Cambridge 的英文定義通常在 ddef_d 標籤內)
            definition = soup.find('div', class_='def ddef_d db')
            # 抓取例句 (通常在 deg 標籤內)
            example = soup.find('span', class_='eg deg')

            print(f"\n===== Word: {word} =====")
            if definition:
                print(f"Definition: {definition.get_text().strip()}")
            else:
                print("Sorry, could not find the definition.")
                
            if example:
                print(f"Example: {example.get_text().strip()}")
            print("=" * (12 + len(word)))
        else:
            print(f"Error: Unable to access the page (Status code: {response.status_code})")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        target = input("\nEnter a word to look up (or 'q' to quit): ").lower().strip()
        if target == 'q':
            break
        if target:
            lookup_cambridge(target)