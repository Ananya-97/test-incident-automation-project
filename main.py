import csv
def ttcount(team_count, team):
    if team in team_count:
        team_count[team] += 1
    else:
        team_count[team] = 1  
def pttcount(p_team_count, team):
    if i["priority"] == "P1":
        if team in p_team_count:
            p_team_count[team] += 1
        else:
            p_team_count[team] = 1
with open("incidents.csv", "r") as f:
    r = csv.DictReader(f)
    tot = 0
    open = 0
    pri = 0
    team_count = {}
    p_team_count = {}
    print("===== CRITICAL OPEN INCIDENTS =====")
    for i in r:
        tot +=1
        if i["priority"] == "P1":
            pri += 1
        if i["status"].lower() == "open":
            open += 1
        if i["status"] == "Open" and i["priority"] == "P1":
            print(i["id"], i["team"])
        ttcount(team_count, i["team"])
        pttcount(p_team_count, i["team"])
    print("===== INCIDENT REPORT =====")
    print("Total:", tot)
    print("P1:", pri)
    print("Open:", open)
    print("===== TEAMS REPORT =====")
    for team, count in team_count.items():
            print(team, ":", count)
    print("===== TEAM P COUNT REPORT =====")
    for team, count in p_team_count.items():
        print(team, ":", count)