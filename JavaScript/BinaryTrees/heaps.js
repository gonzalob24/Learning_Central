class MaxHeap {
	constructor() {
		this.arr = [];
	}

	// check if its empty
	isEmpty() {
		return this.arr.length === 0;
	}

	insert(data) {
		if (this.isEmpty()) {
			this.arr.push(data);
		} else {
			this.arr.push(data);
			var index = this.arr.length - 1;
			var insertedValue = this.arr[index];
			while (index > 0) {
				var parentIndex = Math.floor((index - 1) / 2);
				if (insertedValue <= this.arr[parentIndex]) {
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

	deleteMax() {
		[this.arr[0], this.arr[this.arr.length - 1]] = [
			this.arr[this.arr.length - 1],
			this.arr[0],
		];
		// remove last element
		const element = this.arr[0];
		const length = this.arr.length;
		const maxValue = this.arr.pop();

		let parentIndex = 0;

		while (true) {
			let lchildIndex = parentIndex * 2 + 1;
			let rchildIndex = parentIndex * 2 + 2;
			let leftChild, rightChild;
			let swap = null;

			if (lchildIndex < length) {
				leftChild = this.arr[lchildIndex];
				if (leftChild > element) {
					swap = lchildIndex;
				}
			}
			if (rchildIndex < length) {
				rightChild = this.arr[rchildIndex];
				if (
					(swap === null && rightChild > element) ||
					(swap !== null && rightChild > leftChild)
				) {
					swap = rchildIndex;
				}
			}
			if (swap == null) break;

			this.arr[parentIndex] = this.arr[swap];
			this.arr[swap] = element;

			parentIndex = swap;
		}

		return maxValue;
	}
}

const maxHeap = new MaxHeap();
maxHeap.insert(41);
maxHeap.insert(39);
maxHeap.insert(33);
maxHeap.insert(18);
maxHeap.insert(27);
maxHeap.insert(12);
maxHeap.insert(55);
console.log(maxHeap);
// const maxVal = maxHeap.deleteMax();
