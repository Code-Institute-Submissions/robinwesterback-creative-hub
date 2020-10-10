function sendMail(contactForm) {
    emailjs.send("gmail", "Creative Hub", {
        "name": contactForm.name.value,
        "company": contactForm.company.value,
        "from_email": contactForm.emailaddress.value,
        "phone": contactForm.phone.value,
        "description": contactForm.description.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}