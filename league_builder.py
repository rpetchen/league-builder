import csv
import random

def teamGenerator():
    teamDictionary = {"Sharks": [],
                      "Dragons": [],
                      "Raptors": []
                      }

    experiencedPlayers = []
    inexperiencedPlayers = []

    f = open('soccer_players.csv', 'r')
    csv_f = csv.DictReader(f)
    for row in csv_f:
        name = row['Name']
        height = row['Height (inches)']
        experience = row['Soccer Experience']
        guardians = row['Guardian Name(s)']
        player = {name : {"height" : height,
                          "experience": experience,
                          "guardians": guardians,
                          }}
        if experience == 'YES':
            experiencedPlayers.append(player)
        else:
            inexperiencedPlayers.append(player)

    assignPlayers(teamDictionary, experiencedPlayers, inexperiencedPlayers)

    writeTeams(teamDictionary)



def assignPlayers(teamDictionary, experiencedPlayers, inexperiencedPlayers):
    dictLookup = ["Sharks", "Dragons", "Raptors"]

    random.shuffle(experiencedPlayers)
    random.shuffle(inexperiencedPlayers)

    for i in range(len(experiencedPlayers)):
        dictionaryTeam = dictLookup[i % 3]
        teamDictionary[dictionaryTeam].append(experiencedPlayers[i])

    for i in range(len(inexperiencedPlayers)):
        dictionaryTeam = dictLookup[i % 3]
        teamDictionary[dictionaryTeam].append(inexperiencedPlayers[i])


def writeTeams(teamDictionary):
    f = open('teams.txt', 'w')
    for team in teamDictionary:
        f.write(team + "\n")
        for player in teamDictionary[team]:
            for k,v in player.items():
                f.write("{}, {}, {}".format((k),(v['experience']), (v['guardians'])))
                f.write('\n')
        f.write('\n')

if __name__ == "__main__":
    teamGenerator()