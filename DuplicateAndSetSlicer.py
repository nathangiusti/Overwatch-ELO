import Report

# Since we don't have a good way to allow people to play with the dashboard dynamically we output them as pdf.
# We create one view and then duplicate that view while changing the filter.
# This script uses PowerPy to programatically duplicate sections.

TEAM_LIST_ARR = [
    'ATLANTA REIGN',
    'BOSTON UPRISING',
    'CHENGDU HUNTERS',
    'DALLAS FUEL',
    'FLORIDA MAYHEM',
    'GUANGZHOU CHARGE',
    'HANGZHOU SPARK',
    'HOUSTON OUTLAWS',
    'LONDON SPITFIRE',
    'LOS ANGELES GLADIATORS',
    'LOS ANGELES VALIANT',
    'NEW YORK EXCELSIOR',
    'PARIS ETERNAL',
    'PHILADELPHIA FUSION',
    'SAN FRANCISCO SHOCK',
    'SEOUL DYNASTY',
    'SHANGHAI DRAGONS',
    'TORONTO DEFIANT',
    'VANCOUVER TITANS',
    'WASHINGTON JUSTICE'
]


def main():
    report = Report.Report('OWL ELO.pbix')
    section = report.get_sections()[1]
    for team in TEAM_LIST_ARR:
        dupe_section = report.duplicate_section(section, team)
        slicer = dupe_section.get_visuals_by_type('slicer')[1]
        slicer.set_slicer_value(team)
    report.publish_pbix('MyNewPBIX.pbix')


if __name__ == "__main__":
    main()