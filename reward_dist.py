class Contract:
    def __init__(self):
        self.T = 0
        self.S = 0
        self.stake = {}
        self.P = {}

    def deposit_stake(self, address, amount):
        if address not in self.stake:
            self.stake[address] = 0
            self.P[address] = 0

        self.stake[address] = self.stake[address] + amount
        self.P[address] = self.P[address] + self.S*amount
        self.T = self.T + amount

    def distribute(self, r):
        if self.T != 0:
            self.S = self.S + r/self.T
        else:
            raise Exception()

    def withdraw_stake(self, address, amount):
        if address not in self.stake:
            raise Exception()
        if amount > self.stake[address]:
            raise Exception()

        self.stake[address] = self.stake[address] - amount
        self.P[address] = self.P[address] - self.S*amount
        self.T = self.T - amount
        return amount

    def withdraw_reward(self, address):
        reward = self.stake[address]*self.S - self.P[address]
        self.P[address] = self.stake[address]*self.S
        return reward


addr1 = "0x1"
addr2 = "0x2"
contract = Contract()

contract.deposit_stake(addr1, 100)
contract.distribute(10)

contract.deposit_stake(addr2, 50)
contract.distribute(10)

contract.withdraw_stake(addr1, 100)
contract.distribute(10)


print(contract.withdraw_reward(addr1))
print(contract.withdraw_reward(addr1))
print(contract.withdraw_reward(addr2))


