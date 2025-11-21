financiero-api/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   │       ├── user.py
│   │       ├── account.py
│   │       ├── category.py
│   │       └── transaction.py
│   ├── core/
│   │   ├── config.py
│   │   └── utils.py
│   └── services/
│       └── parsing/
│           ├── chase_csv.py
│           └── capital_one_csv.py
│
├── alembic.ini
├── requirements.txt
└── README.md