# Result of joining the database schema tables
METADATA = {
    "dty_ID": 1090,
    "rst_DisplayName": "language",
    "dty_Type": "enum",
    "rst_MaxValues": 0,
}

# Result of a record's JSON export
DETAIL = [
    {
        "dty_ID": 1090,
        "value": "9728",
        "termLabel": "dum (Middle Dutch)",
        "termCode": "dum",
        "fieldName": "language",
        "fieldType": "enum",
        "conceptID": "",
    },
    {
        "dty_ID": 1090,
        "value": "9470",
        "termLabel": "fro (Old French)",
        "termCode": "fro",
        "fieldName": "language",
        "fieldType": "enum",
        "conceptID": "",
    },
]

# Detail's Pydantic field validation alias
# and the field's value for the Pydantic model
PYDANTIC_KEY_VALUE = {
    "DTY1090": ["dum (Middle Dutch)", "fro (Old French)"],
    "DTY1090_TRM": [9728, 9470],
}

# Detail's serialization from the Pydantic field
ALIAS_KEY_VALUE = {
    "language_COLUMN": ["dum (Middle Dutch)", "fro (Old French)"],
    "language_COLUMN TRM-ID": [9728, 9470],
}
