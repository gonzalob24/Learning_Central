function palindrome(str) {
    let pal1 = 0;
    let str_split = str.replace(/[\W_]/g, "").toLowerCase().split('');
    let str_len = str_split.length;
    console.log(str_split);
    // odd length
    if (str_len % 2 !== 0) {
        let odd_length = parseInt(str_len / 2);
        for (let i = 0; i < odd_length; i++) {
            if (str_split[i] !== str_split[str_len - 1 - i]) {
                return false;
            }
        }
    } else {
        // str_len is even
        let even_len = str_len / 2;
        for (let i = 0; i < even_len; i++) {
            if (str_split[i] !== str_split[str_len - 1 - i]) {
                return false;
            }
        }
    }
}

console.log((palindrome("almostomla")));
// let strr = ['e','y','e'];
// console.log(parseInt(3/2));

let palindrome2 = (str) => {
    let new_str = str.replace(/[\W_]/g, "").toLowerCase().split('');
    let new_str_rev = new_str.slice(0).reverse();
    return new_str.join('') === new_str_rev.join('');
}

// console.log(palindrome2("almostomla"));


// str = '*eeeheee';
// console.log(str[1].match(/[\W_]/))