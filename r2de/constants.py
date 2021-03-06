# data folder
DATA_PATH = 'data/'

# filenames
ANSWERS_TEXT_FILENAME = 'answers_texts.csv'
DETAILED_QS_ANSWERS_FILENAME = 'detailed_quiz_session_answer.csv'
DS_GTE_FILENAME = 'DS_GTE.csv'
DS_VAL_FILENAME = 'DS_VAL.csv'
QUESTION_COUNT_FILENAME = 'questions_counts.csv'

# headers
CORRECT_HEADER = 'correct'
COUNT_HEADER = 'count'
DESCRIPTION_HEADER = 'description'
DIFFICULTY_KEY = 'difficulty'
DISCRIMINATION_KEY = 'discrimination'
FEATURES_HEADER = 'features'
ID_HEADER = 'id'
QUESTION_ID_HEADER = 'question_id'
QUESTION_TEXT_HEADER = 'question_text'
TARGET_DIFFICULTY_HEADER = 'target_difficulty'
TARGET_DISCRIMINATION_HEADER = 'target_discrimination'
TIMESTAMP_HEADER = 'time_stamp'
USER_ID_HEADER = 'user_id'

# values used in the IRT estimation
DIFFICULTY_MIN = -5.0
DIFFICULTY_MAX = 5.0
DEFAULT_DISCRIMINATION = 1.0
DISCRIMINATION_MIN = -1.0
DISCRIMINATION_MAX = 2.5
DEFAULT_GUESS = 0.0
DEFAULT_SLIP = 0.0

DETAILED_QS_ANSWERS_COLUMNS = [
    USER_ID_HEADER,
    TIMESTAMP_HEADER,
    CORRECT_HEADER,
    QUESTION_ID_HEADER,
    QUESTION_TEXT_HEADER,
]
QUESTION_COUNT_COLUMNS = [QUESTION_ID_HEADER, COUNT_HEADER]
ANSWERS_TEXT_COLUMNS = [CORRECT_HEADER, DESCRIPTION_HEADER, ID_HEADER, QUESTION_ID_HEADER]
