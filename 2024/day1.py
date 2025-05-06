import requests

session = input("Illeszd be az Advent of Code session azonosítód: ").strip()

url = "https://adventofcode.com/2024/day/1/input"
headers = {"Cookie": f"session={session}"}
response = requests.get(url, headers=headers)
response.raise_for_status()
input_text = response.text.strip()

left = []
right = []
dist = []

if response.ok:
    print("Sikeresen letöltve az adat:")
    print(response.text[:200], end='')
    print('...')  
else:
    print("Hiba a letöltés során:", response.status_code)


for line in input_text.splitlines():
    if line.strip():  # Üres sorok kihagyása
        parts = line.strip().split()
        if len(parts) == 2:
            l, r = map(int, parts)
            left.append(l)
            right.append(r)
        else:
            print(f"Hiba a sor feldolgozása során: '{line}'")

left, right = sorted(left), sorted(right)

for i, j in zip(left, right):
    dist.append(abs(i-j))

print(sum(dist))
