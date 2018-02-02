// Additional validation for subject and datetime

document.getElementById("button").addEventListener('click', function() {
  var subject = document.getElementById("subject");
  var inmail = document.getElementById("inmail");
  var datetime = document.getElementById("datetime");

  if (inmail.checked && !subject.value) {
    subject.setCustomValidity("Please add a subject for your InMail");
  } else {
    subject.setCustomValidity("");
  }

  if (datetime.value && moment(datetime.value) < moment()) {
    datetime.setCustomValidity("Please set a valid date and time");
  } else {
    datetime.setCustomValidity("");
  }
});
