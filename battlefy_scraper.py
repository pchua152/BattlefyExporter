import requests
import csv
import json


def start():
    link = input("Paste the a link of any page from the battlefy tour\n")
    option = input("Press 1 for exporting all teams, press 2 for looking a specific IGN's team\n")
    match option:
        case '1':
            print(export_to_excel(link))
        case '2':
            IGN = input("Type the IGN of the user you wish to get the team of\n")
            print(get_team(link,IGN))
        case _:
           print("Invalid option")
        
def get_id(link):
    battlefy_link = link.split('/')
    battlefy_id = battlefy_link[5]
    return battlefy_id


def export_to_excel(battlefy_link: str):
    
    battlefy_id = get_id(battlefy_link)
    try:
        if(battlefy_id):
            requesturl = f'https://dtmwra1jsgyb0.cloudfront.net/tournaments/{battlefy_id}/teams'
            htmldata = requests.get(requesturl)
            data = json.loads(htmldata.content.decode('utf-8'))
            result = {}
            for s in data:
                        # Pokepaste link

                result[s['captain']['username']] = ((s['name'], s['customFields'][1]['value']))

            with open('teams.csv','w',newline='',encoding = 'utf-8') as csvfile:
                headers = ['BattlefyName', 'IGN', 'Pokepaste']
                teamwrite = csv.writer(csvfile)
                teamwrite.writerow(headers)
                for x,y in result.items():
                    hyperlink = f'=HYPERLINK("{y[1]}")'
                    teamwrite.writerow([x,y[0],hyperlink])
                    
    
        return "Teams written to teams.csv"
    except:
        return "Invalid link"
    

def get_team(battlefy_link: str, name):
    battlefy_id = get_id(battlefy_link)
    try:
        if battlefy_id:
            requesturl = f'https://dtmwra1jsgyb0.cloudfront.net/tournaments/{battlefy_id}/teams'
            htmldata = requests.get(requesturl)
            data = json.loads(htmldata.content.decode('utf-8'))
            result = []
            for s in data:
                if s['name'] == name:
                    result.append((s['customFields'][1]['value']))
        return result
            
    except:
        return "Invalid link"

if __name__ == "__main__":
    start()