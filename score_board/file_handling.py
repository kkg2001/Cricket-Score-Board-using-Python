def open_scores_file(filename):
    try:
        file=open("score_sheet.csv","r")
        scores=file.read()
        file.close()
        return scores
    except FileNotFoundError:
        return None

def save_scores_file(filename,scores):
    try:
        file=open("score_sheet.csv","w")
        file.write(scores)
        file.close()
        return True
    except:
        return False
        