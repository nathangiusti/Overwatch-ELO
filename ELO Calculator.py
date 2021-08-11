from collections import OrderedDict

import GSheetDB

# Calculates ELO for all teams. Multiple views are created for ease of visualization.

k = 100
season_reset_factor = 5
SPREADSHEET_ID = '1Pt_ezVf1PnIaOSeJi5An_BWXZJbIPymU0DXwyyGrf34'

elo_dict = OrderedDict({
    "San Francisco Shock": 1500,
    "Shanghai Dragons": 1500,
    "Philadelphia Fusion": 1500,
    "Seoul Dynasty": 1500,
    "Paris Eternal": 1500,
    "Florida Mayhem": 1500,
    "Los Angeles Valiant": 1500,
    "Los Angeles Gladiators": 1500,
    "Atlanta Reign": 1500,
    "Houston Outlaws": 1500,
    "Dallas Fuel": 1500,
    "Washington Justice": 1500,
    "Toronto Defiant": 1500,
    "Vancouver Titans": 1500,
    "Boston Uprising": 1500,
    "New York Excelsior": 1500,
    "Guangzhou Charge": 1500,
    "Hangzhou Spark": 1500,
    "Chengdu Hunters": 1500,
    "London Spitfire": 1500
})

SEASON_COL = 1
STAGE_COL = 2
WINNING_TEAM_COL = 3
WIN_SCORE_COL = 4
LOSING_TEAM_COL = 5
LOSE_SCORE_COL = 6
DATE_COL = 7


def calculate_elo(winning_team_rating, losing_team_rating, margin):
    e1 = winning_team_rating/(winning_team_rating + losing_team_rating)
    e2 = losing_team_rating/(winning_team_rating + losing_team_rating)
    r1 = winning_team_rating + k * (1 - e1) * margin
    r2 = losing_team_rating - k * e2 * margin
    return [r1, r2]


def main():
    elo_time_upload = [['ROW NUMBER', 'SEASON', 'STAGE', 'TEAM', 'ELO', 'DATE']]
    elo_diff_upload = [['GAME ID', 'TEAM', 'ELO DIFF']]
    service = GSheetDB.GSheetDB('token.json', SPREADSHEET_ID)
    dim_games_sheet = service.pages['Sheet1']
    elo_time_sheet = service.pages['Sheet2']
    elo_change_sheet = service.pages['Sheet3']
    games = dim_games_sheet.get_all_values()
    season = games[0][SEASON_COL]
    row_count = 0
    for row in games:
        stage = row[STAGE_COL]
        if row[SEASON_COL] != season:
            for key, val in elo_dict.items():
                elo_dict[key] = 1500 + (val - 1500)/season_reset_factor
            season = row[SEASON_COL]

        winning_team = row[WINNING_TEAM_COL]
        losing_team = row[LOSING_TEAM_COL]
        date = row[DATE_COL]

        elo_arr = calculate_elo(elo_dict[winning_team], elo_dict[losing_team], int(row[WIN_SCORE_COL]) - int(row[LOSE_SCORE_COL]))

        win_diff = elo_arr[0] - elo_dict[winning_team]
        loss_diff = elo_arr[1] - elo_dict[losing_team]
        elo_diff_upload.append([row[0], winning_team, win_diff])
        elo_diff_upload.append([row[0], losing_team, loss_diff])

        elo_dict[winning_team] = elo_arr[0]
        elo_dict[losing_team] = elo_arr[1]
        row_count += 1
        elo_time_upload.append([row_count, season, stage, winning_team, elo_arr[0], date])
        row_count += 1
        elo_time_upload.append([row_count, season, stage, losing_team, elo_arr[1], date])

    elo_time_sheet.add_rows(elo_time_upload)
    elo_change_sheet.add_rows(elo_diff_upload)
    print("done")


if __name__ == '__main__':
    main()
