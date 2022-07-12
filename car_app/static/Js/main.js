console.log("work")

function edit_brand_name(brand_id) {
  const name = document.getElementById(brand_id + "_nameInput")
	axios.post( "/brands/" + brand_id + "/edit_name/", {brand_id: brand_id,
			new_name: name.value
		}).then((response) => {
    window.location.reload()
	})
}

// change name
function edit_brand_description(brand_id) {
  // Retrieve info from form first
  const descript = document.getElementById(brand_id + "_descriptionInput")
	axios({
		method: "post",
		url: "/brands/" + brand_id + "/edit_descript/",
		data: {
			brand_id: brand_id,
      // NOTE: .value is needed to get the input
			new_description: descript.value,
		},
	}).then(function (response) {
    window.location.reload()
	});
}