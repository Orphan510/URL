import requests
import os
os.system("clear")
print ("\033[93m welcome")
print ()
print ("This simple tool is made by the Orphan of the Lulzsec Black team")
print ()
print("Don't forget to follow my Instagram account orphan_cyber")
print()
print ()
def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

# طلب الرابط من المستخدم
long_url = input("Enter the link you want to shorten:\n")

# اختصار الرابط
short_url = shorten_url(long_url)
if short_url:
    print(f"short link: {short_url}")
else:
    print("The link has not been shortened, there is a problem, try again")
