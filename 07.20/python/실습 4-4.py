black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

users_info = [{'company': 'Deckow-Crist',
  'lat': '-43.9509',
  'lng': '-34.4618',
  'name': 'Ervin Howell'},
 {'company': 'Romaguera-Jacobson',
  'lat': '-68.6102',
  'lng': '-47.0653',
  'name': 'Clementine Bauch'},
 {'company': 'Keebler LLC',
  'lat': '-31.8129',
  'lng': '62.5342',
  'name': 'Chelsey Dietrich'},
 {'company': 'Considine-Lockman',
  'lat': '-71.4197',
  'lng': '71.7478',
  'name': 'Mrs. Dennis Schulist'},
 {'company': 'Johns Group',
  'lat': '24.8918',
  'lng': '21.8984',
  'name': 'Kurtis Weissnat'},
 {'company': 'Hoeger LLC',
  'lat': '-38.2386',
  'lng': '57.2232',
  'name': 'Clementina DuBuque'}]

def censorship(i):
    if i['company'] in black_list:
        print(f"{i['company']} 소속의 {i['name']} 은/는 등록할 수 없습니다.")
        return False
    else:
        print("이상 없습니다.")
        return True
    
def create_user(n):
    censored_user_list = {}
    for i in n:
        if censorship(i) == True:
            censored_user_list[i['company']] = [i['name']]
    return censored_user_list

print(create_user(users_info))