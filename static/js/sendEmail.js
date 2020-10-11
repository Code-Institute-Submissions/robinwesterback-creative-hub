function sendMail(contactForm) {
  var emailMessage = document.getElementById("email-message");

  emailjs
    .send("gmail", "Creative Hub", {
      name: contactForm.name.value,
      company_name: contactForm.company_name.value,
      email: contactForm.email.value,
      phone: contactForm.phone.value,
      description: contactForm.description.value,
    })
    .then(
      function (response) {
        console.log("SUCCESS", response);
        document.getElementById("email-message").innerHTML = "E-mail successfully sent!";
      },
      function (error) {
        console.log("FAILED", error);
        document.getElementById("email-message").innerHTML = "E-mail failed to send!";
        emailMessage.className(input-error-message);
      }
    );
  return false; // To block from loading a new page
}
