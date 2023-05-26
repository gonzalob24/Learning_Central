// importing module
// import a named export
// need to add .js for files
// import place to the same place in memory, they are not copies of the original
import {
  addToCart,
  totalPrice as price,
  totalQuantity as qty,
  cart,
} from './shoppingCart.js';
import * as ShoppingCart from './shoppingCart.js';
import defaultExport from './shoppingCart.js';

console.log('importing modules');
addToCart('bread', 10);
console.log(price, qty);
ShoppingCart.addToCart('cheese', 2);
defaultExport();
console.log(cart);

// can use top level await in modules
// no need to have an async await
// this however blocks entire execution of module
// this did not happen before
// console.log('start fetching');
// const res = await fetch('https://jsonplaceholder.typicode.com/posts');
// const data = await res.json();
// console.log(data);
// console.log('something');

const getLastPost = async function () {
  const res = await fetch('https://jsonplaceholder.typicode.com/posts');
  const data = await res.json();
  console.log(data);

  return { title: data.at(-1).title, text: data.at(-1).body };
};

const lastPost = getLastPost();

console.log(lastPost);
// I can access the post with then or use top level await
lastPost.then((last) => console.log(last));

// const lastPost2 = await getLastPost();
// console.log(lastPost2);

// module pattern
// closures and IIFE
const ShoppingCart2 = (function () {
  const cart = [];
  const shippingCost = 11;
  const totalPrice = 222;
  const totalQuantity = 33;
  const addToCart = function (prod, q) {
    cart.push({ prod, q });
    console.log(`${q} ${prod} added to cart`);
  };

  const orderStock = function (prod, q) {
    cart.push({ prod, q });
    console.log(`${q} ${prod} order from supplier`);
  };

  // what we want to expose
  return {
    addToCart,
    cart,
    totalPrice,
    totalQuantity,
  };
})();

ShoppingCart2.addToCart('apples', 4);
ShoppingCart2.addToCart('pizzas', 4);
console.log(ShoppingCart2.cart);

// node module system
// export
// export.addToCart = function (prod, q) {
//     cart.push({ prod, q });
//     console.log(`${q} ${prod} added to cart`);
//   };

//   // import
//   const {addToCart} = require('./shoppingCart.js')

// COMMAND LINES
/**
 * npm init --> use the defaults for now
 * package.json
 *  - stores all config files for project
 * - --save-dev: used for development not part of the codebase
 * node modules
 *  -
 */

// import cloneDeep from './node_modules/lodash-es/cloneDeep.js';
import cloneDeep from 'lodash-es'; // works like this because of parcel

const state = {
  cart: [
    { product: 'bread', quantity: 5 },
    { product: 'pizza', quantity: 5 },
  ],
  user: { loggedIn: true },
};

const stateClone = Object.assign({}, state);
const stateDeepClone = cloneDeep(state);
state.user.loggedIn = false; // change the original, and the cloned one also changes
console.log(stateClone);
console.log(stateDeepClone);

// Bundling with Parcel and NPM scripts
// similar to webpack -- used in react
/**
 * npx commands to run parcel
 * npx parcel index.js -- goal is to bundle js scripts together
 */

if (module.hot) {
  module.hot.accept();
}
