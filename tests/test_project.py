from project import add_income, add_expense


def test_add_income(monkeypatch):
    transactions = []

    inputs = iter(["5000", "Salary", "Monthly salary"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_income(transactions)

    assert transactions[0]["type"] == "income"
    assert transactions[0]["amount"] == 5000
    assert transactions[0]["category"] == "Salary"


def test_add_expense(monkeypatch):
    transactions = []

    inputs = iter(["2000", "Food", "Lunch"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_expense(transactions)

    assert transactions[0]["type"] == "expense"
    assert transactions[0]["amount"] == 2000
    assert transactions[0]["category"] == "Food"