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
    return `${uniqueVals.length}, [${uniqueVals}]`
}

function countUniqueValues2(sortedArray) {
    if(sortedArray.length === 0) return 0
    // pointer 1 
    var i = 0;
    // pounter 2
    // var j = 1;
    // loop array and update pointer2 if its unique
    for(var j=1; j<sortedArray.length; j++){
        var item1 = sortedArray[i];
        var item2 = sortedArray[j];
        if (item1 !== item2) {
            i++;
            sortedArray[i] = sortedArray[j]
        }
    }
    return i + 1
}

// console.log(countUniqueValues2([1,1,1,1,1,1,2]))

// naive solution: get subarray up to n and get sum O(n^2)
function maxSubarraySum(numArray, n) {
    // 
    // loop the array to find max sum array
    var maxSum = -Infinity;
    for(var i=0; i<numArray.length - n + 1; i++) {
        var tempSum = 0;
        for(var j=0; j<n; j++) {
            tempSum += numArray[i + j]
        }
        if(tempSum > maxSum) {
            maxSum = tempSum;
        }
    }
    // retrun max sum
    return maxSum;
}

// O(n) time a much faster solution
function maxSubarraySumOptimized(numArray, n) {
    var maxSum = 0;
    var tempSum = 0;
    // loop once up to n to get sub sum
    for(var i=0; i<n; i++) {
        maxSum += numArray[i];
    }
    tempSum = maxSum;
    
    // loop entire array with sliding window. subtract first item and add next item in array
    for(var i=n; i<numArray.length; i++) {
        tempSum = tempSum - numArray[i - n] + numArray[i];
        maxSum = Math.max(tempSum, maxSum);
    }    // return max sum
    return maxSum;

}

console.log(maxSubarraySum([2,6,9,2,1,8,5,6,3],3))
console.log(maxSubarraySumOptimized([2,6,9,2,1,8,5,6,3],3))