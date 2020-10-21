/* Great for storing and looking up items * 
* Obejcts -- similar to python dictionaries
    - access with dot notation
    - or key name obj["name"]

    - delete obj_name["key"]

    - Testing for poperties
    - obj_name.hasOwnProperty("key")

* Math.random()
    - (0,1) non inclusive

* parseInt(num_str, radix)

* Conditional ternary operator
    - conditon ? expression-if-true : expression-if-false

*/


// Objects

var obj1 = {
    key: "value",
    key2: "value2"
}

console.log(obj1)
console.log(obj1['key'])

// change value of items
obj1["key"] = "changed Value";
console.log(obj1)
console.log(obj1["key"])
console.log(obj1.hasOwnProperty("key"))

delete obj1.key
console.log(obj1)

console.log(Math.round(Math.random() * 5) + 1)
console.log(Math.floor(Math.random() * 2) + 1)

var min = 1;
var max = 6;

console.log(Math.floor(Math.random() * (max - min + 1)) + min)

console.log(parseInt("007"))