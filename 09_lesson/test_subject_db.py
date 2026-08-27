from subject_table import SubjectTable
from config import connection_string


db = SubjectTable(connection_string)


def test_add_subject():
    max_id = db.max_subject_id()
    subject_id = max_id + 1
    subject_title = "Astronomy"
    db.add_subject(subject_id, subject_title)

    result = db.select_subject(subject_id)
    assert result[0]["subject_id"] == subject_id
    assert result[0]["subject_title"] == subject_title

    db.delete_subject(subject_id)


def test_update_subject():
    max_id = db.max_subject_id()
    subject_id = max_id + 1
    subject_title = "Astronomy"
    db.add_subject(subject_id, subject_title)

    new_title = "Ecology"
    db.update_subject(subject_id, new_title)
    result = db.select_subject(subject_id)
    assert result[0]["subject_title"] == new_title

    db.delete_subject(subject_id)


def test_delete_subject():
    max_id = db.max_subject_id()
    subject_id = max_id + 1
    subject_title = "Astronomy"
    db.add_subject(subject_id, subject_title)

    db.delete_subject(subject_id)

    result = db.select_subject(subject_id)
    assert len(result) == 0
