
// This is private so I need to create functions to access elements
var budgetController = (function() {
    // var x = 23;
    // var add = function(a) {
    //     return x + a;
    // }
    // // returns an object called publicTest  
    // return {
    //     publicTest: function (b) {
    //         return add(b);
    //     }
    // }



})();

var uiController = (function () {


})();

// allows for the controllers to interact with each other
var controller = (function(budgetCtrl, uiCtrl) {
    // var z = budgetCtrl.publicTest(20);
    // return {
    //     publicTest2: function () {
    //         return z;
    //     }
    // }
    document.querySelector('.add__btn').addEventListener('click', function () {
        console.log('Button was clicked');
        })  
    
    
    document.querySelector('keypress', function (event) {
        console.log(event);
    });

})(budgetController, uiController);














