import psycopg2
import datetime as dt


def update_posts(title, content, currentpost_id):
    conn = psycopg2.connect(dbname='blog-posts', user='postgres', host='localhost', password='Uakkes04', port=5432)
    cur = conn.cursor()
    if title == '' or content == '':
        return 0
    cur.execute("""UPDATE posts_post SET title = %s, main_post = %s, created_at = %s WHERE id = %s""",
                (title, content, dt.datetime.now(), currentpost_id))
    conn.commit()
    cur.close()
    conn.close()


def get_posts():
    pass


def new_post(title, content, user):
    conn = psycopg2.connect(dbname='blog-posts', user='postgres', host='localhost', password='Uakkes04', port=5432)
    cur = conn.cursor()
    if title == '' or content == '':
        return 0
    cur.execute("""INSERT INTO posts_post (title, main_post, created_at, username) VALUES (%s, %s, %s, %s);""",
                (title, content, dt.datetime.now(), user))
    conn.commit()
    cur.close()
    conn.close()
