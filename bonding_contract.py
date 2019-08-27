from math import sqrt, floor

class Agent:
    def __init__(
            self,
            balance=10000,
            referrer=None,
            name=None,
            active_at_quantity=0):

        self.balance = balance
        self.results = []
        self.games = []


class BondingContract:
    def __init__(
            self,
            initial_price=0.00001,
            price_increment=1e-11,
            div_ratio=0.1,
    ):

        self.holdings = {} # how much each agent owns
        self.sold = {} # how much each agent has sold
        self.referral_balances = {}
        self.referrals_left = {}

        self.payouts_to = {}

        self.initial_price = initial_price
        self.price_increment = price_increment
        self.div_ratio = div_ratio

        self.supply = 0
        self.profit_per_share = 0
        self.bonded_balance = 0

    def init_agent(self, agent):
        self.holdings[agent] = 0
        self.payouts_to[agent] = 0
        self.sold[agent] = 0

    def get_bonded_eth(self):
        return self._tokens_to_ethereum(self.supply)

    def buy(self, agent, eth_amount):

        if agent not in self.holdings:
            self.init_agent(agent)

        bonded_eth = self.get_bonded_eth()

        divs = eth_amount*self.div_ratio
        taxed_eth = eth_amount - divs

        token_amount = self._ethereum_to_tokens(taxed_eth)

        fee = divs

        if self.supply > 0.:
            self.supply += token_amount
            self.profit_per_share += divs/self.supply
            fee = token_amount*divs/self.supply
        elif self.supply == 0.:
            self.supply = token_amount
        else:
            raise Exception('No more tokens can be sold')

        self.holdings[agent] += token_amount
        updated_payouts = self.profit_per_share*token_amount-fee

        # import ipdb; ipdb.set_trace()
        self.payouts_to[agent] += updated_payouts

        agent.balance -= eth_amount
        self.bonded_balance += eth_amount

        # agent.bought_godl(token_amount)

    def sell(self, agent, token_amount):

        assert(self.holdings[agent] > token_amount)

        free_tokens = self.supply

        if token_amount > free_tokens:
            raise Exception('Cannot sell more than %g tokens'%(free_tokens))

        if not agent in self.holdings:
            return

        eth_amount = self._tokens_to_ethereum(token_amount)
        divs = eth_amount*self.div_ratio

        taxed_eth = eth_amount - divs

        self.supply -= token_amount
        self.holdings[agent] -= token_amount

        updated_payouts = self.profit_per_share*token_amount + taxed_eth
        # import ipdb; ipdb.set_trace()
        self.payouts_to[agent] -= updated_payouts

        if self.supply > 0:
            self.profit_per_share += divs/self.supply

        self.sold[agent] += token_amount

    def sell_price(self):
        return self._tokens_to_ethereum(1)*1.1

    def sell_all(self, agent):
        if not agent in self.holdings:
            return

        free_tokens = self.supply

        self.sell(agent, min(self.holdings[agent], free_tokens)-1e-4)

    def withdraw(self, agent):
        if not agent in self.holdings:
            return

        divs = self.dividends_of(agent)
        self.payouts_to[agent] += divs

        agent.balance += divs
        self.bonded_balance -= divs

    def _tokens_to_ethereum(self, token_amount):
        return token_amount*self.initial_price \
            + token_amount*self.price_increment*self.supply \
            - 0.5*token_amount**2*self.price_increment

    def _ethereum_to_tokens(self, eth_amount):
        result = (sqrt(self.supply**2*self.price_increment**2
                       + 2*eth_amount*self.price_increment
                       + 2*self.supply*self.initial_price*self.price_increment
                       + self.initial_price**2)
                  -self.initial_price)/self.price_increment - self.supply

        return result

    def dividends_of(self, agent):
        if not agent in self.holdings or not agent in self.payouts_to:
            return 0

        # import ipdb; ipdb.set_trace()
        return self.profit_per_share*self.holdings[agent]-self.payouts_to[agent]

    def calc_median_price(self):
        return self.initial_price + self.supply*self.price_increment

    def contract_info(self):
        result = ''
        result += 'Current supply: %d tokens\n'%self.supply
        result += 'Current price: %g ETH/token\n'%self.calc_median_price()
        result += 'ETH in contract: %g ETH\n'%self.bonded_balance

        return result

    def agent_info(self, agent):
        if agent in self.holdings:
            holdings = self.holdings[agent]
            divs = self.dividends_of(agent)
        else:
            holdings = 0
            divs = 0

        result = ''
        result += 'Agent balance: %.3f ETH\n'%agent.balance
        result += 'Agent token balance: %d GODL\n'%holdings
        result += 'Agent token balance (converted): %.3f ETH\n'%(self._tokens_to_ethereum(holdings)*0.9)
        result += 'Agent total divs+sold: %.3f ETH\n'%divs

        return result


contract = BondingContract()
agent1 = Agent()
agent2 = Agent()

contract.buy(agent1, 1000)
contract.buy(agent2, 1000)

contract.sell_all(agent1)
contract.sell_all(agent2)

contract.withdraw(agent1)
contract.withdraw(agent2)

print(contract.contract_info())

print(contract.agent_info(agent1))
print(contract.agent_info(agent2))
