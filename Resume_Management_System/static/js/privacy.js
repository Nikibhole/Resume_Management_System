function downloadPDF() {
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF();

  doc.setFontSize(18);
  doc.text("Privacy Policy", 20, 20);

  const content = `
Data Usage:
We collect your information solely for job matching purposes. Your data is encrypted and stored securely.

Privacy Commitment:
We never share your personal information without your explicit consent. We respect your privacy rights fully.

Contact & Queries:
Have any concerns? Visit our contact page and we’ll be happy to assist.
`;

  doc.setFontSize(12);
  doc.text(content, 20, 40);
  doc.save("Privacy_Policy.pdf");
}
