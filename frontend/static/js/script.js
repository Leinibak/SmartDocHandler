document.addEventListener('DOMContentLoaded', function() {
    const homeScreen = document.getElementById('homeScreen');
    const pdfInvoiceDataContent = document.getElementById('pdfInvoiceDataContent');
    const pdfOtherFeatureContent = document.getElementById('pdfOtherFeatureContent');
    const excelFeature1Content = document.getElementById('excelFeature1Content');
    const excelFeature2Content = document.getElementById('excelFeature2Content');

    const menuHome = document.getElementById('menuHome');
    const menuPDFManagement = document.getElementById('menuPDFManagement');
    const menuInvoiceData = document.getElementById('menuInvoiceData');
    const menuOtherPDFFeature = document.getElementById('menuOtherPDFFeature');
    const menuExcelManagement = document.getElementById('menuExcelManagement');
    const menuExcelFeature1 = document.getElementById('menuExcelFeature1');
    const menuExcelFeature2 = document.getElementById('menuExcelFeature2');

    const pdfMenu = document.getElementById('pdfMenu');
    const excelMenu = document.getElementById('excelMenu');
    const fileInput = document.getElementById('fileInput');
    const fileList = document.getElementById('fileList');
    const fileForm = document.getElementById('fileForm');

    const extractBtn = document.getElementById('extractBtn');
    const clientSelect = document.getElementById('clientSelect');
    const typeSelect = document.getElementById('typeSelect');
    const regionSelect = document.getElementById('regionSelect');
    const successMessage = document.getElementById('successMessage');


    // Show home screen initially
    homeScreen.classList.remove('d-none');

    // Toggle PDF menu and content
    menuPDFManagement.addEventListener('click', () => {
      homeScreen.classList.add('d-none');
      pdfMenu.style.display = 'block';
      excelMenu.style.display = 'none';
    });

    // Show PDF Invoice Data Extraction
    menuInvoiceData.addEventListener('click', () => {
      pdfInvoiceDataContent.classList.remove('d-none');
      pdfOtherFeatureContent.classList.add('d-none');
      excelFeature1Content.classList.add('d-none');
      excelFeature2Content.classList.add('d-none');
    });

    // Show other PDF feature
    menuOtherPDFFeature.addEventListener('click', () => {
      pdfInvoiceDataContent.classList.add('d-none');
      pdfOtherFeatureContent.classList.remove('d-none');
    });

    // Toggle Excel menu and content
    menuExcelManagement.addEventListener('click', () => {
      homeScreen.classList.add('d-none');
      excelMenu.style.display = 'block';
      pdfMenu.style.display = 'none';
    });

    // Show Excel Feature 1
    menuExcelFeature1.addEventListener('click', () => {
      excelFeature1Content.classList.remove('d-none');
      excelFeature2Content.classList.add('d-none');
    });

    // Show Excel Feature 2
    menuExcelFeature2.addEventListener('click', () => {
      excelFeature2Content.classList.remove('d-none');
      excelFeature1Content.classList.add('d-none');
    });


    // Handle the Extract button click
    extractBtn.addEventListener('click', function() {
        const files = fileInput.files;
        if (files.length === 0 || !clientSelect.value || !typeSelect.value || !regionSelect.value) {
            alert('Please select client, type, region and files.');
            return;
        }

        const formData = new FormData();
        formData.append('client', clientSelect.value);
        formData.append('doc_type', typeSelect.value);
        formData.append('region', regionSelect.value);

        for (let i = 0; i < files.length; i++) {
            formData.append('files[]', files[i]);
        }

        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
            successMessage.classList.remove('d-none');
            successMessage.textContent = 'Invoice data successfully extracted and saved as Excel!';
            window.location.href = `/download/${data.output_file}`;
            } else {
            alert('Failed to extract data.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error processing the request.');
        });
    });

    // Event listener for file input
    fileInput.addEventListener('change', function(event) {
      const files = event.target.files; // Get the selected files
      fileList.innerHTML = '';  // Clear previous file list

      // Loop through selected files and add them to the list
      for (let i = 0; i < files.length; i++) {
        const file = files[i];

        // Create a list item for each file
        const listItem = document.createElement('li');
        listItem.classList.add('list-group-item');
        listItem.textContent = file.name; // Display the file name

        // Optionally, add a remove button to remove files from the list
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.classList.add('btn', 'btn-danger', 'btn-sm', 'float-end', 'ms-2');
        removeButton.addEventListener('click', () => {
          listItem.remove();  // Remove the file from the list
        });

        listItem.appendChild(removeButton);
        fileList.appendChild(listItem); // Add the file to the list
      }
    });

    // Handle form submission
    fileForm.addEventListener('submit', function(event) {
      event.preventDefault();

      const selectedFiles = [];
      const listItems = fileList.querySelectorAll('li');

      listItems.forEach(item => {
        selectedFiles.push(item.textContent.replace('Remove', '').trim()); // Get file names from the list
      });

      if (selectedFiles.length > 0) {
        console.log("Selected Files:", selectedFiles);
        alert("Files ready for submission: " + selectedFiles.join(', '));
      } else {
        alert("No files selected.");
      }
    });
});