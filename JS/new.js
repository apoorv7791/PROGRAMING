// how to use asynhronous function
// how to use await
// how to use try catch
function asyncFunction() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Async Hello World');
        }, 1000);
        reject('Error');
    });
}