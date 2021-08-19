"use strict"
var statusMenu = "open";

function MenuButton(){
	var element = document.getElementsByClassName("item-text");
	var menu = document.getElementById("Menu");

	if (statusMenu == "open" || statusMenu == "process")
		CloseMenu(element, menu);
	else if (statusMenu == "close")
		OpenMenu(element, menu);
}

function CloseMenu(element, menu)
{
	addArrayProperty(element, 
		`position: fixed; 
		transition: .25s; 
		opacity: 0;`);
	addProperty(menu,
		`width: 70px;
		transition: .5s;`);
	statusMenu = "close";
}

function OpenMenu(element, menu){
	addArrayProperty(element, 
		`position: fixed; 
		transition: .5s; 
		opacity: 1;`);
	addProperty(menu,
		`width: 25vw;
		transition: .5s;`);
	statusMenu = "process";
	setTimeout(() => {
		if(statusMenu == "process"){
			addArrayProperty(element, `position: static; `);
			statusMenu = "open";
		}}, 
		500);
}