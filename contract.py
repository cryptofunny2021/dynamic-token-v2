# Dynamic Token v2.0
# Connected Reward Token for SocialFi Ecosystem

from genlayer import *

class DynamicToken(gl.Contract):
    balances: TreeMap[Address, u256]

    def __init__(self):
        pass

    @gl.public.write
    def mint(self, amount: u256) -> None:
        """Mint tokens as reward"""
        user = gl.message.sender_address
        current = self.balances.get(user, u256(0))
        self.balances[user] = current + amount

    @gl.public.write
    def transfer(self, to: Address, amount: u256) -> None:
        """Transfer tokens to another address"""
        user = gl.message.sender_address
        current = self.balances.get(user, u256(0))
        if current >= amount:
            self.balances[user] = current - amount
            self.balances[to] = self.balances.get(to, u256(0)) + amount

    @gl.public.view
    def my_balance(self) -> u256:
        """Get my token balance"""
        return self.balances.get(gl.message.sender_address, u256(0))
