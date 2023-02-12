import os

FILE_DIRECTORY = 'storage'
RANKINGS_FILENAME = 'high_score.txt'
MAX_SCORES = 3


# TODO: visualize top 10 results
def store_high_score(score):
    filepath = __verify_filepath_available(RANKINGS_FILENAME)
    latest_scores = read_high_scores(filepath)

    if len(latest_scores) < MAX_SCORES:
        latest_scores.append(score)
        __store_scores(filepath, latest_scores)
    else:
        min_score = min(latest_scores)
        # print('MIN SCORE: ', min_score, ' | ', 'STR SCORE: ', score)
        if score > min_score:
            # print('STR SCORE IS HIGHER')
            min_score_index = latest_scores.index(min_score)
            latest_scores[min_score_index] = score
            latest_scores.sort(reverse=True)
            __store_scores(filepath, latest_scores)


def read_top_score():
    filepath = os.path.join(FILE_DIRECTORY, RANKINGS_FILENAME)
    if os.path.exists(filepath):
        return read_high_scores(filepath)[0]
    return 0


def read_high_scores(filepath):
    with open(filepath, 'r') as file:
        stored_scores = [int(score) for score in file.read().splitlines()]
        # print("READ: ", stored_scores)
        return stored_scores


def __store_scores(filepath, scores):
    with open(filepath, 'w') as file:
        content = '\n'.join(map(str, scores))
        # print("stringified content before write: ", content)
        file.write(content)


def __verify_filepath_available(filename):
    if not os.path.exists(FILE_DIRECTORY):
        os.mkdir(FILE_DIRECTORY)

    filepath = os.path.join(FILE_DIRECTORY, filename)
    if not os.path.exists(filepath):
        fd = open(filepath, 'x')
        fd.close()

    return filepath
