CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(128),
    subtitle VARCHAR(256),
    body TEXT,
    active BOOLEAN DEFAULT 1
);

INSERT INTO
    tasks (
        title,
        subtitle,
        body
    )
VALUES
    (
        'Wash the car',
        'Go outside and wash the car',
        'Either do it yourself or take it to a car wash'
    );

INSERT INTO
    tasks (title, subtitle, body)
VALUES
    (
        'Dinner',
        'Prepare dinner',
        "Tonight's dinner should be pizza or tacos; Buy or order"
    );