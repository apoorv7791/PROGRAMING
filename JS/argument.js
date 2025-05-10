class details {
    constructor(age) {
        this.age = age;
    }
    show() {
        console.log("age is :" + this.age);
    }
}
var a = new details(20)
a.show();