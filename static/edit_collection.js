document.querySelector('.editBtn').addEventListener('click', function(event) {
	event.preventDefault();
	let removeButtons = document.querySelectorAll('.removeBtn');
	for (let button of removeButtons) {
		button.classList.toggle('hidden');
	}
});

document.addEventListener('click', async function(event) {
	const target = event.target;

	if (target.tagName === 'BUTTON' && target.classList.contains('removeBtn')) {
		event.preventDefault();
		const productID = target.dataset.id;
		response = await axios.post(`/remove/${productID}`);
		updateCollectionDOM(productID);
	}
});

function updateCollectionDOM(productID) {
	document.querySelector(`#product-${CSS.escape(productID)}`).remove();
}
