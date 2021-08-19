async function write()
{
	document.open();
	await document.write(`\
	<tr>
		<th>{{ Report.production_department.label_tag }}</th>
		<th>{{ Report.production_department }}</th>
	</tr>`);
	document.close();
}