# Data Structure

- Systematic way of organizing and accessing data

# Algorithm

- step by step procedure for performing some task in a finite amount of time
- what can affect the running time of algorithm?
  - input size
  - hardware: processor, clock rate,
  - OS
- Goal: characterize algorithms running time as a function of input size
- I can use a time function to track start and stop of algorithm
- better I can keep track of clock cycles
- timeit python module
- limitations of experimental analysis:
  - limited to same hardware and software specs
  - time will vary depending on machine
  - for fast algorithms speed measurements may bot be precise enough
  -
- what does better mean?
  - Faster
  - less memory intensive
  - more readable

# Big O

- allows us to evaluate the algo independent of hardware and software environments
- does not require implementation of algorithm --> only a high level understanding
- takes into account all possible inputs
- Big O way of comparing code and its performance to other pieces of code
- this gives a numeric representation of how code may perform
- Useful in discussing trade-offs between different approaches
- When code slows down and crashes, identify parts of the code that inefficient can help us find pin points in our application
- we can count number of simple operations
  - \*, +, -, /
  - numbers will be constant time

## Constant time

- Primitive operations

## Asymptotic Analysis

- focus on the growth rate of the running time as a function of the input size n
- regardless of the exact number, the number of operations grows roughly with n
- formal way to keep track of number of operations
- we don't care about the details, only the trends

- talking about the worst case scenario, the upper bound
- An algorithm is O(f(n)) if the number of simple operations the computer has do is eventually less than a constant times f(n), as n increases
- f(n) could be linear (f(n) = n)
- f(n) could be quadratic (f(n) = n )
- f(n) could be constant (f(n) = 1)
- f(n) could be something entirely different!

- for loops are O(n)
- nested for loops could be O(n^2)

- space complexity

  - how much additional memory do we need to allocate in order to run the code in our algorithm?
  - Sometimes you'll hear the term auxiliary space complexity to refer to space required by the algorithm, not including space taken up by the inputs.
  - Most primitives (booleans, numbers, undefined, null) are constant space
  - Strings require O(n) space (where n is the string length)
  - Reference types are generally O( n), where n is the length (for arrays) or the number of keys (for objects)

  - LOGS
    - log2(value) = exponent ----> 2^exponent = value
    - some search, sort, recursion algorithms have log time complexity

  ### RULES

  - Constants Don't matter
  - Smaller terms don't matter
  - Arithmetic operations are constant
  - Variable assignment is constant
  - Accessing elements in an array (by index) or object (by key) is constant
  - In a loop, the the complexity is the length of the loop times the complexity of whatever happens inside of the loop

# Objects

1. when to use objects

   - When you don't need order
   - When you need fast access / insertion and removal

2. Object.keys - O(N)
3. Object.values - O(N)
4. Object.entries - O(N)
5. hasOwnProperty - O(1)

# Arrays

- When you need order
- When you need fast access / insertion and removal (sort of....)
- push - O(1)
- pop - O(1)
- shift - O(N) - removes from the front
- unshift - O(N) - add to the front
- concat - O(N)
- slice - O(N)
- splice - O(N)
- sort - O(N \* log N)
- forEach/map/filter/reduce/etc. - O(N)

# Problem Solving Patterns

An algorithm: a series of steps to accomplish a task

### Improve Solving Problems

- Devise a plan for solving problems
- Master common problem solving patterns
- Understand the Problem
- Explore Concrete Examples
- Break It Down - what category of problems is it?
- Solve/Simplify
- Look Back and Refactor

#### Understand The Problem

1. Can I restate the problem in my own words?
2. What are the inputs that go into the problem?
3. What are the outputs that should come from the solution to the problem?
4. Can the outputs be determined from the inputs? In other words, do I have enough information to solve the problem? (You may not be able to answer this question until you set about solving the problem. That's okay; it's still worth considering the question at this early stage.)
5. How should I label the important pieces of data that are a part of the problem? -> What are the things that matter for the problem, Think if names for important pieces

`Example: Write a function which takes two numbers and returns their sum.`

    1. Restate the problem: I will be adding two numbers
        - adding two numbers
    2. What are the inputs that go into the problem?
        - are they strings, integers. Are the inputs always two?
    3. What are the inputs that should come from the solution to the problem?
        - should it be an integer, float, string..?
    4. Can the outputs be determined from the inputs?
        - Do we have enough information to solve the problem?
    5. How should I label the important pieces?
        -

#### Come up with examples to the problem. This provides a sanity check

1. Start with simple examples
2. Progress to more complicated examples
3. Explore examples with empty inputs
4. Explore examples with invalid inputs

#### Break It Down

1. Explicitly write out the steps you need to take.
   `This forces you to think about the code you'll write before you write it, and helps you catch any lingering conceptual issues or misunderstandings before you dive in and have to worry about details (e.g. language syntax) as well.`
2. Find the core difficulty in what you're trying to do
3. Temporarily ignore that difficulty
4. Write a simplified solution
5. Then incorporate that difficulty back in
6. Look back and refactor
   - Can you check the result?
   - Can you derive the result differently?
   - Can you understand it at a glance?
   - Can you use the result or method for some other problem?
   - Can you improve the performance of your solution?
   - Can you think of other ways to refactor?
   - How have other people solved this problem?

# PATTERNS

## Frequency

- This pattern uses objects or sets to collect values/frequencies of values
- This can often avoid the need for nested loops or O(N^2) operations with arrays / strings
  `Example: Write a function called same, which accepts two arrays. The function should return true if every value in the array has it's corresponding value squared in the second array. The frequency of values must be the same.`

      same([1,2,3], [4,1,9]) // true
      same([1,2,3], [1,9]) // false
      same([1,2,1], [4,4,1]) // false (must be same frequency)

## Multiple Pointers

- Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition

- Very efficient for solving problems with minimal space complexity as well