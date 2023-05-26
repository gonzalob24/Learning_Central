// Exporting modules
console.log('exporting modules');

// blocking code /////////////
// this will block the module that is importing named exports from this module
// console.log('Start fetching users');
// await fetch('https://jsonplaceholder.typicode.com/users');
// console.log('finish fetching users');
/////////////////

// all top level variables are private to this module
const shippingCost = 10;
export const cart = [];
// this is a named export
export const addToCart = function (prod, q) {
  cart.push({ prod, q });
  console.log(`${q} ${prod} added to cart`);
};
// in order to access these I will need to export them

// named exports multiple names at the same time
const totalPrice = 237;
const totalQuantity = 23;

// I can also rename them here totalQuantity as qty
export { totalPrice, totalQuantity };

// default exports
// used when I want to export one thing from a file
export default function () {
  console.log('add the logic that I want here in the default export');
}
