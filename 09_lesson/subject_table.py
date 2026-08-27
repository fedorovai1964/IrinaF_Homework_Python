from sqlalchemy import create_engine, text


class SubjectTable:
    scripts = {
        "select": text("select * from subject"),
        "select_by_id": text(
            "select * from subject where subject_id = :subject_id"),
        "max_subject_id": text("select MAX(\"subject_id\") from subject"),
        "insert": text("insert into subject \
                       (\"subject_id\", \"subject_title\") values \
                       (:subject_id, :subject_title)"),
        "update": text("update subject set subject_title = :subject_title\
                        where subject_id = :subject_id"),
        "delete": text("delete from subject where subject_id = :subject_id")
        }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def select(self):
        with self.db.connect() as connection:
            results = connection.execute(SubjectTable.scripts["select"])
            rows = results.mappings().all()
            return rows

    def select_subject(self, subject_id):
        with self.db.connect() as connection:
            result = connection.execute(
                self.scripts["select_by_id"], {"subject_id": subject_id})
            subject = result.mappings().all()
            return subject

    def add_subject(self, subject_id, subject_title):
        with self.db.connect() as connection:
            with connection.begin():
                connection.execute(
                    self.scripts["insert"], {
                        "subject_id": subject_id,
                        "subject_title": subject_title})

    def delete_subject(self, subject_id):
        with self.db.connect() as connection:
            with connection.begin():
                connection.execute(
                    self.scripts["delete"], {"subject_id": subject_id})

    def update_subject(self, subject_id, subject_title):
        with self.db.connect() as connection:
            with connection.begin():
                connection.execute(self.scripts["update"], {
                    "subject_id": subject_id,
                    "subject_title": subject_title})

    def max_subject_id(self):
        with self.db.connect() as connection:
            result = connection.execute(self.scripts["max_subject_id"])
            max_id = result.scalar()
            return max_id
