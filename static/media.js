function myFunction(x) {
	if (x.matches) {
		// If media query matches
		document.querySelector('#section-filter').classList.add('hidden');
	} else {
		document.querySelector('#section-filter').classList.remove('hidden');
	}
}

var x = window.matchMedia('(max-width: 800px)');
myFunction(x); // Call listener function at run time
x.addListener(myFunction); // Attach listener function on state changes
