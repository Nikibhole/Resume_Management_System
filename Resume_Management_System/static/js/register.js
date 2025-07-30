let currentStep = 1;

function showStep(step) {
  document.querySelectorAll('.step').forEach((s, index) => {
    s.classList.add('d-none');
    s.classList.remove('fade-in');
    if (index === step - 1) {
      s.classList.remove('d-none');
      s.classList.add('fade-in');
    }
  });

  const progressBar = document.getElementById("form-progress");
  const percent = step * 33.33;
  progressBar.style.width = percent + "%";
  progressBar.innerText = `Step ${step} of 3`;
}

function nextStep() {
  const currentFields = document.querySelectorAll(`.step-${currentStep} input, .step-${currentStep} select`);
  for (let field of currentFields) {
    if (!field.checkValidity()) {
      field.reportValidity();
      return;
    }
  }

  if (currentStep < 3) {
    currentStep++;
    showStep(currentStep);
  }
}

function prevStep() {
  if (currentStep > 1) {
    currentStep--;
    showStep(currentStep);
  }
}

function previewFileName() {
  const file = document.getElementById("cv").files[0];
  const label = document.getElementById("file-name");
  if (file) {
    label.innerText = "Selected: " + file.name;
  } else {
    label.innerText = "";
  }
}

document.addEventListener("DOMContentLoaded", () => showStep(currentStep));
