import requests

r = requests.get("http://api.open-notify.org/astros.json")
astros = r.json()

print(f"""People in space: {astros["number"]}""")
for person in astros["people"]:
	print(f"""{person["name"]} is on the {person["craft"]}.""")
