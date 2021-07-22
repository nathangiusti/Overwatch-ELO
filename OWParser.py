import datetime

import GSheetDB

# Parses a copy/paste of the overwatch league results and pastes them in a google sheet

SPREADSHEET_ID = '1Pt_ezVf1PnIaOSeJi5An_BWXZJbIPymU0DXwyyGrf34'

SEASON = "2021"

def main():

    service = GSheetDB.GSheetDB('token.json', SPREADSHEET_ID)
    sheet = service.pages['Sheet1']

    file1 = open('input.txt', 'r')
    stage = "WEEK 32"
    sheet_rows = []
    while True:
        line = file1.readline()
        if not line:
            break
        date = datetime.datetime.strptime(line + ' ' + SEASON, '%a, %b %d %Y')
        line = file1.readline()
        line = file1.readline()
        line = file1.readline()

        team_1 = file1.readline().strip()
        file1.readline()
        team_1_score = int(file1.readline().strip())
        file1.readline()
        file1.readline()
        file1.readline()
        team_2_score = int(file1.readline().strip())
        file1.readline()
        team_2 = file1.readline().strip()
        file1.readline()
        file1.readline()
        file1.readline()
        if team_1_score > team_2_score:
            sheet_rows.append([SEASON, stage, team_1, team_1_score, team_2, team_2_score, date.strftime('%m/%d/%Y')])
        else:
            sheet_rows.append([SEASON, stage, team_2, team_2_score, team_1, team_1_score, date.strftime('%m/%d/%Y')])

    file1.close()
    sheet.add_rows(sheet_rows)
    print(stage)


if __name__ == '__main__':
    main()
