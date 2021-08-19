"use strict"
var statusMenu = 1;

/*function MenuButton(){
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
*/
function MenuButton(){
	var element = document.getElementsByClassName("item-text");
	var menu = document.getElementById("Menu");

	if (statusMenu == 1)
		CloseMenu(element, menu);
	else
		OpenMenu(element, menu);
}

function CloseMenu(element, menu)
{
	addArrayProperty(element, 
		`left: 0px;
		opacity: 0;
		transition: opacity .25s, left .5s; 
		`);
	addProperty(menu,
		`width: 70px;
		transition: .5s;`);
	statusMenu = 0;
}

function OpenMenu(element, menu){
	addProperty(menu,
		`width: 300px;
		transition: .3s;`);
	addArrayProperty(element, 
		`left: 80px;
		opacity: 1;
		transition: opacity .75s, left .5s; `);
	statusMenu = 1;
}