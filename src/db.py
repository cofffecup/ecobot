import sqlite3


# def add_user(chat_id, login_, campus_, type_):
#     con = sqlite3.connect('Dataset/book_bot.db')
#     cursor = con.cursor()
#     tmp = "INSERT INTO users (chat_id, login, campus, type) VALUES (" + str(chat_id) + ", '" \
#           + login_ + "', '" + campus_ + "', '" + type_ + "')"
#     try:
#         cursor.execute(tmp)
#     except sqlite3.IntegrityError:
#         cursor.close()
#         con.close()
#         return False
#     else:
#         con.commit()
#         cursor.close()
#         con.close()
#         return True
#
#
# def get_campus(chat_id):
#     con = sqlite3.connect('Dataset/book_bot.db')
#     cursor = con.cursor()
#     tmp = "SELECT campus FROM users WHERE chat_id = '" + str(chat_id) + "'"
#     cursor.execute(tmp)
#     res = cursor.fetchone()
#     cursor.close()
#     con.close()
#     return res[0]


def get_map():
    pass


def get_ivents():
    pass


def get_trash_info():
    pass


def get_organizations():
    pass


def get_apps():
    pass


def get_sorting():
    pass


def get_reuse():
    pass


def saving():
    pass


def get_article():
    pass


def get_video():
    pass
