document.addEventListener("DOMContentLoaded", () => {
  const resumeInput = document.getElementById("resume");
  const fileError = document.getElementById("file-error");
  const fileName = document.getElementById("file-name");
  const pdfPreviewBox = document.getElementById("preview-box");
  const pdfPreview = document.getElementById("pdf-preview");

  resumeInput.addEventListener("change", () => {
    fileError.textContent = "";
    fileName.textContent = "";
    pdfPreviewBox.style.display = "none";

    const file = resumeInput.files[0];

    if (!file) return;

    const allowedTypes = ["application/pdf", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"];
    const maxSize = 2 * 1024 * 1024; // 2MB

    if (!allowedTypes.includes(file.type)) {
      fileError.textContent = "Invalid file type. Please upload PDF, DOC, or DOCX.";
      resumeInput.value = "";
      return;
    }

    if (file.size > maxSize) {
      fileError.textContent = "File size exceeds 2MB. Please upload a smaller file.";
      resumeInput.value = "";
      return;
    }

    fileName.textContent = "Selected: " + file.name;

    // Preview only for PDF
    if (file.type === "application/pdf") {
      const fileURL = URL.createObjectURL(file);
      pdfPreview.src = fileURL;
      pdfPreviewBox.style.display = "block";
    }
  });
});
