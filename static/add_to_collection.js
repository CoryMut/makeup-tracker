document.addEventListener('click', async function(event) {
	const target = event.target;

	if (target.tagName === 'BUTTON' && target.classList.contains('addBtn')) {
		event.preventDefault();
		const productID = target.dataset.id;
		const response = await axios.post(`/add/${productID}`);

		updateCollectionDOM(target);
	}
});

function updateCollectionDOM(target) {
	target.classList.remove('btn-primary');
	target.classList.add('btn-green');
	target.innerHTML = '<i class="fas fa-check text-light"></i>';
	target.disabled = true;
}
