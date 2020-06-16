from datetime import datetime

FILE = "src/highscores.dat" 

def compare_points(pair):
    return pair[0]

class HighscoreHandler:
    def __init__(self):
        self.scores = []
    def load_highscores(self):
        try:
            with open(FILE, "r") as data:
                for line in data:
                    time, points = line[:-1].split("|")
                    self.scores.append((int(points), time))
        except FileNotFoundError:
            pass
        self.scores.sort(reverse=True, key=compare_points)
    def add_highscore(self, points):
        time = datetime.now().strftime("%d-%m-%Y %Hh%Mm%Ss")
        self.scores.append((points, time))
        self.scores.sort(reverse=True, key=compare_points)
    def get_top_scores(self):
        empty = {"points": "N/A", "day": "  No score", "time": "  No score"}
        if len(self.scores) > 0:
            first = {"points": str(self.scores[0][0]), "day": self.scores[0][1][:10], "time": self.scores[0][1][11:]}
        else:
            return [empty, empty, empty]
        if len(self.scores) > 1:
            second = {"points": str(self.scores[1][0]), "day": self.scores[1][1][:10], "time": self.scores[1][1][11:]}
        else:
            return [first, empty, empty]
        if len(self.scores) > 2:
            third = {"points": str(self.scores[2][0]), "day": self.scores[2][1][:10], "time": self.scores[2][1][11:]}
        else:
            return [first, second, empty]
        return [first, second, third]
    def save_highscores(self):
        with open(FILE, "w+") as data:
            for score in self.scores:
                data.write(score[1] + "|" + str(score[0]) + "\n")