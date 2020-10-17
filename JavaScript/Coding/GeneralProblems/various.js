function anagram(str1, str2) {
    // check if lengths are not equal
    if (str1.length !== str2.length) {
        return false;
    }

    const result = {}
    // loop through the first string and get frequency of each letter
    for (let i=0; i<str1.length; i++) {
        //console.log(str1[char]);
        let letter = str1[i];
        result[letter] ? result[letter] += 1 : result[letter] = 1;

        // if (!result[letter]) {
        //     result[letter] = 1;
        // } else {
        //     result[letter] += 1;
        // }    
    }

    for(let i=0; i<str2.length; i++) {
        let letter = str2[i];
        if(!result[letter]) {
            return false;
        } else {
            result[letter] -=1;
        }
    }

    return true;
}

// console.log(anagram("hello", "lloeh"))

function sumZeroNaive(sortedArray) {
    // have a pointer to index1
    let index1 = 0;
    // have a pointer to index2 = index1 + 1
    let index2 = 1;
    // keep track sum
    var sumIndex;
    // pairs that sum to zero
    const sumZeroPairs = [];

    for (let i=0; i<sortedArray.length; i++){
        index1 = sortedArray[i];
        for (let j=i+1; j<sortedArray.length; j++) {
            index2 = sortedArray[j];
            // calc. sum of index1 + index2 if sum=0 break
            sumIndex = index1 + index2;
            if(sumIndex === 0) {
                sumZeroPairs.push(index1);
                sumZeroPairs.push(index2);
                return sumZeroPairs;
            }
        }
    }
    // return pair
    return undefined;
}

function sumZeroOptimized(sortedArray) {
    // have a pointer to index1
    let i = 0;
    // have a pointer to index2 = index1 + 1
    let j = sortedArray.length - 1;
    // keep track sum
    var sumIndex;
    // pairs that sum to zero
    const sumZeroPairs = [];

    while (i < j) {
        sumIndex = sortedArray[i] + sortedArray[j];
        if(sumIndex === 0) {
            sumZeroPairs.push(sortedArray[i]);
            sumZeroPairs.push(sortedArray[j]);
            return sumZeroPairs;
        } else if (sumIndex > 0) {
            j--;
        } else { // sumIndex < 0
            i++;
        }
    }
    // return pair
    return undefined;
}



// console.log(sumZeroNaive([-3,-2,-1,0,1]));
// console.log(sumZeroNaive([-3,-2,-1,0,10]));

// console.log(sumZeroOptimized([-3,-2,-1,0,1]));
// console.log(sumZeroOptimized([-3,-2,-1,0,10]));


function countUniqueValues(sortedArray) {
    // store values that are unique
    // const uniqueVals = {}
    const uniqueVals = [];
    // keep track of unique values
    // var count = 0;
    // loop sortedArray
    for(let i=0; i<sortedArray.length; i++) {
        var item = sortedArray[i];
        if(!(uniqueVals.includes(item))) {
            uniqueVals.push(item);
            // count++;
        }
    }
    // return Object.keys(uniqueVals).length;
    // return `${uniqueVals.length}, [${uniqueVals}]`
}
console.log(countUniqueValues([1,1,1,1,1,1,2]))