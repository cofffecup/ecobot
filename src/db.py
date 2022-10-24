import sqlite3



# def add_user(chat_id, login_, campus_, type_):
    # con = sqlite3.connect('Dataset/book_bot.db')
    # cursor = con.cursor()
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


def get_info(num):
    con = sqlite3.connect('ecobot.db')
    cursor = con.cursor()
    tmp = "SELECT name, link, about FROM items WHERE item_type_id = " + str(num)
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchall()
    cursor.close()
    con.close()
    return res
