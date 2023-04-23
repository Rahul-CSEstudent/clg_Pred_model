const form = document.getElementById('myForm');
form.addEventListener('submit', function(event) {
  event.preventDefault(); // prevent the form from submitting

  // Get the form data
  const formData = new FormData(event.target);

    // Get a reference to the <div> element where we want to add the data
    const dataDiv = document.getElementById('data');

        const dataElement = document.createElement('p');
        //displa
        dataDiv.innerHTML = `<h2>The top 3 preffered college for you is NIT trichy 89%, VIT chennai 88% and BITS bilani 85%</h2>`;
        dataDiv.appendChild(dataElement);
});

