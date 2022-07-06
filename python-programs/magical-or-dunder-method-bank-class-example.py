"""
REFERENCE: https://dbader.org/blog/python-dunder-methods

Enriching a Simple Account Class
Throughout this article I will enrich a simple Python class with various dunder methods to unlock the following language features:

Initialization of new objects
Object representation
Enable iteration
Operator overloading (comparison)
Operator overloading (addition)
Method invocation
Context manager support (with statement)
"""


from functools import total_ordering


@total_ordering
class Account:
    'A simple account class'

    def __init__(self, owner, amount=0):
        'This is the constructor that lets us create objects from this class'
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(self.owner,
                                                               self.amount)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        owner = '{}&{}'.format(self.owner, other.owner)
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc

    def __call__(self):
        print('Start amount: {}'.format(self.amount))
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))

    def __enter__(self):
        print('ENTER WITH: making backup of transactions for rollback')
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT WITH:', end=' ')
        if exc_type:
            self._transactions = self._copy_transactions
            print('rolling back to previous transactions')
            print('transaction resulted in {} ({})'.format(exc_type.__name__, exc_val))  # noqa E501
        else:
            print('transaction ok')

def validate_transaction(acc, amount_to_add):
    with acc as a:
        print('Adding {} to account'.format(amount_to_add))
        a.add_transaction(amount_to_add)
        print('New balance would be: {}'.format(a.balance))
        if a.balance < 0:
            raise ValueError('sorry cannot go in debt!')

if __name__ == '__main__':
    acc = Account('bob', 10)
    acc.add_transaction(20)
    acc.add_transaction(-10)
    acc.add_transaction(50)
    acc.add_transaction(-20)
    acc.add_transaction(30)
    assert acc.balance == 80
    assert list(reversed(acc)) == [30, -20, 50, -10, 20]

    print(acc.balance)
    print(len(acc))
    print(acc[3])
    for i, t in enumerate(acc):
        print(f"acc[{i}]", t, sep=":", end=", ")

    print()
    print("Reversed Transactions: ", list(reversed(acc)))

    acc2 = Account('tim', 100)
    print("Account1 Balance", acc.balance , 
          "Account2 Balance" , acc2.balance, 
          "Account2 > Account1: ", acc2 > acc )
    
    print(acc + acc2)
    acc()

    validate_transaction(acc2, 20)
