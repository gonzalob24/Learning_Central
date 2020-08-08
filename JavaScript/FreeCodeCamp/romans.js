function convertToRoman(num) {
    let num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    let romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

    let result = "";

    for (let i = 0; i < num_list.length; i++) {
        while (num_list[i] <= num) {
            result += romans[i];
            num -= num_list[i];
        }
    }

    return result;
}
console.log(convertToRoman(2));



