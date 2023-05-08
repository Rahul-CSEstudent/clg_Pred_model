const form = document.getElementById('myForm');
form.addEventListener('submit', function(event) {
  event.preventDefault(); // prevent the form from submitting

  // Get the form data
  const formData = new FormData(event.target);

    // Get a reference to the <div> element where we want to add the data
    const dataDiv = document.getElementById('data');

        const dataElement = document.createElement('p');
        const val = Math.random();
        //displa
        dataDiv.innerHTML = `<h2>The chance of getting into that college is ${val}</h2>`;
        dataDiv.appendChild(dataElement);
});

