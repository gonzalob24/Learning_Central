'use strict';

/////////////////////////////////////////////////
/////////////////////////////////////////////////
// BANKIST APP

// Data from a web API ()
const account1 = {
  owner: 'Jonas Schmedtmann',
  movements: [200, 450, -400, 3000, -650, -130, 70, 1300],
  interestRate: 1.2, // %
  pin: 1111,
};

const account2 = {
  owner: 'Jessica Davis',
  movements: [5000, 3400, -150, -790, -3210, -1000, 8500, -30],
  interestRate: 1.5,
  pin: 2222,
};

const account3 = {
  owner: 'Steven Thomas Williams',
  movements: [200, -200, 340, -300, -20, 50, 400, -460],
  interestRate: 0.7,
  pin: 3333,
};

const account4 = {
  owner: 'Sarah Smith',
  movements: [430, 1000, 700, 50, 90],
  interestRate: 1,
  pin: 4444,
};

const accounts = [account1, account2, account3, account4];

// Elements
const labelWelcome = document.querySelector('.welcome');
const labelDate = document.querySelector('.date');
const labelBalance = document.querySelector('.balance__value');
const labelSumIn = document.querySelector('.summary__value--in');
const labelSumOut = document.querySelector('.summary__value--out');
const labelSumInterest = document.querySelector('.summary__value--interest');
const labelTimer = document.querySelector('.timer');

const containerApp = document.querySelector('.app');
const containerMovements = document.querySelector('.movements');

const btnLogin = document.querySelector('.login__btn');
const btnTransfer = document.querySelector('.form__btn--transfer');
const btnLoan = document.querySelector('.form__btn--loan');
const btnClose = document.querySelector('.form__btn--close');
const btnSort = document.querySelector('.btn--sort');

const inputLoginUsername = document.querySelector('.login__input--user');
const inputLoginPin = document.querySelector('.login__input--pin');
const inputTransferTo = document.querySelector('.form__input--to');
const inputTransferAmount = document.querySelector('.form__input--amount');
const inputLoanAmount = document.querySelector('.form__input--loan-amount');
const inputCloseUsername = document.querySelector('.form__input--user');
const inputClosePin = document.querySelector('.form__input--pin');

const displayMovements = function (movements) {
  containerMovements.innerHTML = '';

  movements.forEach((move, i) => {
    const type = move > 0 ? 'deposit' : 'withdrawal';
    const html = `<div class="movements__row">
        <div class="movements__type movements__type--${type}">${
      i + 1
    } ${type}</div>
        <div class="movements__value">${move}</div>
      </div>`;

    containerMovements.insertAdjacentHTML('afterbegin', html);
  });
};

displayMovements(account1.movements);

const calcDisplaySummary = function (movements) {
  const incomes = movements
    .filter((mov) => mov > 0)
    .reduce((acc, mov) => acc + mov, 0);

  labelSumIn.textContent = `${incomes}`;

  const out = movements
    .filter((mov) => mov < 0)
    .reduce((acc, mov) => acc + mov, 0);
  labelSumOut.textContent = `${Math.abs(out)}`;

  const interest = movements
    .filter((mov) => mov > 0)
    .map((deposit) => (deposit * 1.2) / 100)
    .filter((int, i, arr) => {
      console.log(arr);
      return int >= 1;
    })
    .reduce((acc, int) => acc + int, 0);
  labelSumInterest.textContent = `${interest}`;
};

calcDisplaySummary(account1.movements);

const createUserName = (accs) => {
  accs.forEach(function (acc) {
    acc.userName = acc.owner
      .toLowerCase()
      .split(' ')
      .map((name) => name[0])
      .join('');
  });
};

const user = 'Steven Thomas Williams'; // stw
createUserName(accounts);
console.log(accounts);

let currentAccount;

btnLogin.addEventListener('click', function (e) {
  e.preventDefault(); // prevents form from sumbimtting
  currentAccount = accounts.find(
    (acc) => acc.userName === inputLoginUsername.value
  );
  console.log(currentAccount);

  if (currentAccount.pin == Number(inputLoginPin.value)) {
    console.log('Logged in');
  }
});

const deposits = account1.movements.map(function (mov) {
  console.log(mov);
});

// does not return an array only the first instance in which condition is true

const firstWithdrawal = account1.movements.find((mov) => mov < 0);

console.log(account1.movements);
console.log(firstWithdrawal);

const account = accounts.find((acc) => acc.owner === 'Jessica Davis');
console.log(account);

/*
const euroToUSD = 1.1;
console.log('----------Total-------------------');
const totalDeposits = account1.movements
  .filter((mov) => mov > 0)
  .map((mov) => mov * euroToUSD)
  .reduce((acc, mov) => acc + mov, 0);

console.log(totalDeposits);
// const initials = userName.map((name) => {

//   return name[0]
// })



// MAP returns a new array
const euroToUSD = 1.1;
const movementsUSD = account1.movements.map(function(mov) {
  return mov * euroToUSD;
})

console.log(account1.movements);
console.log(movementsUSD);

const movementsDesctiption = account1.movements.map((movement, i, arr) => 
  // if (movement > 0) {}
  //   console.log(`Movement ${i+1}: You deposited ${movement}`);
  // } else {
  //   console.log(`Movement ${i + 1}, You withdrew ${Math.abs(movement)}`);
  // }
  `Movement ${i + 1}: You ${movement > 0 ? 'deposited' : 'withdrew'} ${Math.abs(movement)}`
)
console.log(movementsDesctiption);


/////////////////////////////////////////////////
/////////////////////////////////////////////////
// LECTURES

const currencies = new Map([
  ['USD', 'United States dollar'],
  ['EUR', 'Euro'],
  ['GBP', 'Pound sterling'],
]);

const movements = [200, 450, -400, 3000, -650, -130, 70, 1300];

/////////////////////////////////////////////////

let arr = ['a','b', 'c','d','e'];

// SLICE extract parts of the aray
console.log(arr.slice(2)) // returns a new array
console.log(arr.slice(2, 4)) // end is not inclusive
console.log(arr.slice(-2));
console.log(arr.slice(1, -2));

// create shallow copy --> both of these do the same thing
console.log(arr.slice());
console.log([...arr]);

// SPLICE --> this can can mutate the array
// console.log(arr.splice(2)); // splice deleted items from original array
console.log(arr.splice(-1));
console.log(arr);
console.log(arr.splice(1,2));
console.log(arr);  

arr = ['a','b', 'c','d','e'];
const arr2 = ['j', 'i', 'h', 'g', 'f']

console.log(arr2.reverse()); //  mutates the original array
console.log(arr2);

// concat --> concatenate two arrays, both ways are the same
const letters = arr.concat(arr2)
console.log(letters);
console.log([...arr, ...arr2]);

// JOIN
console.log(letters.join(' - '));


// for of

for(const [i, movement] of movements.entries()) {
  if (movement > 0) {
    console.log(`Movement ${i+1}: You deposited ${movement}`);
  } else {
    console.log(`Movement ${i + 1}, You withdrew ${Math.abs(movement)}`);
  }
}

console.log('--------------------------forEach-------------------');
// loops over array and has access to current element, index, entire array
// Continue and breaks wont work here.
movements.forEach(function(movement, index, array) {
  if (movement > 0) {
    console.log(`Movement ${index+1}: You deposited ${movement}`);
  } else {
    console.log(`Movement ${index+1}: You withdrew ${Math.abs(movement)}`);
  }
});

console.log('--------------------------MAPS-------------------');

// forEach with maps
currencies.forEach(function(value, key, map) {
  console.log(`${key}: ${value}`);
})


console.log('--------------------------SETS-------------------');
const currenciesunique = new Set(['USD', 'GBP', 'USD', 'EUR', 'EUR'])
console.log(currenciesunique);
currenciesunique.forEach(function(value, _, map) {
  console.log(`${value}: ${value}`);
})


*/
