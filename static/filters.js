myProducts = document.querySelectorAll('.product');

filters = new Set();
category_filters = new Set();
type_filters = new Set();

document.addEventListener('click', function(event) {
	const target = event.target;
	if (target.type !== 'checkbox') {
		return;
	}

	if (target.type === 'checkbox' && target.checked === true && target.classList.contains('brand-box')) {
		filters.add(target.value);
	} else if (target.type === 'checkbox' && target.checked === false && target.classList.contains('brand-box')) {
		filters.delete(target.value);
	} else if (target.type === 'checkbox' && target.checked === true && target.classList.contains('category-box')) {
		category_filters.add(target.value.toLowerCase());
	} else if (target.type === 'checkbox' && target.checked === false && target.classList.contains('category-box')) {
		category_filters.delete(target.value.toLowerCase());
	} else if (target.type === 'checkbox' && target.checked === true && target.classList.contains('type-box')) {
		type_filters.add(target.value);
	} else if (target.type === 'checkbox' && target.checked === false && target.classList.contains('type-box')) {
		type_filters.delete(target.value);
	}
	if (filters.size === 0 && category_filters.size === 0 && type_filters.size === 0) {
		for (let product of myProducts) {
			product.classList.remove('hidden');
		}
	} else if (filters.size > 0 && category_filters.size > 0 && type_filters.size > 0) {
		for (let product of myProducts) {
			if (
				filters.has(product.dataset.brand) &&
				category_filters.has(product.dataset.category) &&
				type_filters.has(product.dataset.type)
			) {
				product.classList.remove('hidden');
			} else {
				product.classList.add('hidden');
			}
		}
	} else if (filters.size > 0 && category_filters.size === 0 && type_filters.size === 0) {
		for (let product of myProducts) {
			if (filters.size === 0 && category_filters.size === 0 && type_filters.size === 0) {
				product.classList.remove('hidden');
			} else if (filters.has(product.dataset.brand) && filters.size > 0) {
				product.classList.remove('hidden');
			} else {
				product.classList.add('hidden');
			}
		}
	} else if (category_filters.size > 0 && filters.size === 0 && type_filters.size === 0) {
		for (let product of myProducts) {
			if (category_filters.has(product.dataset.category.toLowerCase())) {
				product.classList.remove('hidden');
			} else {
				product.classList.add('hidden');
			}
		}
	} else if (type_filters.size > 0 && filters.size === 0 && category_filters.size === 0) {
		for (let product of myProducts) {
			if (type_filters.has(product.dataset.type.toLowerCase())) {
				product.classList.remove('hidden');
			} else {
				product.classList.add('hidden');
			}
		}
	} else if (filters.size > 0 && category_filters.size > 0 && type_filters.size === 0) {
		for (let product of myProducts) {
			if (filters.has(product.dataset.brand) && category_filters.has(product.dataset.category.toLowerCase())) {
				product.classList.remove('hidden');
			} else {
				product.classList.add('hidden');
			}
		}
	} else if (filters.size > 0 && type_filters.size > 0 && category_filters.size === 0) {
		for (let product of myProducts) {
			if (filters.has(product.dataset.brand) && type_filters.has(product.dataset.type.toLowerCase())) {
				product.classList.remove('hidden');
			} else {
				product.classList.add('hidden');
			}
		}
	} else if (category_filters.size > 0 && type_filters.size > 0 && filters.size === 0) {
		for (let product of myProducts) {
			if (
				category_filters.has(product.dataset.category.toLowerCase()) &&
				type_filters.has(product.dataset.type.toLowerCase())
			) {
				product.classList.remove('hidden');
			} else {
				product.classList.add('hidden');
			}
		}
	}
});
