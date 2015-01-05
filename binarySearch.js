var binarySearch = function(pool, num) {
	var min = 1;
	var max = pool;
	var tries = 1;
	while (guess != num) {
		var guess = Math.floor((min + max) / 2);
		tries++;
		if (guess === num) {
			console.log("You guessed my number, " + guess + ", in " + tries + " tries!");
			break;
		}
		else if (guess > num) {
			console.log('Your guess ' + guess + ' is too high.');
			max = guess - 1;
		} else {
			console.log('Your guess ' + guess + ' is too low.');
			min = guess + 1;
		}
	
	}
};

if (require.main === module) {
    binarySearch(120, 34);
}