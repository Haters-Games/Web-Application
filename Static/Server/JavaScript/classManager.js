/*function hasClass(element, cls) {
	return element.classList.contains(cls)
}

function addClass(element, cls) {
	if (!hasClass(element, cls)) 
		element.classList.add(cls);
}

function addArrayClass(element, cls){
	for(var i = 0; i < element.length; i++){
		addClass(element[i],cls)
	}
}

function removeClass(element, cls) {
	if (hasClass(element, cls)) 
		element.classList.remove(cls);
}

function removeArrayClass(element, cls){
	for(var i = 0; i < element.length; i++){
		removeClass(element[i],cls)
	}
}*/

function addArrayProperty(element, Property) {
	for(var i = 0; i < element.length; i++){
		element[i].style.cssText = Property;
	}
}

function addProperty(element, Property) {
	element.style.cssText = Property;
}