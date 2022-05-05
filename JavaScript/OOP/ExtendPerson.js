const Employee = require("./Person");

class Janitor extends Employee {
    constructor(salary, jobType, empName) {
        super(salary, jobType);
        this.empName = empName;
    }

    introduce() {
        console.log(`My name is ${this.empName} I work as a ${this.jobType}.`)
    }
}

const gonzalo = new Janitor(40000, "Cook", "Gonzalo");
// add to the prototype
Janitor.prototype.likeJob = function () {
    console.log(`I love being a ${this.jobType}`);
}
gonzalo.introduce();

gonzalo.likeJob();