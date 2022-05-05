const buf = new Buffer.alloc(10, "gonzalo", "base64");
// console.log(buf[0]);
// buf.forEach((el) => {
// 	console.log(el);
// });

console.log(buf.slice(0, 4));
console.log("the stuff in buf", buf.toString("base64"));

const item1 = {
    name: "gonzalo",
    age: 22,
    address: {
        add1: { on1: "1939 Jonathan" },
        zip: 77521,
    },
};

// copying
const item2 = Object.assign({}, item1);

console.log(item1);
console.log(item2);

item1.age = 30;
console.log("new item1 ", item1);
console.log("new item2 ", item2);

item2.address.add1.on1 = "new addresss";

// item one also changes, here we need to do a deep copy
console.log("Last item1", item1);
console.log("Last item2", item2);

// deep cloning: clone this way always:
const item3 = {
    name: "Jones",
    age: 22,
    address: {
        add1: { on1: "1939 Jonathan" },
        zip: 77521,
    },
};
const item4 = JSON.parse(JSON.stringify(item3));
console.log(item3);
console.log(item4);

item4.address.add1.on1 = "Last change";
console.log("item3: ", item3);
console.log("item4: ", item4);
