/*

* Splice --> takes up to 3 arguments
    - index, elements to delete, elements to insert

* slice --> takes two argument copy array items
    - start, stop 

* spread operator --> used on arrays
    - 

    // For Objects
* 'Key' in object --> returns true or false

* for (ley key in object) {
    // do something
}

* Obejct.keys(name_of_object) --> returns an array of the objects keys



*/ 

let array = [1,2,3,4,5]
array.splice(2,0,1,1)
console.log(array)

const copyArr = array.slice(1,3)
console.log(copyArr)

// Spread to copy or combine 
let thisArray = [...array]
console.log(thisArray)

let thisArray2 = [10,9,...array,22,22]
console.log(thisArray2)