function fibonacci(n) {
  // first two numbers ar 0 and 1
  var first = 0;
  var second = 1;

  if (n < 1) {
    return "n can't be less than 1";
  } else if (n === 1 || n === 2) {
    return n - 1;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

function canConstruct(target, wordBank) {
  if (target == "") {
    return true;
  }
  for (let word of wordBank)
    if (target.indexOf(word) == 0) {
      suffix = target.slice(word.length);
      if (canConstruct(suffix, wordBank) == true) {
        return true;
      }
    }

  return false;
}
// 0 1 1 2 3
// console.log(fibonacci(5))
// console.log(fibonacci(10))
console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
