// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {

    // Mapping to store the balance of each customer (address)
    mapping(address => uint256) private balances;

    // Event to log deposits
    event Deposit(address indexed accountHolder, uint256 amount);

    // Event to log withdrawals
    event Withdraw(address indexed accountHolder, uint256 amount);

    // Deposit money into the customer's account
    function deposit()public payable {
        require(msg.value > 0, "You must send some Ether to deposit.");  // Ensure Ether is sent
        balances[msg.sender] += msg.value;  // Add deposited amount to the sender's balance
        emit Deposit(msg.sender, msg.value);  // Log the deposit event
    }

    // Withdraw money from the customer's account
    function withdraw(uint256 amount) public {
        require(amount > 0, "Withdrawal amount must be greater than zero.");
        require(amount <= balances[msg.sender], "Insufficient balance.");

        // Transfer the specified amount to the sender
        payable(msg.sender).transfer(amount);

        // Deduct withdrawn amount from sender's balance
        balances[msg.sender] -= amount;

        // Log the withdrawal event
        emit Withdraw(msg.sender, amount);
    }

    // Check the balance of the customer
    function checkBalance() public view returns (uint256) {
        return balances[msg.sender];  // Return the balance of the sender
    }
}