class Node {
  constructor(value, priority) {
    this.info = value;
    this.priority = priority;
  }
}

class PriorityQueue {
  constructor() {
    this.arr = [];
  }
  // use linear O(n) to insert based on priority
  insert_On() {}

  isEmpty() {
    return this.arr.length === 0;
  }
  // O(log n)
  enqueue(data, priority) {
    let newNode = new Node(data, priority);
    if (this.isEmpty()) {
      this.arr.push(newNode);
    } else {
      this.arr.push(newNode);
      var index = this.arr.length - 1;
      var insertedValue = this.arr[index];
      while (index > 0) {
        var parentIndex = Math.floor((index - 1) / 2);
        if (insertedValue.priority >= this.arr[parentIndex].priority) {
          break;
        }
        [this.arr[parentIndex], this.arr[index]] = [
          this.arr[index],
          this.arr[parentIndex],
        ];

        index = parentIndex;
      }
    }
  }

  dequeue() {
    [this.arr[0], this.arr[this.arr.length - 1]] = [
      this.arr[this.arr.length - 1],
      this.arr[0],
    ];
    // remove last element
    const element = this.arr[0];
    const length = this.arr.length;
    const minValue = this.arr.pop();

    let parentIndex = 0;

    while (true) {
      let lchildIndex = parentIndex * 2 + 1;
      let rchildIndex = parentIndex * 2 + 2;
      let leftChild, rightChild;
      let swap = null;

      if (lchildIndex < length) {
        leftChild = this.arr[lchildIndex];
        if (leftChild.priority < element.priority) {
          swap = lchildIndex;
        }
      }
      if (rchildIndex < length) {
        rightChild = this.arr[rchildIndex];
        if (
          (swap == null && rightChild.priority < element.priority) ||
          (swap !== null && rightChild.priority < leftChild.priority)
        ) {
          swap = rchildIndex;
        }
      }
      if (swap == null) break;

      [this.arr[parentIndex], this.arr[swap]] = [
        this.arr[swap],
        this.arr[parentIndex],
      ];
      parentIndex = swap;
    }

    return minValue;
  }
}

let Er = new PriorityQueue();

Er.enqueue("Cold", 5);
Er.enqueue("Gun shot", 1);
Er.enqueue("Fever", 4);
Er.enqueue("Borken Arm", 2);
Er.enqueue("Bail in foot", 3);
