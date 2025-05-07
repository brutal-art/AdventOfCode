import requests

# A modul letölti egy input_text változóba a napi feladathoz tartozó adatokat.

class AoCInputHandler:
    def __init__(self, session: str, year: int = 2024):
        self.session = session
        self.year = year

    def fetch_input(self, day: int) -> str:
        url = f"https://adventofcode.com/{self.year}/day/{day}/input"
        headers = {"Cookie": f"session={self.session}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text.strip()
    
    


# --- main rész külön, a fájl végén ---
if __name__ == '__main__':
    session = input("Illeszd be az Advent of Code session azonosítód: ").strip()
    day = int(input("Add meg a nap számát (1–25): ").strip())

    handler = AoCInputHandler(session)

    try:
        input_data = handler.fetch_input(day)
        print("Első 200 karakter az inputból:\n", input_data[:200], "...")
    except Exception as e:
        print(f"Hiba történt: {e}")